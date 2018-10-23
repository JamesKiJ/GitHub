def consumer():
    r = ''
    while True:
        n = yield r
        if not n :
            return
        print('[CONSUER]Consuming %s...'%n)
        r ='200 ok'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n +=1
        print('[PRODUCE] Consuming %s...'%n)
        r = c.send(n)
        print('[PRODUCE] Consumer return :%s..'%r)
        print('test...%s'%n)
    c.close()

c =consumer()
produce(c)


