from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def update_task_status():
    print("Updating task status...")

def send_notifications():
    print("Sending notification...")

def configure_scheduler(scheduler):
    update_interval = int(os.getenv('UPDATE_TASK_INTERVAL', '60'))
    notification_interval = int(os.getenv('NOTIFICATION_INTERVAL', '30'))

    scheduler.add_job(update_task_status, 'interval', minutes=update_interval)
    scheduler.add_job(send_notifications, 'interval', minutes=notification_interval)

def init_scheduler():
    scheduler = BackgroundScheduler(daemon=True)
    configure_scheduler(scheduler)
    scheduler.start()

@app.before_first_request
def prepare_app():
    init_scheduler()

@app.route('/')
def home():
    return "Application is running!"

if __name__ == '__main__':
    app.run()