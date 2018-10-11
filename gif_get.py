import requests,os,bs4


URL = 'http://docs.python-requests.org/zh_CN/latest/index.html#'
os.makedirs('requests',exist_ok=True)
print('Download page %s..'%URL)
res =requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
requests_jpg = soup.select('img[class="logo"]')
if requests_jpg  == []:
    print('Download you need png is not exist...')
else:
    requests_png = 'http://docs.python-requests.org/zh_CN/latest/'+requests_jpg[0].get('src')
    print('Download you need png...%s'%requests_png)
    res1 = requests.get(requests_png)
    res1.raise_for_status()
    imageFile = open(os.path.join('requests',os.path.basename(requests_png)),'wb')
print('Done')
