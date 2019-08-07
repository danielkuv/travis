import os
import unittest


class Tester(unittest.TestCase):

    def setUp(self):
        print("**************************Testing Travis**************************")

    def test_success(self):
        self.assertTrue(True)

    def test_failure(self):
        self.assertTrue(False)

    def tearDown(self):
        print("**************************Testing Ended**************************")


if __name__ == '__main__':
    unittest.main()
