import os
import unittest


class Tester(unittest.TestCase):

      def test_success(self):
        self.assertTrue(True)

      def test_failure(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
