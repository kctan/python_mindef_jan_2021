import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#Prepare email for sending attachment

msg = MIMEMultipart()
zipfile = open("attach.zip", "rb")  
zip = MIMEBase('application', 'zip', name="attach.zip")
zip.set_payload(zipfile.read())
zipfile.close()
#
encoders.encode_base64(zip)
msg.attach(zip)


sender_email_address ="sitsprint@gmail.com"
sender_email_password = "uurltlnomitneezj"
receiver_email_address = "tkokchen@gmail.com"
email_title_content = "Subject: Sending Email Using Python\nThis is a test mail.f"

print("Trying to connect o Gmail SMTP server")
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

print("Connected.  Logging in...")
smtpObj.login(sender_email_address, sender_email_password)

smtpObj.sendmail(sender_email_address, receiver_email_address,  msg.as_string())
#smtpObj.sendmail(sender_email_address, receiver_email_address,  email_title_content)
print("Email sent successfully...")

smtpObj.quit()
