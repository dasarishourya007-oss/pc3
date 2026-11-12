import unittest

class TestApp(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(10 + 20, 30)

if __name__ == "_main_":
    unittest.main()