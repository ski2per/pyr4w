# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:10:09 2018

@author: admin
"""
'''
def fibo(n):
    f1=1 
    f2=1
    print(f1,'',f2,'', end='')
    for i in range(3,n):
        f3=f2+f1
        print(f3,'',end='')
        f1=f2
        f2=f3
        

fibo(1)
'''
import requests
import pandas
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

response=requests.get('http://haoshu.xshcs.com')
response.encoding='utf-8'
html=response.text
strhtml=BeautifulSoup(html,'lxml')
lists=strhtml.select('[class="title"]')
lists2=strhtml.select('[class="price"]')
lists3=strhtml.select('[class="publisher"]')

df = pandas.DataFrame()
i=0
for fr in lists:
    context = fr.string+ '：'+ lists2[i].string.replace('¥','') + '：' + lists3[i].string
    #print(context)
    i=i+1
    tmp = pandas.DataFrame([context.split('：')], columns=["书名", "价格", "出版社"])
    df = df.append(tmp, ignore_index=True)

print(df)
#df.to_csv('new_book.csv', encoding='gbk', index=False)

# 通过出版社名来分组，计算每个出版社出书数量
new_df = df.groupby("出版社").size().to_frame("count")

# 加载中文字体
font = fm.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")
# 创建空白图片
fig , ax = plt.subplots()
# 创建饼图，设置显示格式，并获取饼图上的文本
_, texts, autotexts = ax.pie(new_df['count'], labels=new_df.index, autopct='%.2f')
# 设置图片宽高
fig.set_figheight(10)
fig.set_figwidth(10)

# 设置饼图文本的字体为中文, 防止中文乱码
plt.setp(autotexts, fontproperties=font)
plt.setp(texts, fontproperties=font)

# 设置图表标题
plt.title("各出版社出版书籍比例", fontproperties=font)
plt.show()
# plt.savefig("image.jpg")



'''
with open('book.txt','w',encoding='utf-8') as f:
    i=0
    for fr in lists:
        context= fr.string+ '：'+ lists2[i].string.replace('¥','')
        i=i+1
        f.write(context)
'''