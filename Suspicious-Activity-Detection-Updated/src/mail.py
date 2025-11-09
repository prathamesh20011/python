"""
Email notification system for suspicious activity detection
"""

import smtplib
from email.message import EmailMessage

# Email configuration - UPDATE THESE WITH YOUR CREDENTIALS
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
RECIPIENT_EMAIL = "recipient@gmail.com"

def send_alert():
    try:
        print("Sending email alert...")
        msg = EmailMessage()
        msg['Subject'] = "Suspicious Activity Detection Alert"
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg.set_content('Suspicious Activity Detected in CCTV footage. Please check immediately.')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print("Alert email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_alert()