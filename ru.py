from urllib import request#从urllib导入request模块(获取网页源码)
from bs4 import BeautifulSoup#从bs4导入BeautifulSoup模块(提取数据)
import re#导入re模块(正则表达式)
url = "https://sputniknews.cn/russia/"#设置url变量
info = request.urlopen(url).read().decode('utf-8')#获取网页源码并以UTF-8解析
soup = BeautifulSoup(info, "html.parser")#使用BeautifulSoup解析网页源码
data = soup.find_all("a", class_="list__title")#查找a标签中带有指定class标签的源码
data2 = str(data)#转换为字符串类型
con = re.findall(r'<a.*? title="(.*?)".*?>.*?</a>', data2, re.S|re.M)#使用正则表达式过滤title
data3 = str(con)#转换为字符串类型
r = '[’!"#&\'()*,/;<=>?@[\\]{|}]'#设置表达式变量
con1 = re.sub(r, '\n', data3)#使用正则表达式过滤标点符号并替换成换行符
print(con1)#输出结果
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