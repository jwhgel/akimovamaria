#include "pch.h"
#include "Header.h"
#include <cstdlib>  
#include <ctime>    

void add_int_arrays(int* array1, int* array2, int* result, int size) {
    for (int i = 0; i < size; ++i) {
        result[i] = array1[i] + array2[i];
    }
}

void add_float_arrays(float* array1, float* array2, float* result, int size) {
    for (int i = 0; i < size; ++i) {
        result[i] = array1[i] + array2[i];
    }
}

float benchmark_array_addition(int size) {
    clock_t start_time = clock();

    int* array1 = new int[size];
    int* array2 = new int[size];
    int* result = new int[size];

    srand(static_cast<unsigned int>(time(nullptr)));
    for (int i = 0; i < size; ++i) {
        array1[i] = rand() % 1000;
        array2[i] = rand() % 1000;
    }

    add_int_arrays(array1, array2, result, size);

    delete[] array1;
    delete[] array2;
    delete[] result;

    clock_t end_time = clock();
    return static_cast<float>(end_time - start_time) / CLOCKS_PER_SEC;
}
