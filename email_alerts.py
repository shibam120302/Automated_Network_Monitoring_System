# email_alerts.py
# Sends alert emails using SMTP

import smtplib

def send_email_alert(subject, message):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('your_email@gmail.com', 'your_password')
            email_msg = f"Subject: {subject}\n\n{message}"
            smtp.sendmail('your_email@gmail.com', 'target_email@gmail.com', email_msg)
    except Exception as e:
        print(f"Email alert failed: {e}")
