import os
import unittest


class Tester(unittest.TestCase):

    def setUp(self):
        pass

    def test_success(self):
        self.assertTrue(True)

    def test_failure(self):
        self.assertTrue(True)

    def tearDown(self):
        pass


if __name__ == '__main__':
    print("Testing Model A!")
    unittest.main()
