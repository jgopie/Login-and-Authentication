import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

with open("config.json", mode="r") as config:
    key = json.load(config)
    api_key = key["sendgrid_api_key"]



def send_code(code, user_email):
    message = Mail(
        from_email="jordangopie@live.com",
        to_emails=user_email,
        subject="Your registration was successful",
        html_content=f"""
    <html>
    <head><head>
    <body>
        <p>Your registration was successful. <br>
        Please visit <a href=http://127.0.0.1:5000/verify/{user_email}>this link</a> and enter the code: {code}.
        </p>
    </body>
    </html>
    """
    )
    try:
        sg = SendGridAPIClient(api_key=api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


# def send_code(code, user_email):
#     with smtplib.SMTP("smtp.sendgrid.net") as connection:
#         connection.starttls()
#         message = create_message(code, user_email, from_email="jordangopie@live.com")
#         connection.login(user=test_email, password=test_email_password)
#         connection.sendmail(from_addr="jordangopie@live.com", to_addrs=user_email, msg=message.as_string())


def create_message(code, user_email, from_email):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Registration Successful"
    msg["From"] = from_email
    msg["To"] = user_email
    email_text = f"Your registration was successful. Please visit http://127.0.0.1:5000/verify/{user_email} and enter the code {code}."
    html_text = f"""\
    <html>
    <head><head>
    <body>
        <p>Your registration was successful. <br>
        Please visit <a href=http://127.0.0.1:5000/verify/{user_email}>this link</a> and enter the code: {code}.
        </p>
    </body>
    </html>
    """
    part1 = MIMEText(email_text, "plain")
    part2 = MIMEText(html_text, "html")
    msg.attach(part1)
    msg.attach(part2)
    return msg
