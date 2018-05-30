import os
from selenium import webdriver



# print(os.path.abspath(__file__),os.path.dirname(os.path.abspath(__file__)))
# rootdir = os.path.dirname(os.path.abspath(__file__))
# print(os.path.join(rootdir,'screenshots'))

import csv
d = webdriver.Chrome()
with open('testdata/userlogin.csv','r') as f:
        
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            d.get("http://www.baidu.com")
            d.find_element_by_id('kw').send_keys(row[0])
            print(row)
    
    