import unittest
import random
from Akimova_3_porazr import radixSort 

class TestRadixSort(unittest.TestCase):
    def setUp(self):
        self.empty_arr = []
        self.single_element = [42]
        self.sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.reverse_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.duplicates_arr = [5, 1, 5, 2, 5, 1, 3, 2, 5, 5]
        self.random_arr = [random.randint(1, 500) for _ in range(100)]
        self.expected_random_sorted = sorted(self.random_arr)

    def test_all_cases(self):
        self.assertEqual(radixSort(self.empty_arr.copy()), [])
        self.assertEqual(radixSort(self.single_element.copy()), [42])
        self.assertEqual(radixSort(self.sorted_arr.copy()), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(radixSort(self.reverse_arr.copy()), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(radixSort(self.duplicates_arr.copy()), [1, 1, 2, 2, 3, 5, 5, 5, 5, 5])

        res = self.random_arr.copy()
        radixSort(res)
        self.assertEqual(res, self.expected_random_sorted)

if __name__ == "__main__":
    unittest.main()