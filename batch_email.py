import os
import smtplib
from email.message import EmailMessage
import pandas as pd

email_addr = os.environ.get('airful_email_addr')
email_pass = os.environ.get('airful_email_pass')

print(email_addr, email_pass)

df = pd.read_csv(r'/mnt/c/users/Clive/Desktop/test.csv')
contacts = df['email'].tolist()
v = ', '.join(contacts)
print(v)
print(type(v), len(v))
#print(contacts)

for i in v:
    if cntr = 2
        msg = EmailMessage()
        msg['Subject'] = 'Invitation for Job Hunt'
        msg['From'] = email_addr
        msg['bcc'] = ', '.join(contacts)

        msg.set_content("""\
            Hello there, 
            \n \n I hope you and your family are well! 
            \n I am writing to you to introduce you to an innovative, new platform on behalf of the team at GeekTrust! 
            \n \n GeekTrust helps in finding great jobs for software engineering professionals and onboarding them at some of the fastest growing Indian startups. Compensation and salaries are above market standards. 
            \n \n The platform features coding challenges, exposure to open job positions at renowned companies and seamlessly manages the interviewing process - all in pursuit of giving you a great job hunting experience and land something really game changing for your career! 
            \n \n Check it out here → Link : https://www.geektrust.in/?refToken=28cf61c2b9ba3de4002b27 
            \n \n Thank you,
            \n Subhro,
            \n On Behalf on GeekTrust""")

        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <body>
                Hello there,
                <br><br>I hope you and your family are well!
                <br>I am writing to you to introduce you to an innovative, new platform on behalf of the team at GeekTrust!
                <br><br>GeekTrust helps in finding great jobs for software engineering professionals and onboarding them at some of the fastest growing Indian startups. Compensation and salaries are <i><b>above</b></i> market standards.
                <br><br>The platform features coding challenges, exposure to open job positions at renowned companies and seamlessly manages the interviewing process - all in pursuit of giving you a great job hunting experience and land something really game changing for your career!
                <br><br>Check it out here → <a href="https://www.geektrust.in/?refToken=28cf61c2b9ba3de4002b27">Link</a>
                <br><br>Thank you,
                <br>Subhro,
                <br>On Behalf of GeekTrust.
            </body>
        </html>
        """, subtype = 'html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as i:
            i.login(email_addr, email_pass)
            i.send_message(msg)