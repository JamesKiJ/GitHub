import requests,bs4,os

def research_pic(item):
    select_pic =str(item)
    URL = 'https://www.veer.com/query/image?phrase='+select_pic+'&key=IT1399'
    os.makedirs('pic',exist_ok=True)
    while not URL.endswith('#'):
        res = requests.get(URL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        pic_select = ''.join(soup.select('a[class="asset_link draggable"]'))
        for pic in pic_select:
            pic_url =r'href="(.+?/&key=IT1399)" target'
            print('Download you need pic...%s'%pic_url)
            res_pic =requests.get(pic_url)
            res.raise_for_status()
            imageFile = open(os.path.join('pic',os.path.basename(pic_url)),'wb')
            imageFile.close()

research_pic('白色')








