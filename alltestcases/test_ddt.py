

import unittest
from ddt import ddt, data, file_data, unpack
import csv

def get_data_csv(filename):
    users = []
    with open(filename,'r') as f:
        
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            users.append(row)
    return users

# get_data_csv()

@ddt
class A(unittest.TestCase):

    @data(*get_data_csv("userlogin.csv"))
    @unpack
    def test_a(self,value1,value2,value3,value4):
        print("value=======",value1)
        print("value=======",value2) 
        print("value=======",value3)
        print("value=======",value4)
        print("=============================")

if __name__ == '__main__':
    unittest.main()