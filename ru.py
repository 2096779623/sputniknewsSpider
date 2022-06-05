# -*- encoding: utf-8 -*-
'''
@File    :   ru.py
@Time    :   2022/06/05 13:45:57
@Author  :   2096779623 
@Contact :   admin@utermux.dev
@License :   MIT
'''

from urllib import request
from bs4 import BeautifulSoup
url = "https://sputniknews.cn/russia/"
info = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(info, "html.parser")

def text():
  data = soup.find_all("a", class_="list__title")
  data2 = str(data)
  con = re.findall(r'<a.*? title="(.*?)".*?>.*?</a>', data2, re.S|re.M)
  data3 = str(con)
  r = '[’!"#&\'()*,/;<=>?@[\\]{|}]'
  text = re.sub(r, '\n', data3)
  text = str(text)
  print(text)
def link():
  for link in soup.find_all('a', class_="list__title"):
    link = link.get('href')
    link = str(link)
    link = re.sub('(.*.html)',r'https://sputniknews.cn\1',link)
    print(link)

if __name__ == '__main__':
  text()
  link()
  
'''

                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |# '.
                 / \\|||  :  |||# \
                / _||||| -:- |||||- \
               |   | \\\  -  #/ |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     *******************************************

               佛祖保佑         永无BUG
'''
