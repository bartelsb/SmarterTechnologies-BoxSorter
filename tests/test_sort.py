import unittest
from sort import sort

class TestSortClassification(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(10, 20, 30, 5), "STANDARD")

    def test_bulky_width(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    def test_bulky_height(self):
        self.assertEqual(sort(10, 150, 10, 5), "SPECIAL")

    def test_bulky_length(self):
        self.assertEqual(sort(10, 10, 150, 5), "SPECIAL")

    def test_bulky_volume(self):
        # 100 * 100 * 101 = 1,010,000
        self.assertEqual(sort(100, 100, 101, 5), "SPECIAL")

    def test_heavy_only(self):
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")

    def test_bulky_and_heavy(self):
        self.assertEqual(sort(200, 10, 10, 25), "REJECTED")

    def test_boundary_bulky_and_heavy(self):
        # volume == 1,000,000 and mass == 20 should be REJECTED
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort(0, 10, 10, 5)
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 5)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, 0)

if __name__ == "__main__":
    unittest.main()
