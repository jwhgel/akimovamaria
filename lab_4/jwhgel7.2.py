def min_from_union_set(a,b):
    a_b = a | b
    return min(a_b)
inputA = input().split()
setA = set(inputA)
inputB = input().split()
setB = set(inputB)
print(min_from_union_set(setA,setB))
