#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText

def send_test_email():
    # Konfiguriere die E-Mail
    sender = "kontakt@giuseppe-troiano.de"    # Ersetze dies durch deine Absenderadresse
    recipient = "gt-foto@gmx.de"      # Ersetze dies durch die Empfängeradresse
    subject = "Test-E-Mail von Supervisor Mail Alert"
    body = "Dies ist eine Test-E-Mail, um die SMTP-Funktion zu prüfen."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    # Verbindung zum lokalen SMTP-Server auf Port 25 herstellen
    smtp_host = "localhost"
    smtp_port = 25

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            # Optional: Falls dein SMTP-Server Authentifizierung benötigt, logge dich ein:
            # server.login("dein-benutzer@example.com", "dein-passwort")
            server.send_message(msg)
            print("Test-E-Mail erfolgreich versendet!")
    except Exception as e:
        print("Fehler beim Senden der Test-E-Mail:", e)

if __name__ == '__main__':
    send_test_email()
