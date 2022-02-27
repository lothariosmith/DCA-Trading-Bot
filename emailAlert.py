from http import server
import smtplib
from email.message import EmailMessage
import email
import imaplib
import easyimap as e

# Send email script

answer = ""

def market_notification(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "ENETR EMAIL HERE"
    msg['from'] = user
    password = "ENETR PASSWORD HERE"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


# Receive Email Script

def readEmail():
    user = "ENTER EMAIL HERE"
    password = "ENTER PASSWORD HERE"
    server = e.connect("imap.gmail.com", user, password)
    #server.listids()
    email = server.mail(server.listids()[0])
    ans = email.title
    ans = ans.upper()
    answer = str(ans)
    print(answer)

