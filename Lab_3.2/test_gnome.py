import unittest
import random
from Akimova_3_gnome import gnomeSort 

class TestGnomeSort(unittest.TestCase):
    def setUp(self):
        self.empty_arr = []
        self.single_element = [42]
        self.sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.reverse_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.duplicates_arr = [5, 1, 5, 2, 5, 1, 3, 2, 5, 5]
        self.random_arr = [random.randint(1, 500) for _ in range(100)]
        self.expected_random_sorted = sorted(self.random_arr)

    def test_all_cases(self):
        # Наш гном модифицирует массив на месте, поэтому проверяем состояние переменной
        arr1 = self.empty_arr.copy()
        gnomeSort(arr1)
        self.assertEqual(arr1, [])

        arr2 = self.single_element.copy()
        gnomeSort(arr2)
        self.assertEqual(arr2, [42])

        arr3 = self.sorted_arr.copy()
        gnomeSort(arr3)
        self.assertEqual(arr3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        arr4 = self.reverse_arr.copy()
        gnomeSort(arr4)
        self.assertEqual(arr4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        arr5 = self.duplicates_arr.copy()
        gnomeSort(arr5)
        self.assertEqual(arr5, [1, 1, 2, 2, 3, 5, 5, 5, 5, 5])

        arr6 = self.random_arr.copy()
        gnomeSort(arr6)
        self.assertEqual(arr6, self.expected_random_sorted)

if __name__ == "__main__":
    unittest.main()