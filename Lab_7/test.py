import time
import random

def benchmark_array_addition(n: int) -> float:
    start = time.perf_counter()

    a = [random.randint(0, 100) for _ in range(n)]
    b = [random.randint(0, 100) for _ in range(n)]

    c = [a[i] + b[i] for i in range(n)]

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    sizes = [1_000_000, 10_000_000, 100_000_000]

    for n in sizes:
        elapsed = benchmark_array_addition(n)
        print(f"Размер: {n:>10} элементов | Время: {elapsed:.6f} сек")