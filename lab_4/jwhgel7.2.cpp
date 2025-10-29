#include <iostream>
#include <cmath>
#include <set>

void min_from_union_set(std::set<int> A, std::set<int> B) {
    std::set<int> a_b;
    a_b.clear();
    a_b.insert(A.begin(), A.end());
    a_b.insert(B.begin(), B.end());
    std::cout << "The smallest element of a union: " << std::endl;
    std::cout << *a_b.begin();
}


int main() {

    std::set<int> A;
    std::set<int> B;
    int x;

    std::cout << "Enter the elements of the set A(Until the entered value is equal to 0):" << std::endl;
    while (std::cin >> x && x != 0) {
        A.insert(x);
    }

    std::cout << "Enter the elements of the set B(Until the entered value is equal to 0):" << std::endl;
    while (std::cin >> x && x != 0) {
        B.insert(x);
    }

    min_from_union_set(A, B);

    return 0;
}
