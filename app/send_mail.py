from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import threading
from urllib import request
from itsdangerous import URLSafeTimedSerializer
from app import app, mail


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer('Sm9obiBTY2hyb20ga2lja3MgYXNz')
    return serializer.dumps(email, salt='email_salt')


def confirrm_token(token, expiration=600):
    serializer = URLSafeTimedSerializer('Sm9obiBTY2hyb20ga2lja3MgYXNz')
    try:
        email = serializer.loads(token, salt='email_salt', max_age=expiration)
    except:
        return False
    return email


def send_mail_thread(msg):
    with app.app_context():
        mail.send(msg)
    return 'sent'


def send_confiramation_email(email):
    token = generate_confirmation_token(email)
    # print (token)
    confirmation_url = f"http://www.somewhere.com/anywhere.co?token={token}"
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        from_adr = 'arcgatedemoacc@gmail.com'
        to_adr = email
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('arcgatedemoacc@gmail.com', 'numqjlaaeybcxowl')
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Emailing a link"
        msg['From'] = from_adr
        msg['To'] = to_adr
        html = f"""
        <html>
            <head></head>
                <body>
                    <h2>For Reset Password:</h2>
                    <a href={confirmation_url}>Click Here</a>
                </body>
        </html>
        """
        part = MIMEText(html, 'html')
        msg.attach(part)
        smtp.sendmail('arcgatedemoacc@gmail.com', email, msg.as_string())
    return 'message sent'


def forgot_password_mail(email):
    token = generate_confirmation_token(email)
    confirmation_url = f"http://somewhere.com/anywhere.co?token={token}"
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        from_adr = 'arcgatedemoacc@gmail.com'
        to_adr = email
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('arcgatedemoacc@gmail.com', 'numqjlaaeybcxowl')
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Emailing a link"
        msg['From'] = from_adr
        msg['To'] = to_adr
        html = f"""
        <html>
            <head></head>
                <body>
                    <h2>For Reset Password:</h2>
                    <a href={confirmation_url}>Click Here</a>
                </body>
        </html>
        """
        part = MIMEText(html, 'html')
        msg.attach(part)
        smtp.sendmail(from_adr, to_adr, msg.as_string())
    return 'message sent'
