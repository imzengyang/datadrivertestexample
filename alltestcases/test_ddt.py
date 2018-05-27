

import unittest
from ddt import ddt, data, file_data, unpack

@ddt
class A(unittest.TestCase):

    @data([1, -3, 2, 0],[1, -3, 2, 0])
    def test_a(self,value):
        print("value=======",value)


if __name__ == '__main__':
    unittest.main()