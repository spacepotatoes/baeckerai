# BäckerAI – Objekterkennung von Backwaren

Dieses Projekt kombiniert ein **Web-Frontend** mit einem **Flask-Backend**, um Bilder von Backwaren automatisch zu analysieren.  
Unterstützte Objekte sind:
- 🥐 Croissants  
- 🥨 Brezeln  
- 🥖 Kaiserbrötchen  

---

## Funktionsweise

1. **Upload im Frontend**  
   Nutzer:innen können ein Bild hochladen (einzelne oder gemischte Backwaren).

2. **Analyse im Backend**  
   - Das Bild wird an den **Flask-Server** geschickt.  
   - Der Server nutzt ein in Google Colab trainiertes **YOLOv10-Objekterkennungsmodell**.  
   - Erkannte Objekte werden mit **Bounding Boxes** und **Confidence Scores** versehen.  
   - Der Server läuft produktiv über **Gunicorn (WSGI)** und ist mit einem von Plesk bereitgestellten **SSL-Zertifikat** abgesichert.

3. **Visualisierung**  
   - Das verarbeitete Bild mit Markierungen wird im Frontend angezeigt.  
   - Zusätzlich können die Erkennungsdaten per Klick auf **Analysieren** mit **Chart.js** grafisch dargestellt werden.

---

## Architektur

- **Frontend:**  
  - HTML/JavaScript-Interface für Upload & Ergebnisanzeige  
  - Chart.js für interaktive Diagramme  

- **Backend:**  
  - Flask-App (`baeckerai_app:app`)  
  - Gunicorn als WSGI-Server (`--bind 0.0.0.0:5000`)  
  - SSL-Absicherung mit Zertifikaten aus Plesk  

---

## Installation & Nutzung

### Voraussetzungen
- Python 3.11+  
- Virtuelle Umgebung empfohlen  
- Gunicorn als WSGI-Server  
- (Optional) Node.js für Frontend-Assets

### Backend starten --- Die Pfade zu den certfiles müssen durch den neuen Admin angepasst werden
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start mit Gunicorn + SSL
gunicorn --bind 0.0.0.0:5000 \
         --certfile /pfad/zertifikat.pem \
         --keyfile /pfad/schluessel.pem \
         baeckerai_app:app
