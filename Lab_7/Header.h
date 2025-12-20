#pragma once

#ifdef ARRAYLIB_EXPORTS
#define ARRAYLIB_API __declspec(dllexport)
#else
#define ARRAYLIB_API __declspec(dllimport)
#endif

extern "C" {
    ARRAYLIB_API void add_int_arrays(int* array1, int* array2, int* result, int size);

    ARRAYLIB_API void add_float_arrays(float* array1, float* array2, float* result, int size);

    ARRAYLIB_API float benchmark_array_addition(int size);
}
