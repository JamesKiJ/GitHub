from email import  encoders
from email.header import Header
from email.mime.text import MIMEText,MIMENonMultipart
from  email.utils import parseaddr,formataddr


import smtplib

def _format_addr(s):
    name,addr =parseaddr(s)
    return  formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_lib =input('SMTP server:')


msg = MIMEText('i am a good man','plain','utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' %from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SYTMP的问候....','utf-8').encode()

server = smtplib.SMTP(smtp_lib,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


