import requests
import time
from bs4 import BeautifulSoup
import re

class color:
    numless10 = '\033[32m'
    numuch10 = '\033[33m'
    numboom = '\033[31m'
    numx = '\033[33m'
    numrst = '\033[0m'
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
        if soup.find('span'):#判斷有沒有得抓推文數,有的話抓推文數,標題和連結
            spanstr = soup.find('span').string
            if(spanstr.isdigit()):
                if (int(spanstr) < 10):#推文數小於10用綠色,大於用黃色
                    print(' ' + color.numless10 + soup.find('span').string, end=' ')
                    print(color.numrst + soup.find('a').string, 'https://www.ptt.cc', end='')
                    print(soup.find('a')['href'])
                else:
                    print(color.numuch10 + soup.find('span').string, end=' ')
                    print(color.numrst + soup.find('a').string, 'https://www.ptt.cc', end='')
                    print(soup.find('a')['href'])
            else:#爆文或X...要紅色或灰色
                if (spanstr == '爆'):#推文數為爆用紅色,x..用灰色
                    print(color.numboom + soup.find('span').string, end=' ')
                    print(color.numrst + soup.find('a').string, 'https://www.ptt.cc', end='')
                    print(soup.find('a')['href'])
                else:
                    print(color.numx + soup.find('span').string, end=' ')
                    print(color.numrst + soup.find('a').string, 'https://www.ptt.cc', end='')
                    print(soup.find('a')['href'])
        else:
            print('  ',soup.find('a').string, 'https://www.ptt.cc', end='')
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
            if c.find('span'):#判斷有沒有得抓推文數有的話抓推文數,標題和連結
                spanstr2 = c.find('span').string
                if(spanstr2.isdigit()):
                    if (int(c.find('span').string) < 10):#推文數小於10用綠色,大於用黃色
                        print(' ' + color.numless10 + c.find('span').string, end=' ')
                        print(color.numrst + c.find('a').string, 'https://www.ptt.cc', end='')
                        print(c.find('a')['href'])#有的話抓推文數,標題和連結
                    else:
                        print(color.numuch10 + c.find('span').string, end=' ')
                        print(color.numrst + c.find('a').string, 'https://www.ptt.cc', end='')
                        print(c.find('a')['href'])#有的話抓推文數,標題和連結
                else:#爆文或X...要紅色或灰色
                    if (soup.find('span').string == '爆'):#推文數為爆用紅色,x..用灰色
                        print(color.numboom + c.find('span').string, end=' ')
                        print(color.numrst + c.find('a').string, 'https://www.ptt.cc', end='')
                        print(c.find('a')['href'])#有的話抓推文數,標題和連結
                    else:
                        print(color.numx + c.find('span').string, end=' ')
                        print(color.numrst + c.find('a').string, 'https://www.ptt.cc', end='')
                        print(c.find('a')['href'])#有的話抓推文數,標題和連結
            else:
                print('  ',c.find('a').string, 'https://www.ptt.cc', end='')
                print(c.find('a')['href'])
    #取下次要用的按紐值
    UPnum = re.findall(r'\d+',str(UP))
    UPnum = UPnum[1]
    time.sleep(5)
