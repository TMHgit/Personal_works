import json
import random

import pandas as pd
import requests
import warnings
import time
satt=time.time()

warnings.filterwarnings("ignore")

shock_absorber_resut = []
temp=[]
model_id=[]
url = "https://api.pttfitauto.com/merchant/api/get/car/master-data/"
temps=[153561481111,153561481112,153561481213,153561481214,153561481215,153561481216,153561481217,153561481218,153561481219,1535614812110,1535614812111,1535614812112,1535614812113,1535614812114,1535614812115,1535614812116,1535614812117]
Car_model_id=[]
files=[
]
headers = {
  'key': 'Xe4IKQ7aT1QZBncUwCku42mhb4jScf7Y'
}
satt=time.time()
for i in range(len(temps)):
  payload={'key': 'Xe4IKQ7aT1QZBncUwCku42mhb4jScf7Y',
           'car_brand_id': f'{temps[i]}'}
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  jsonobj = json.loads(response.text)
  cont=jsonobj['results']['car_master_data_list']
  for k in cont:
      payload = {'key': 'Xe4IKQ7aT1QZBncUwCku42mhb4jScf7Y',
                 'car_brand_id': f'{temps[i]}',
                 'car_model': f'{k}'}
      response = requests.request("POST", url, headers=headers, data=payload, files=files)
      jsonobjj = json.loads(response.text)

      cont = jsonobjj['results']['car_master_data_list']

      for n in cont:
          # print(temps[i],k,n)
          payload = {'key': 'Xe4IKQ7aT1QZBncUwCku42mhb4jScf7Y',
                     'car_brand_id': f'{temps[i]}',
                     'car_model': f'{k}',
                     'car_variant':f'{n}'}
          response = requests.request("POST", url, headers=headers, data=payload, files=files)

          try:
            jsonobjs = json.loads(response.text)
          except Exception as e:
              pass
          year=jsonobjs['results']['car_master_data_list']
          for l in year:
              URL = f'https://api.pttfitauto.com/applayout/list/?key=Xe4IKQ7aT1QZBncUwCku42mhb4jScf7Y&applayout_id=1543235305401153&limit_per_page=8&page=1&categories=155083586312723&car_master_data_id={l["id"]}&sortby=popular&options={{%22entities%22:[%22name%22,%22brand_id%22,%22brand_name%22,%22desc%22,%22start%22,%22end%22,%22is_new%22,%22left_tag%22]}}'
              hearders = {
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
                  }
              r = requests.get(URL, headers=hearders, verify=False)
              r.encoding = r.apparent_encoding
              jsonobj = json.loads(r.text)
              print(temps[i],l['id'],k,n,jsonobj['results']['shoppening_list'])
              if jsonobj['results']['shoppening_list']!=[]:
                  for idxs in jsonobj['results']['shoppening_list']:
                      name = idxs['name']
                      service_name = idxs['service_name']
                      image = idxs['image']['url']
                      full_price = idxs['full_price']
                      desc = idxs['desc']
                      product_type='micro cam'
                      shock_absorber_resut.append([l['id'],service_name,product_type,name,image,full_price,desc])
                      time.sleep(random.choice([0.1,0.2,0.3]))


shock_absorber_data= pd.DataFrame(shock_absorber_resut, columns=['car_year_id','service_name','product_type','product_name','product_image','price', 'desc'])
shock_absorber_data.to_excel(r'C:\Users\tian\Desktop\micro_cam_data.xlsx')