# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('index.html','r') as file:
  html = file.read()

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

msg = MIMEMultipart('alternative')
msg['Subject'] = "Your account has been compromised."
msg['From'] = "sender@gmail.com"
msg['To'] = "recipt@gmail.com"
part2 = MIMEText(html, 'html')
msg.attach(part2)


# Authentication 
APP_PASS = 'UPDATE THIS FOR YOUR APP PASS'
s.login("sender@gmail.com", APP_PASS) 
  
  
# sending the mail 
s.sendmail(me, you, msg.as_string()) 
  
# terminating the session 
s.quit() 