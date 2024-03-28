import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = 'yourpassword'

class EmailSender:
    def __init__(self):
        self.sender_email = 'youremailadress@gmail.com'
        self.password = password
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587

    def send_email(self, receiver_email, subject, body):
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message(message)

if __name__ == "__main__":
    # Create an instance of EmailSender
    email_sender = EmailSender()

    # Define the email content
    receiver_email = 'sefa.sahan@nl.ey.com'
    subject = 'Feedbacks analyze by Feedback AI APP'
    body = """
    Hello,
    This is a test email sent from Python.
    """

    # Send the email
    email_sender.send_email(receiver_email, subject, body)
    print('Email sent successfully!')
