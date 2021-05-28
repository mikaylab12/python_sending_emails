# sending simple email using python
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'mikaylabeelders@gmail.com'
receiver_email_id = 'mikayla@trade245.com'
# senders password
password = input("Enter your password: ")
s.starttls()
s.login(sender_email_id, password)
# message that will be displayed
message = "Hi there"
message = message + "Did this work?"
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating after email sent
s.quit()