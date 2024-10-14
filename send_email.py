import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from kafka import KafkaConsumer
import json
from key import smtp_password,recipient_email,smtp_user

# E-posta ayarları
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = smtp_user
smtp_password = smtp_password
recipient_email = recipient_email


consumer = KafkaConsumer(
    'GREATER_THAN_NINE_STREAM',
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, recipient_email, msg.as_string())

def consume_and_send_emails():
    for message in consumer:
        data = message.value
        print(f"Alınan veri: {data}")  
        if 'NUMBER' in data:
            number = data['NUMBER']
            timestamp = data['TIMESTAMP']
            subject = f"New Number Alert: {number}"
            body = f"A new number greater than 9 has been detected.\n\nNumber: {number}\nTimestamp: {timestamp}"
            send_email(subject, body)
            print(f"E-posta gönderildi: {data}")
        else:
            print("Mesajda 'NUMBER' anahtarı bulunamadı.")

if __name__ == '__main__':
    consume_and_send_emails()
