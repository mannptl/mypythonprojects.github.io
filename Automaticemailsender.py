import smtplib
import os
from email.message import EmailMessage

email_id = os.environ.get("EMAIL_ADDR")
email_pass = os.environ.get("EMAIL_PASS")

with smtplib.SMTP_SSL("smtp.gmail.com" , 465) as smtp :
    smtp.login(email_id,email_pass)

    subject = "Hello Coders!!"
    body =  " Welcome to world of python"

    msg = f"Subject : {Subject}\n\n\n{body}"
    smtp.sendmail(email_id,"compify.works@gmail.com" , msg)