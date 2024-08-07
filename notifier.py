import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

def send_email_notification(task_name, task_status, recipient_email):

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg['Subject'] = f'Task Notification: {task_name}'

    if task_status.lower() == "success":
        body = f"Congratulations! The task '{task_name}' was completed successfully."
    else:
        body = f"Alert: The task '{task_name}' failed to complete."

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, recipient_email, text)
        server.quit()
        print(f"Notification sent to {recipient_email} for task '{task_name}'.")
    except Exception as e:
        print(f"Failed to send notification. Error: {e}")

def notify_on_event(event_name, event_status, notification_method, contact_info):

    if notification_method.lower() == "email":
        if event_status.lower() == "completed":
            send_email_notification(event_name, "Success", contact_info)
        else:
            send_email_notification(event_name, "InProgress", contact_info)