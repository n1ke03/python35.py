import contextlib
import string
import random
import re

def nod(a, b):
  if (b == 0):
    return a
  else:
    return nod(b, a % b)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(nod(a, b))