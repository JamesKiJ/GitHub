from email.mime.text import MIMEText


msg =MIMEText('hello,send by Python...','plain','utf-8')
from_addr =input('From:')
password =input('Password:')
to_addr =input('To:')
stmp_server = input('SMTP server: ')

import  smtplib

server = smtplib.SMTP(stmp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
