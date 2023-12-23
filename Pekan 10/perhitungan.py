# Module Perhitungan

import math

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def pangkat(a, b):
    return a ** b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol"

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def log(a, base=10):
    return math.log(a, base)

def akar(a):
    return math.sqrt(a)

def tan(a):
    return math.tan(math.radians(a))