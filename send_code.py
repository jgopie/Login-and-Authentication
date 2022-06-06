import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

test_email = "apikey"
test_email_password = "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"


def send_code(code, user_email):
    with smtplib.SMTP("smtp.sendgrid.net") as connection:
        connection.starttls()
        message = create_message(code, user_email, from_email="jordangopie@live.com")
        connection.login(user=test_email, password=test_email_password)
        connection.sendmail(from_addr="jordangopie@live.com", to_addrs=user_email, msg=message.as_string())


def create_message(code, user_email, from_email):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Registration Successful"
    msg["From"] = from_email
    msg["To"] = user_email
    email_text = f"Your registration was successful. Please visit http://127.0.0.1:5000/verify and enter the code {code}."
    html_text  = f"""\
    <html>
    <head><head>
    <body>
        <p>Your registration was successful. <br>
        Please visit <a href=http://127.0.0.1:5000/verify>this link</a> and enter the code: {code}.
        </p>
    </body>
    </html>
    """
    part1 = MIMEText(email_text, "plain")
    part2 = MIMEText(html_text, "html")
    msg.attach(part1)
    msg.attach(part2)
    return msg
