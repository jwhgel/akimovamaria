import ctypes
import os

dll_path = os.path.abspath("DLL1.dll")
lib = ctypes.CDLL(dll_path)

lib.add_int_arrays.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
]
lib.add_int_arrays.restype = None

lib.add_float_arrays.argtypes = [
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
    ctypes.c_int,
]
lib.add_float_arrays.restype = None


a1 = (ctypes.c_int * 5)(1, 2, 3, 4, 5)
a2 = (ctypes.c_int * 5)(10, 20, 30, 40, 50)
res_int = (ctypes.c_int * 5)()

lib.add_int_arrays(a1, a2, res_int, 5)
print("Результат int:", [res_int[i] for i in range(5)])

f1 = (ctypes.c_float * 3)(1.5, 2.5, 3.5)
f2 = (ctypes.c_float * 3)(0.5, 1.5, 2.5)
res_float = (ctypes.c_float * 3)()

lib.add_float_arrays(f1, f2, res_float, 3)
print("Результат float:", [res_float[i] for i in range(3)])