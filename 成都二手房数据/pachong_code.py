"""
KNN01 -

Author 
Date 2021/10/18

"""
import time

import requests
import re
import pandas as pd
data=[]
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
list1=['jinjiang','qingyang','wuhou','gaoxin7','chenghua','jinniu','tianfuxinqu','gaoxinxi1','shuangliu','wenjiang','pidou','longquanyi','xindou','tianfuxinqunanqu','qingbaijiang','doujiangyan','pengzhou','jianyang','xinjin','chongzhou1','dayi','jintang','pujiang','qionglai']
list2=[100,100,100,100,100,100,100,71,100,100,100,100,100,1,89,100,73,80,98,35,6,100,2,1]
for k in range(len(list1)):
    for j in range(list2[k]):
        URL=f'https://cd.lianjia.com/ershoufang/{list1[0]}/pg{j}/'
        resp=requests.get(url=URL,headers=headers)
        time.sleep(0.5)
        area=re.search('<ul class="sellListContent" log-mod="list"><li clas(.*?)</a></h1></div><div class=',resp.text,re.S).group(1)
        a=re.compile('target="_blank">(.*?)</a> </div></div><div class="address"><div class="houseInfo"><span class="houseIcon"></span>(.*?)</div>(.*?)<i> </i><span>(.*?)</span><i>(.*?)<span>(.*?)</span>')
# #         # 0,1,3,5
        conte=a.findall(area)
        for i in conte:
            if  len(eval(str(i[1].split('|')).replace(' ','')))==6:
                data.append((list1[k],i[0],eval(str(i[1].split('|')).replace(' ',''))[0],eval(str(i[1].split('|')).replace(' ',''))[1],eval(str(i[1].split('|')).replace(' ',''))[2],eval(str(i[1].split('|')).replace(' ',''))[3],eval(str(i[1].split('|')).replace(' ',''))[4],'修建年限未知',eval(str(i[1].split('|')).replace(' ',''))[5],f'{i[3]}万',i[5]))
            elif len(eval(str(i[1].split('|')).replace(' ','')))==7:
                data.append((list1[k],i[0], eval(str(i[1].split('|')).replace(' ', ''))[0],
                             eval(str(i[1].split('|')).replace(' ', ''))[1],
                             eval(str(i[1].split('|')).replace(' ', ''))[2],
                             eval(str(i[1].split('|')).replace(' ', ''))[3],
                             eval(str(i[1].split('|')).replace(' ', ''))[4],
                             eval(str(i[1].split('|')).replace(' ', ''))[5],
                             eval(str(i[1].split('|')).replace(' ', ''))[6],f'{i[3]}万',i[5]))


datas=pd.DataFrame(data)
datas.to_excel(r'C:\Users\tian\Desktop\chengdudata.xlsx')
