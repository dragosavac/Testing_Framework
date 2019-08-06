import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email_user = "Rade"
email_send = "rade.dragosavac@symphony.is"
subject = "Python"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
body = "This is a random automatic message from Selenium/Python!"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_user, "")


server.sendmail(email_user, email_send, text)
server.quit()
