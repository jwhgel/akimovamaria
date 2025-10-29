def calculateSum(c):
    k = 0
    for i in range(len(c)):
        k+=int(c[i])
    return k
def findArrayWithMinSum(a,b):
    sumA = calculateSum(a)
    sumB = calculateSum(b)
    if sumA<sumB:
        print(f'Сумма элементов массива A: {sumA}')
        print(*a)
        print(f'Сумма элементов массива B: {sumB}')
        print(*b)
    else:
        print(f'Сумма элементов массива B: {sumB}')
        print(*b)
        print(f'Сумма элементов массива A: {sumA}')
        print(*a)
    return ''
a = input().split()
b = input().split()
print(findArrayWithMinSum(a,b))