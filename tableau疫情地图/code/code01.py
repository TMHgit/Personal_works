"""
code -

Author 
Date 2021/11/12

"""
import json
import re
import pandas
import pandas as pd
import  requests
from selenium import webdriver

URL="https://ncov.dxy.cn/ncovh5/view/pneumonia"
hearders = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }
resp=requests.get(url=URL,headers=hearders)
resp.encoding = resp.apparent_encoding
# print(resp.text)
getAreaStat = re.search(r'''<script id="getAreaStat">try { window.getAreaStat =(.*?)</script>''', resp.text, re.S).group(1)
# area_ = eval(getAreaStat.replace('}catch(e){}',''))
area_ = getAreaStat.replace('}catch(e){}','')
a=json.loads(area_)
list1=[]
list2=[]
for i in a:
    # print(i['provinceName'],i['currentConfirmedCount'],i['confirmedCount'])
    list1.append((i['provinceName'],i['currentConfirmedCount'],i['confirmedCount'],i['deadCount'],i['curedCount']))
    for j in i['cities']:
        list2.append((i['provinceName'],j['cityName'],j['currentConfirmedCount'],j['confirmedCount'],j['deadCount'],j['curedCount']))
#         print(j['cityName'],j['currentConfirmedCount'],j['confirmedCount'])
b=pd.DataFrame(list2,columns=['省份','城市','现存确诊','累计确诊','死亡','治愈'])
print(b)