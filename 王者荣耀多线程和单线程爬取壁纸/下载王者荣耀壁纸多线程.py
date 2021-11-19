"""
多线程 -

Author 
Date 2021/10/2

"""
import os

import requests
import time
from selenium import webdriver
from  concurrent.futures import ThreadPoolExecutor

os.makedirs('C:/Users/tian/Desktop/王者荣耀壁纸')
URL="https://pvp.qq.com/web201605/wallpaper.shtml###"
b = webdriver.Chrome()

b.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    }
)
b.get(URL)

def download_img(href, tilte):
    resp = requests.get(href)
    with open(f'C:/Users/tian/De    sktop/王者荣耀壁纸/{tilte}.jpg', 'wb') as file:
        file.write(resp.content)
def main():
    for i in range(25):
        img_list=b.find_elements_by_class_name('sProdImgL7')
        title_list=b.find_elements_by_class_name('p_newhero_item')
        with ThreadPoolExecutor(max_workers=16) as pool:
            for i in range(len(img_list)):
                a=img_list[i].find_element_by_css_selector('.sProdImgL7>a').get_attribute('href')
                title=title_list[i].find_element_by_css_selector('.p_newhero_item>h4>a').text
                pool.submit(download_img,a,title)
        b.find_element_by_class_name('downpage').click()

start=time.time()
main()
end=time.time()
print(f'用时{end-start}秒')