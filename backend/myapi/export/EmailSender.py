from email.mime.application import MIMEApplication
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:

    # Properties of email server
    email_host = 'smtp.gmail.com'
    email_port = 587
    email_username = 'optimate.development@gmail.com'
    email_password = 'gwxn lebw fhmy relb'

    # E-Mail-Properties
    from_email = 'optimate.development@gmail.com'
    subject = 'Ihre OptiMate-Untersuchung'

    def __init__(self, first_name, last_name, email, pdf_base64):
        """
            Initializes an object with the given user information and a message.

            :param first_name: First name of the recipient
            :param last_name: Last name of the recipient
            :param email: Email address of the recipient
            :param pdf_base64: Base64-encoded PDF file to be sent as an attachment
            :return: None
        """
        
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
        """
            Sends an email with a text message and a PDF attachment.

            :return: None
            :raises Exception: If there is an error while sending the email
        """
        
        # Create a MIME-Message
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = self.subject

        # Attach the message text
        msg.attach(MIMEText(self.message, 'plain'))

        # Decode the base64 PDF and attach it
        pdf_data = base64.b64decode(self.pdf_base64)
        pdf_attachment = MIMEApplication(pdf_data, _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename="OptiMate_Untersuchung.pdf")
        msg.attach(pdf_attachment)

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(self.email_host, self.email_port)
            server.starttls()
            server.login(self.email_username, self.email_password)
            
            # Send the email
            server.sendmail(self.from_email, self.to_email, msg.as_string())
            
        except Exception as e:
            # Print the error if sending the email fails
            print(f'Fehler beim Senden der E-Mail: {str(e)}')
            
        finally:
            # Close the connection to the server
            server.quit()