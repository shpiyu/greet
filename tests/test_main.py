import unittest
from greet.main import greet, get_messages


class MyTestCase(unittest.TestCase):
    def test_greet(self):
        self.assertIn(greet(), get_messages())


if __name__ == '__main__':
    unittest.main()
