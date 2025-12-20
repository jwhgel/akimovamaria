#include <iostream>
#include <vector>
#include <random>
#include <chrono>

double benchmark_array_addition(std::size_t n) {
    using namespace std;

    // Для честного измерения считаем время с момента начала генерации
    auto start = chrono::high_resolution_clock::now();

    // Генерация данных
    vector<int> a(n);
    vector<int> b(n);
    vector<int> c(n);

    // Генератор случайных чисел
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist(0, 100);

    for (std::size_t i = 0; i < n; ++i) {
        a[i] = dist(gen);
        b[i] = dist(gen);
    }

    // Поэлементное сложение
    for (std::size_t i = 0; i < n; ++i) {
        c[i] = a[i] + b[i];
    }

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    return elapsed.count(); // секунды
}

int main() {
    using namespace std;

    vector<size_t> sizes = {
        1'000'000,      // 1 000 000
        10'000'000,     // 10 000 000
        100'000'000     // 100 000 000
    };

    for (size_t n : sizes) {
        setlocale(LC_ALL, "RU");
        double t = benchmark_array_addition(n);
        cout << "Размер: " << n
            << " элементов | Время: " << t << " сек" << endl;
    }

    return 0;
}
