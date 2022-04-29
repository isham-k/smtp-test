# Import required files here
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import re
import os
 
# Initialising MIMEMultipart
msg = MIMEMultipart()

# Regex validator for validating email
# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Message and subject to be sent
message = "This is an email sent for test purpose."
msg['Subject'] = "Test Mail."

# function for checking whether the mail is valid or not.(if valid, return mailid or return null
def is_valid_mail(regex, mail):
    if re.match(regex, mail):
        return mail
    return None
 
# Function for sending mail
def send_mail():
    try:
        username = input("Enter your SMTP username : ")
        password = input("Enter your SMTP password : ")
        smtphost = input("Enter your smtp host : ")

        #check whether the from mail and to mails are valid or not
        f=lambda from_mail: (is_valid_mail(regex,from_mail)) or (f(input("please enter a valid mail..\nEnter From Mail : ")))
        msg['From'] = f(input("Enter From Mail : "))

        f=lambda from_mail: (is_valid_mail(regex,from_mail)) or (f(input("please enter a valid mail..\nEnter To Mail : ")))
        msg['To'] = f(input("Enter To Mail : "))
        
       #sending email using smtplib sendmail
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP(smtphost)
        
        server.starttls()
        
        server.login(username, password)
        
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
        
        print ("Successfully sent email to : %s 😁" % (msg['To']))

    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print("exception here : ",e)
        os._exit(0)

# call the function for sending mail from here
res = send_mail()

# Happy Coding 😁
