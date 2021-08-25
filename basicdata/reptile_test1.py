from bs4 import BeautifulSoup
import requests
# pip install beautifulsoup4
if __name__ == "__main__":
     target = 'https://www.cnblogs.com/xuwujing/p/10393111.html'
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html)
     # 缩进格式
     # print(bf.prettify())
     # 获取所有的head标签中的所有内容
     texts = bf.find_all('head')
     print(texts)
     #获取所有的a标签，并遍历打印a标签中的href的值
     for item in bf.find_all("a"):
          print(item.get("href"))

     # 获取所有的a标签，并遍历打印a标签的文本值
     for item in bf.find_all("a"):
          print(item.get_text())
     # 获取title的内容
     texts = bf.find('title')
     print(texts)
