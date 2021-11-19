"""
练习11111111111 
Author:TMH
Date:2021/8/19
"""
import os

import requests
import time
from selenium import webdriver
from  concurrent.futures import ThreadPoolExecutor

os.makedirs('C:/Users/tian/Desktop/王者荣耀壁纸01')
URL="https://pvp.qq.com/web201605/wallpaper.shtml###"
b = webdriver.Chrome()

b.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    }
)
start=time.time()
b.get(URL)
for i in range(25):
    img_list=b.find_elements_by_class_name('sProdImgL7')
    title_list=b.find_elements_by_class_name('p_newhero_item')
    for i in range(len(img_list)):
        a=img_list[i].find_element_by_css_selector('.sProdImgL7>a').get_attribute('href')
        title=title_list[i].find_element_by_css_selector('.p_newhero_item>h4>a').text
        content=requests.get(a).content
        with open(f'C:/Users/tian/Desktop/王者荣耀壁纸01/{title}.png', 'wb') as file:
            file.write(content)

    b.find_element_by_class_name('downpage').click()

end=time.time()
print(f'用时{end-start}秒')