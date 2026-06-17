import unittest
import random
import sys
from Akimova_3_bistr import quickSort 

# Подстраховка для лимита рекурсии
sys.setrecursionlimit(15000)

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.empty_arr = []
        self.single_element = [42]
        self.sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.reverse_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.duplicates_arr = [5, 1, 5, 2, 5, 1, 3, 2, 5, 5]
        self.random_arr = [random.randint(1, 500) for _ in range(100)]
        self.expected_random_sorted = sorted(self.random_arr)

    def test_all_cases(self):
        arr1 = self.empty_arr.copy()
        quickSort(arr1, 0, len(arr1) - 1)
        self.assertEqual(arr1, [])

        arr2 = self.single_element.copy()
        quickSort(arr2, 0, len(arr2) - 1)
        self.assertEqual(arr2, [42])

        arr3 = self.sorted_arr.copy()
        quickSort(arr3, 0, len(arr3) - 1)
        self.assertEqual(arr3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        arr4 = self.reverse_arr.copy()
        quickSort(arr4, 0, len(arr4) - 1)
        self.assertEqual(arr4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        arr5 = self.duplicates_arr.copy()
        quickSort(arr5, 0, len(arr5) - 1)
        self.assertEqual(arr5, [1, 1, 2, 2, 3, 5, 5, 5, 5, 5])

        arr6 = self.random_arr.copy()
        quickSort(arr6, 0, len(arr6) - 1)
        self.assertEqual(arr6, self.expected_random_sorted)

if __name__ == "__main__":
    unittest.main()