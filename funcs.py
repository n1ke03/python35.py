import contextlib
# node makehtml.js

with contextlib.suppress(ImportError):
  from pyscript import window
  input = window.prompt
  print = window.alert


def DZ_2_1_1_SumOrMul(event):
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит 
# на экран сумму трёх чисел или произведение трёх чисел
  numsStr = input('3 num split space')
  nums=''
  if numsStr:
    nums = numsStr.split()
  operation = input('operation type (* or +)')
  total = 0

  if operation == '*':
    total = 1

  for n in nums:
    if operation == '+':
      total+=int(n)
    else:
      total*=int(n)
      
  if operation == '+':
    print(f"sum is {total}")
  else:
    print(f"mul is {total}")

