import asyncio

from aiohttp import web
from flask import Flask,request


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>hello,world</h1>\r\n<p><input name="username"></p>\r\n<p><input password="password" type="password"></p>\r\n<p><button type="submit">Sign In</button></p>\r\n</form>'
                      b'\r\n\r\n@app.route(methods["POST"])\r\nif request.form["username"]=="admin" and request.form["password"]=="password":\r\nreturn "<h3>Hello,Mickle</h3>" ',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello,%s!</h1>\r\n<style>\r\nh1{color:#333333;font-size:48px;text-shadow:3px 3px 3px #666666;}\r\n</style>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
