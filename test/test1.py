from deeplearning.data.dataloader import dataloader
import unittest

class TestStringMethods(unittest.TestCase):
    def test_exist(self):
        self.assertEqual(dataloader, [1,2,3])

if __name__ == '__main__':
    unittest.main()