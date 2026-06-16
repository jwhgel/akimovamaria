import unittest

def top_curve(x):
    return x**2 + 4

def bottom_curve(x):
    return -x**2 - 4

def integrand_f(x):
    return top_curve(x) - bottom_curve(x)

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        n += 1
        
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        integral += 2 * f(a + i * h)
        
    return integral * (h / 3)

class TestSimpsonArea(unittest.TestCase):
    TRUE_AREA = 98.0 / 3.0

    def test_precision_low_n(self):
        calculated = simpson_rule(integrand_f, 3, 4, 2)
        self.assertAlmostEqual(calculated, self.TRUE_AREA, places=7)
        
    def test_precision_medium_n(self):
        calculated = simpson_rule(integrand_f, 3, 4, 20)
        self.assertAlmostEqual(calculated, self.TRUE_AREA, places=7)
        
    def test_precision_high_n(self):
        calculated = simpson_rule(integrand_f, 3, 4, 100)
        self.assertAlmostEqual(calculated, self.TRUE_AREA, places=7)

if __name__ == "__main__":
    print("Таблица испытаний / разбиений:")
    print(f"{'Количество N':<15} | {'Результат вычисления':<25}")
    print("-" * 43)
    
    test_nodes = [2, 4, 10, 20, 50, 100, 1000, 10000]
    for n in test_nodes:
        res = simpson_rule(integrand_f, 3, 4, n)
        print(f"{n:<15} | {res:<25.15f}")
        
    print("\nЗапуск Unit-тестов:")
    unittest.main()
