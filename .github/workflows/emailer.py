import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def send_email(jobs):
    msg = EmailMessage()
    msg["Subject"] = f"Daily Jobs – {len(jobs)} EU / Remote roles"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    body = ""
    for job in jobs:
        body += f"""
{job['title']}
{job['company']}
{job['link']}
Posted: {job['date']}
---------------------------
"""

    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
