import random
import time

def combineBuckets(buckets):
    combinedArray = []
    for bucket in buckets:
        combinedArray.extend(bucket)
    return combinedArray

def sortByDigit(arr, digitPlace):
    buckets = [[] for _ in range(10)]

    for num in arr:
        bucketIndex = (num // digitPlace) % 10
        buckets[bucketIndex].append(num)
    arr[:] = combineBuckets(buckets)

def radixSort(arr):
    if not arr:
        return arr
        
    maxVal = max(arr)
    digitPlace = 1
    
    while maxVal // digitPlace > 0:
        sortByDigit(arr, digitPlace)
        digitPlace *= 10
        
    return arr

if __name__ == "__main__":
    N = 1000000
    RANGE = 100

    print("Generating array...")
    arr = [random.randint(1, RANGE) for _ in range(N)]

    print("Original array (first 20 elements):")
    print(" ".join(map(str, arr[:20])))

    start_time = time.perf_counter()

    radixSort(arr)

    end_time = time.perf_counter()
    duration_ms = int((end_time - start_time) * 1000)

    print("Sorted array (FIRST 20 elements):")
    print(" ".join(map(str, arr[:20])))

    print(f"Time taken by radixSort: {duration_ms} milliseconds")