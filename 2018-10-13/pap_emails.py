from email.parser import Parser
from email.header import decode_header
from email.utils import  parseaddr

import poplib



#检测编码
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type =msg.get('Content-Type','').lower()
        pos = content_type.find('charset =')
        if pos >=0:
            charset =content_type[pos + 8:].strip()
    return charset

#邮件编码都需要是str
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

#用于编写邮件显示规范
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From','To','Subject']:
            value =msg.get(header,'')
            if value :
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr ,addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' %(name,addr)
            print('%s%s: %s'%(' '* indent,header,value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n,part in enumerate(parts):
            print('%spart %s'%(' ' * indent,n))
            print('%s ----------------------'%(' '*indent))
            print_info(part,indent+1)
    else:
        content_type = msg.get_content_type()   #获取邮件格式
        if content_type == 'text/plain' or content_type == 'text/html':
            content =msg.get_payload(decode=True)
            charset =guess_charset(msg)
            if charset:
                content =content.decode(charset)
            print('%sText :%s'%(' '*indent,content))
        else:
            print('%sAttachment:%s'%(' '*indent,content_type))

#输入邮箱验证
email = input('Email:')
password = input('Password:')
pop3_server = input('POP_server:')

#连接pop3服务器
server =poplib.POP3_SSL(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

#进行身份验证
server.user(email)
server.pass_(password)

#返回占用空间
print('Message: %s,Size: %s'% server.stat())
resp,mails,octets = server.list()
print(mails)

#获取新的一封邮件，注意索引从1开始
index =len(mails)
resp, lines, octets = server.retr(index)
msg_content = b'\r\n'.join(lines).decode('utf-8')

#解析出邮件
msg = Parser().parsestr(msg_content)

print_info(msg)

#关闭连接
server.quit()


