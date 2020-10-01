import smtplib
import getpass
import pyttsx3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

inpass = getpass.getpass ("Enter your password :")
apass = "rahuljoshi"
if inpass!=apass:
    pyttsx3.speak("Incorrect Password Try Again ")
    exit()
from_addr='email_address'
to_addr=['abcd@gmail.com','asdavegf.@gmail.com']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='Notice'

body='This is to inform you that.....'

msg.attach(MIMEText(body,'plain'))

#Here you have to specify your email and password
email='YOUR_EMAIL'
password='YOUR_PASSWORD'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()
