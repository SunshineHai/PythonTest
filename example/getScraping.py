# begining:
'''
1.处理兄弟标签
  next_siblings() 函数 和 previous_sibling()函数
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table',{'id':'giftList'}).descendants:  # 与.children()的区别
    print(child)

print('----------------------------------------------------------------------------------')

for sibling in bs.find('table' , {'id' : 'giftList'}).tr.next_siblings:
    print(sibling)

print('---------------分割线------------------------')
print(bs.find('table',{'id' : 'giftList'}).tr)

print('-------------------------------------------')
print(bs.find('img',{'src' : '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
# regex (正则表达式) ： 可识别的字符串
# 正则字符串 ： 任意可以用一系列线性规则构成的字符串。
print('-----------------------------分割线-----------------------------------------')
print(bs.findAll('img'))

import re    # 导入正则表达式的包
images = bs.findAll('img',{'src' : re.compile('\.\.\/img\/gifts\/img.*\.jpg')})   # ../img/gifts/img3.jpg
for img in images :
    print(img['src'])
'''
1. 此处使用正则表达式匹配，得到图片的路径信息
2.感觉正则表达式符号好乱，表达的是啥意思都不直观
3.匹配字符解释：\. : \反斜杠表示转义字符，其实表示 . 的意思
             。 ： 表示匹配任意单子字符（包括符号、数字和空格）
             *  ：匹配 前面的字符、字表达式或括号里的字符至少1次。
'''
print('-------------------------------------------------------')
print(bs.findAll(lambda tag: len(tag.attrs) == 2)) # 找出带有2个属性的所有标签

print(bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?') )
print(bs.find_all('', text='Or maybe he\'s only resting?'))


