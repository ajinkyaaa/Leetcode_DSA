import unittest
print("s")
class TestCal(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2,2)


if __name__ == "__main__":
    unittest.main()