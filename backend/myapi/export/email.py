from email.mime.application import MIMEApplication
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class send_email:

    # Einstellungen für den E-Mail-Server
    email_host = 'smtp.gmail.com'
    email_port = 587  # Der Port kann je nach Anbieter variieren
    email_username = 'optimate.development@gmail.com'
    email_password = 'gwxn lebw fhmy relb'

    # E-Mail-Einstellungen
    from_email = 'optimate.development@gmail.com'
    subject = 'Ihre OptiMate-Untersuchung'

    def __init__(self, first_name, last_name, email, pdf_base64):
        self.first_name = first_name
        self.last_name = last_name
        self.to_email = email
        self.pdf_base64 = pdf_base64
        self.message = f"""
        Sehr geehrte/r {self.first_name} {self.last_name}!\n
        Im Anhang finden Sie die Ergebnisse Ihrer OptiMate Untersuchung.\n
        Mit freundlichen Grüßen
        Ihr OptiMate-Team."""

    def send_email(self): 
        # Erstelle eine MIME-Nachricht
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = self.subject

        # Füge den Nachrichtentext hinzu
        msg.attach(MIMEText(self.message, 'plain'))

        # Decode the base64 PDF and attach it
        pdf_data = base64.b64decode(self.pdf_base64)
        pdf_attachment = MIMEApplication(pdf_data, _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename="OptiMate_Untersuchung.pdf")
        msg.attach(pdf_attachment)

        try:
            # Verbinde dich mit dem SMTP-Server
            server = smtplib.SMTP(self.email_host, self.email_port)
            server.starttls()
            server.login(self.email_username, self.email_password)
            
            # Sende die E-Mail
            server.sendmail(self.from_email, self.to_email, msg.as_string())
            print('E-Mail erfolgreich gesendet!')
            
        except Exception as e:
            print(f'Fehler beim Senden der E-Mail: {str(e)}')
            
        finally:
            # Schließe die Verbindung zum Server
            server.quit()