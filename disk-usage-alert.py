import os
import psutil
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# SendGrid credentials
sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
email_receiver = os.getenv('RECEIVER_EMAIL')

# Function to send email
def send_email(subject, msg):
    message = Mail(
        from_email=os.getenv('SENDER_EMAIL'),
        to_emails=email_receiver,
        subject=subject,
        plain_text_content=msg)
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Function to check disk usage
def check_disk_usage():
    hdd = psutil.disk_usage('/')
    print("Current disk usage: ", hdd.percent)
    return hdd.percent

# Check disk usage
disk_usage = check_disk_usage()

if disk_usage >= 85:
    send_email("Disk Usage Warning", "Disk usage is at or above 85%. Please free up some space.")
