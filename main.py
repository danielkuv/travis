import os
import unittest


class Tester(unittest.TestCase):

      def test_success(self):
        self.assertTrue()

      def test_failure(self):
        self.assertFalse()


if __name__ == '__main__':
    unittest.main()
