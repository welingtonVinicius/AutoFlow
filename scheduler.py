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

scheduler = BackgroundScheduler(daemon=True)

scheduler.add_job(update_task_status, 'interval', minutes=int(os.getenv('UPDATE_TASK_INTERVAL', '60')))
scheduler.add_job(send_notifications, 'interval', minutes=int(os.getenv('NOTIFICATION_INTERVAL', '30')))

@app.before_first_request
def start_scheduler():
    scheduler.start()

def export_scheduler_start():
    start_scheduler()

@app.route('/')
def home():
    return "Application is running!"

if __name__ == '__main__':
    app.run()