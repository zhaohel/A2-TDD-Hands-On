import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd("Boba@12"))  # 7 characters

    def test2(self):
        self.assertFalse(check_pwd("Boba@1111112345687890"))  # 21 characters

    def test3(self):
        self.assertFalse(check_pwd("boba@123"))  # contain 1 lowercase characters

if __name__ == '__main__':
    unittest.main()

