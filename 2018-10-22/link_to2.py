import asyncio


async def wetg(host):
    print('web...%s'%host)
    connect = asyncio.open_connection(host,80)
    reader,writer = await connect
    header = 'GET/HTTP/1.0 \r\nHost:%s\r\n\r\n'%host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line ==b'\r\n':
            break
        print('%s host>%s...'%(host,line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wetg(host) for host in ['www.sina.com','www.baidu.com','www.sohu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()




