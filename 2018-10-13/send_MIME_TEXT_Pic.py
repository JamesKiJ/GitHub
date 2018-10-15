from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.image import MIMEImage
from email import encoders


import smtplib
import random


def _format_addr(s):
    name,addr =parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From:')
password =input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP Server:')
smtp_port = 587

msg =MIMEMultipart()
msg['From'] =_format_addr('yao<%s>'%from_addr)
msg['To'] = _format_addr('管理员<%s>'%to_addr)
msg['Subject'] = Header('SMTP_test','utf-8').encode()

msg.attach(MIMEText('<html><body><h1>hello,my friend...</h1>'+'<p><img src="cid:0"></p>'+'</body></html>','html','utf-8'))

with open('/Users/yaoming/Desktop/GitHub/thum.jpg','rb') as f:
    mime = MIMEBase('image','jpg',filename = 'thum.jpg')
    mime.add_header('Content-Disposition','attachment',filename='thum.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('x-Attachment-id','ID')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

