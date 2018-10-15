import os,datetime


timef = datetime.datetime.today()
name = str(timef.strftime('%Y-%m-%d'))
os.makedirs(name,exist_ok=True)
