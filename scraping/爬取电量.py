
# 使用 urllib 和 BeautifulSoup 库实现
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

# 一、获取网址中的HTML源代码存储为python list对象
requst = urllib.request.Request('http://dianf.whpu.edu.cn/ICBS/MobilePayStandard/html/index.html')
# 二、因网站设置有反爬虫，需要添加请求头
requst.add_header('User-Agent' , 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)') # 添加请求头，模仿人使用浏览器访问页面
response = urllib.request.urlopen(requst)
html = response.read()

# 三、使用 BeauSoup() 对象实现对 HTML 页面的解析 ，使用 python 自带的解析方式 ‘html.parser’
bs = BeautifulSoup(html, 'html.parser')
# 四、定位 通知信息所在的 table 标签，使用find_all() 方法，class 类选择器查找
divs = bs.find_all('div', class_= "topWrap")  # {'class' : 'in_list2'}  两种写法
print(divs)

