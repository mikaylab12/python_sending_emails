# exercise: sending email with a subject of "Greetings"
# email must be sent to lecturer and two of my friends
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'mikaylabeelders@gmail.com'
receiver_email_id = 'thapelo@lifechoices.co.za, tashwilla27@gmail.com, godwin@lifechoices.co.za, mikayla@trade245.com, lizzystrachan99@gmail.com'
# enter sender's password
password = input("Enter your password: ")
# subject of email
subject= "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To']= receiver_email_id
msg['Subject']= subject
# email body/text/message to be displayed
body = "Hi guys, I am sorry for disturbing you, but this email was sent as part of an exercise\n"
body = body + "I hope you have a good day further."
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
# start TLS for security
s.starttls()
s.login(sender_email_id, password)
# sending email
s.sendmail(sender_email_id, receiver_email_id, text)
# terminate session
s.quit()