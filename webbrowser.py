import itertools

def pi(N):
    y = itertools.count(1)
    list1 = itertools.takewhile(lambda x: x<=N,y)
    list2 = list(list1)
    c = 0
    for n in list2:
        n = 2*n-1
        if ((n+1)/2)%2 ==0 :
            n =-4/n
        else:
            n =4/n
        c += n
    return c

print(pi(1000))




