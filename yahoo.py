# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate  # 引入xml解析模块
from urllib import request  # 引入URL请求模块


class WeatherSaxHandler(object):  # 定义一个天气事件处理器

    weather = {'city': 1, 'forecast': []}  # 初始化城市city和预报信息forecast

    def start_element(self, name, attrs):  # 定义开始标签处理事件

        if name == 'yweather:location':  # 获取location信息
            self.weather['city'] = attrs['city']

        elif name == 'yweather:forecast':  # 获取forecast信息
            self.weather['forecast'].append({
                'date': attrs['date'],
                'high': attrs['high'],
                'low': attrs['low'],
                'text': attrs['text']
            })


def parseXml(xml_str):  # 定义xml解析器

    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)  # 解析xml文本

    print('City: ' + handler.weather['city'])  # 打印city信息
    print('Weather: ')
    for x in handler.weather['forecast']:  # 打印天气信息
        print(x)

    return handler.weather


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'

