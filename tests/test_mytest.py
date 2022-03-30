#from example_package import add_one
from context import torahtxt
from torahtxt import add_one
import unittest

class TestStringMethods(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

if __name__ == '__main__':
    unittest.main()
