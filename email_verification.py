# modules needed
import random
import re
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd


# user credentials to csv
def user_info(pnum,name,email,uid,upasssword):
    fname       = name
    email       = email
    phone_no    = pnum
    passsword  = upasssword
    df          = pd.read_csv('data/user_credentials.csv',index_col=0)
    # df.drop_duplicates(subset=['E-mail','Password'],keep='first',inplace=True)
    df.loc[uid] =  [fname,email,phone_no,passsword]
    df.to_csv('data/user_credentials.csv')

    
# verification code generator
def code_generator():

    random_str = random.randint(100000, 999999)
    return random_str

cc_code = int(code_generator())

# send mail to user and smtp server
def send_email(mail):

    sender_email = "brosbooking3"
    receiver_email = mail
    password = '#axbctTK@bbros_690'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Booking bros verification code"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
    Hi,
    This is your verification code:
    {cc_code}"""
    html = """\
    <html>
    <head>
    <style>
    h1 {{text-align: center;}}
    p {{text-align: center;}}
    strong {{text-align: center;}}
    </style>
    </head>
    <body>
        <h1>Verification</h1>
        <p>Hi,<br>
        This is your verification code:<br>
        <strong> {cc_code} </strong>
        </p>
    </body>
    </html>
    """.format(cc_code=cc_code)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

# check if email is valid or not
def email_validater(email):
    return bool(re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$',str(email)))


