from smtplib import SMTP
from email.message import EmailMessage
#from getpass import getpass #encrypt
import smtplib
import datetime
import schedule
import win32com.client
import platform


#EmailMessage information
sender_email = "first.last@domain.tld"
receiver_email = "first.last@domain.tld"
subject = "python test email"
body = """This is a test email sent from python script,if this goes through, congratulations, this means that the email sent through script was sucessful."""

msg = EmailMessage()

python_info = f"Python/{platform.python_version()} ({platform.system()} {platform.release()})"

msg['From'] = sender_email
msg['To'] = receiver_email
msg['subject'] = subject
msg['X-Python-Info'] = python_info
msg.set_content(
    body + f"\nPython {platform.python_version()} ({platform.system()} {platform.release()})" #Platform and OS in email.
)

try:
#Connect to relay server, server type using, All available IPv4/6
    with smtplib.SMTP(host='IP address or server name resolve', port=#) as server:
        server.set_debuglevel(1)    #Enable debug output.
        response = server.ehlo()
        server.starttls()
        #server.login("username", "pin or password") #If login is required.
        response = server.ehlo()
        server.send_message(msg)
        #server.quit()

except Exception as e:
    print(f"General error: {e}")

print("EHLO response", response )






