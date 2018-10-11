from html.parser import HTMLParser
from urllib import request
import requests
import re


class MyHTMLParser(object):

    def __init__(self):        #d定义存放数据
        HTMLParser.__init__(self)
        self.is_time =False
        self.is_title =False
        self.is_location =False
        self.is_year =False
        self.info =[]

    def handle_starttag(self,tag,attrs):   #定义抓取内容位置
        if tag == 'time' :
            self.is_time =True
        if tag == 'h3' and ('class','event-title') in attrs:
            self.is_title =True
        if tag =='span' and ('class','event-location') in attrs:
            self.is_location =True
        if tag =='span' and ('class','say-no-more') in attrs:
            self.is_year =True

    def handle_data(self,data):            #定义抓取数据
        if self.is_time ==True:
            self.is_time =False
            self.info.append(dict(会议时间=data))
        if self.is_title ==True:
            self.is_title =False
            self.info.append(dict(会议名称=data))
        if self.is_location ==True:
            self.is_location =False
            self.info.append(dict(会议地址=data))
        if self.is_year ==True:
            self.is_year =False
            if re.match(r'[0-9]',data.strip()):
                self.info.append(dict(会议年份=data))

def getinfo(data,u):            #定义如何显示数据
    parser = MyHTMLParser()
    parser.feed(data)
    count = 0
    print('抓取数据如下：%s\n抓取信息如下：'%u)
    for x in parser.info:
        for key in x:
            print(key+':'+str(x[key]))
        count +=1
        if count %4 ==0 :
            print('-----------------------')

web ='https://www.python.org/events/python-events/'     #输入网址
with requests.get(web) as res:
    getinfo(res,web)

