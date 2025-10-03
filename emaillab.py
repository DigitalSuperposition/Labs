from smtplib import SMTP
from email.message import EmailMessage
import smtplib
import datetime
import schedule
import win32com.client



#Server configuration /authenication
with smtplib.SMTP.connect(host='', port=) as server:
    server.starttls()
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, input("Enter pin:"))
    server.quit()
	
namespace = outlook.GetNamespace("MAPI")

#EmailMessage information
sender_email = "ammon.fasusi.ctr@marines.usmc.mil"
receiver_email = "ammon.fasusi.ctr@marines.usmc.mil"
subject = "python test email"
body = "This is a test email sent from python script,if this goes through, congratulations, this means that the email sent through script was sucessful."

""" msg = EmailMessage()

msg['From'] = "Python Script <rcen.@marines.usmc.mil>"
msg['To'] = receiver_email
msg['subject'] = subject
msg['X-Mailer'] = "Python smtplib"
msg.set_content(body + "\n Sent using Python smtplib") """

print(response, traf_res )




