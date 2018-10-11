from xml.parsers.expat import ParserCreate
from urllib import request

class WeatherSaxHandler(object):

    weather ={'city':1,'forecast':[]}

    def start_element(self,name,attrs):
        if name =='yweather:location':
            self.weather['city']=attrs['city']

        elif name=='yweather:forecast':
            self.weather['forecast'].append({
                'data':attrs['data'],
                'high':attrs['high'],
                'low':attrs['low']
            })

def parseXML(xml_self):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parser(xml_self)

    print('City:',handler.weather['city'])
    print('Weather')
    for x in handler.weather['forecast']:
        print(x)

    return handler.weather

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL,timeout=4) as res:
    data =res.read()
    result =parseXML(data.decode('utf-8'))
assert request['city'] == 'Beijing'

