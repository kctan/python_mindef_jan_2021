import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Prepare email for sending attachment
msg = MIMEMultipart()
#
# HTML message for the email body
html = """
<html>
  <head></head>
  <body>
       <h1>Hello</h1>
       <img src='cid:image1'>
    </p>
  </body>
</html>
"""
# Add the HTML text using MIMEText
html = MIMEText(html, 'html')

msg.attach(html)
f = open('android.png', "rb")
# Create the MIMEImage object
img = MIMEImage( f.read() )
# Note how "<image1>" below for Content-ID match the HTML "src" above
img.add_header('Content-ID', '<image1>')
# Always close after done reading
f.close()
# Set it to be viewed "inline"
img.add_header('Content-Disposition', 'inline', filename='android.png')
msg.attach(img)



sender_email_address ="sitsprint@gmail.com"
sender_email_password = "uurltlnomitneezj"
receiver_email_address = "tkokchen@gmail.com"
#email_title_content = "Subject: Sending Email Using Python\nThis is a test mail.f"

print("Trying to connect o Gmail SMTP server")
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

print("Connected.  Logging in...")
smtpObj.login(sender_email_address, sender_email_password)

smtpObj.sendmail(sender_email_address, receiver_email_address,  msg.as_string())
print("Email sent successfully...")

smtpObj.quit()
