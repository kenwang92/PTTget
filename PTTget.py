import requests
import time
from bs4 import BeautifulSoup
import re

print('PTT開爬')

r = requests.Session()

need = {
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
}#因為用post所以要header

fake = r.post('https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html',need)
soup = BeautifulSoup(fake.text,'html.parser')
UP = soup.find_all('a',{"class":"btn wide"})
UPnum = re.findall(r'\d+',str(UP))#找出每次上一頁按鈕不同部份(不同部份在href中index後面的一串數字))
UPnum = UPnum[1]
#記得抓第一頁
for soup in soup.find_all('div',{"class":"r-ent"}):
    if soup.find('div','author').string == '-':#是否被刪文
        pass
    else:
        if soup.find('span'):#判斷有沒有得抓推文數
            print(soup.find('span').string, soup.find('a').string, 'https://www.ptt.cc', end='')
            print(soup.find('a')['href'])#有的話抓推文數,標題和連結
        else:
            print(' ',soup.find('a').string, 'https://www.ptt.cc', end='')
            print(soup.find('a')['href'])

while(1):
    url = 'https://www.ptt.cc/bbs/Gossiping/index'+UPnum+'.html'
    req = r.get(url)
    soup = BeautifulSoup(req.text,'html.parser')
    UP = soup.find_all('a',{"class":"btn wide"})
    for c in soup.find_all('div',{"class":"r-ent"}):
        if c.find('div','author').string == '-':#是否被刪文
            pass
        else:
            if c.find('span'):#判斷有沒有得抓推文數
                print(c.find('span').string, c.find('a').string, 'https://www.ptt.cc', end='')
                print(c.find('a')['href'])#有的話抓推文數,標題和連結
            else:
                print(c.find('a').string, 'https://www.ptt.cc', end='')
                print(c.find('a')['href'],end='')
    #取下次要用的按紐值
    UPnum = re.findall(r'\d+',str(UP))
    UPnum = UPnum[1]
    time.sleep(5)
