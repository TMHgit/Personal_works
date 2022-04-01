import os
import warnings

import pandas as pd
from selenium import webdriver
import requests
warnings.filterwarnings("ignore")
temps=[]
b= webdriver.Chrome('chromedriver.exe')
b.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    }
)
URL="https://chobrod.com/car-honda-civic"
b.get(URL)
b.find_element_by_class_name('icon-angle-double-right').click()
end_page=b.find_elements_by_class_name('active')[2].text
print(end_page)
path='C:/Users/tian/Desktop/car_imge/honda/civic'

os.makedirs(path)
for i in range(28,int(end_page)+1):
    print(i)
    url=f"https://chobrod.com/car-honda-civic/p{i}"
    b.get(url)
    for i in  b.find_element_by_class_name('list-product').find_elements_by_class_name('itemlist'):
        try:
            title=i.find_element_by_class_name('photo > a').get_attribute('title')
            print(title)
            if i.find_element_by_class_name('photo > a > img').get_attribute('src') ==None:
                img_addrs1=i.find_element_by_class_name('photo > a > img').get_attribute('data-src')
                print(img_addrs1)
            else:
                img_addrs1=i.find_element_by_class_name('photo > a > img').get_attribute('src')
                print(img_addrs1)
            try:
                i.find_element_by_class_name('info')
            except Exception as e:
                print('没有找到')
            else:
                year=i.find_element_by_class_name('info').find_element_by_class_name('info-inside').find_element_by_class_name('info-group').find_element_by_class_name('tags-group').find_element_by_class_name('mgt_4').text
                print(year)
            temps.append(['honda','civic',year,title])
            contet=requests.get(img_addrs1).content
            with open(f'C:/Users/tian/Desktop/car_imge/honda/civic/{title}.jpg', 'wb') as f:
                f.write(contet)
        except Exception as e:
            pass

pd.DataFrame(temps).to_excel('C:/Users/tian/Desktop/car_data_honda_civic.xlsx',header=['broand','car_series','car_year','car_name'])
    # print(temps)
    # print('结束------------------')
    # break




