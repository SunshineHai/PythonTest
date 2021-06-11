#1.获取给定页面里的链接
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.baidu.com/')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])