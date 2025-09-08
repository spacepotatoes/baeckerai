from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import os
import signal
import sys

# Signal-Handler definieren
def graceful_shutdown(signum, frame):
    print(f"Signal {signum} empfangen. Fahre mit dem Herunterfahren fort.")
    # Hier kannst du weitere Aufräumarbeiten durchführen, falls nötig.
    sys.exit(0)

# Registriere die Handler für SIGTERM und SIGINT
signal.signal(signal.SIGTERM, graceful_shutdown)
signal.signal(signal.SIGINT, graceful_shutdown)

app = Flask(__name__)
CORS(app)

# YOLO-Modell laden (Passe den Pfad an dein eigenes Modell an)
model = YOLO("best_crois_bretzel4.pt")

@app.route('/ping', methods=['GET'])
def ping():
    """
    Einfache Route, um den Serverstatus zu prüfen.
    Gibt { "status": "OK" } zurück, wenn der Server läuft.
    """
    return jsonify({"status": "OK"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty file"}), 400

    # Temporäre Bilddatei speichern
    image_path = "temp_image.jpg"
    file.save(image_path)

    # YOLO-Inferenz
    results = model(image_path)
    os.remove(image_path)  # Aufräumen

    # Bounding Boxes extrahieren
    predictions = []
    for result in results:
        for box in result.boxes:
            bbox = box.xyxy[0].tolist()   # [x1, y1, x2, y2]
            class_id = int(box.cls[0])
            conf = float(box.conf[0])
            predictions.append({
                "class": model.names[class_id],
                "confidence": conf,
                "bbox": bbox
            })

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        ssl_context=(
            '/opt/psa/var/certificates/scfO4aS0x',  # Zertifikat
            '/opt/psa/var/certificates/scfO4aS0x'   # Privater Schlüssel
        ),
        debug=True
    )
