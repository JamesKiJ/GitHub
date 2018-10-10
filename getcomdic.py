import requests,bs4,os

url = 'http://www.xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...'%url)
    res =requests.get(url)
    res.raise_for_status()
    soup =bs4.BeautifulSoup(res.text)
    comicElem =soup.select('#comic img')
    if comicElem ==[]:
        print('Could you find comic image...')
    else:
        comicURL = 'http:'+comicElem[0].get('src')
        print('Downloading image %s...'%(comicURL))
        res =requests.get(comicURL)
        res.raise_for_status()
        imageFile =open(os.path.join('xkcd',os.path.basename(comicURL)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    preLink =soup.select('a[rel="prev"]')[0]
    url ='http://www.xkcd.com'+preLink.get('href')

print('Done.')

