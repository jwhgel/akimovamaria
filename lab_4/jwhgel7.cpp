#include <iostream>
#include <cmath>

void calculateSum(const int* arr, int size, int& sum) {
    sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
}

void findArrayWithMinSum(const int* arrA, int sizeA, const int* arrB, int sizeB) {
    int sumA = 0, sumB = 0;
    calculateSum(arrA, sizeA, sumA);
    calculateSum(arrB, sizeB, sumB);

    if (sumA < sumB) {
        std::cout << "Array A has the smallest sum: " << sumA << std::endl;
        std::cout << "Elements of array A: ";
        for (int i = 0; i < sizeA; i++) {
            std::cout << arrA[i] << " ";
        }
        std::cout << '\n';
        std::cout << "Array B has the sum: " << sumB << std::endl;
        std::cout << "Elements of array B: ";
        for (int i = 0; i < sizeB; i++) {
            std::cout << arrB[i] << " ";
        }
    }
    else {
        std::cout << "Array B has the smallest sum: " << sumB << std::endl;
        std::cout << "Elements of array B: ";
        for (int i = 0; i < sizeB; i++) {
            std::cout << arrB[i] << " ";
        }
        std::cout << '\n';
        std::cout << "Array A has the sum: " << sumA << std::endl;
        std::cout << "Elements of array A: ";
        for (int i = 0; i < sizeA; i++) {
            std::cout << arrA[i] << " ";
        }
    }
    std::cout << std::endl;
}

int main() {

    int* A = new int[5];
    int* B = new int[4];

    std::cout << "Enter 5 elements for array A:" << std::endl;
    for (int i = 0; i < 5; i++) {
        std::cin >> A[i];
    }

    std::cout << "Enter 4 elements for array B:" << std::endl;
    for (int i = 0; i < 4; i++) {
        std::cin >> B[i];
    }

    findArrayWithMinSum(A, 5, B, 4);


    delete[] A;
    delete[] B;

    return 0;
}