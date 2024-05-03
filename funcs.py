import contextlib
import string
import random
from random import randint
import re
# node makehtml.js

with contextlib.suppress(ImportError):
  from pyscript import window
  input = window.prompt
  print = window.alert


def DZ_5_1_1(event):
  # Задание 1
  # Напишите функцию, которая отображает на экран
  # форматированный текст, указанный ниже:
  # “Don't compare yourself with anyone in this world…
  # if you do so, you are insulting yourself.”
  # Bill Gates

  def text():
      return print(f"“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\nBill Gates")
  text()

def DZ_5_1_2(event):
  # Задание 2
  # Напишите функцию, которая принимает два числа
  # в качестве параметра и отображает все четные числа
  # между ними.

  def num(a,b):
    for i in range(a,b):
      if i%2==0:
        print(i)
  a = int(input())
  b = int(input())
  num(a,b)

def DZ_5_1_3(event):
  # Задание 3
  # Напишите функцию, которая отображает пустой или
  # заполненный квадрат из некоторого символа. Функция
  # принимает в качестве параметров: длину стороны ква-
  # драта, символ и переменную логического типа:
  # ■ если она равна True, квадрат заполненный;
  # ■ если False, квадрат пустой.

  def printSquere(lenght:int, simbol:str, fill:bool)->None:
      l = lenght+2
      s = ''
      for x in range(l):
        for y in range(l):
          if x==0 or x==l-1:
            if y==0:
              s+= ' -'
            elif y==l-1:
              s+= ''
            else:
              s+= '--'
          else:
            if y==0 or y==l-1:
              if y==0:  
                s+= '|'
              if y==l-1:
                s+= ' |'
            else:
              if fill:        
                s+= ' '+simbol
              else:
                s+= '  '
        s+='\n'
      print(s)
    
  l = int(input('Введите сторону квадрата'))
  s = input('Введите символ')
  z = bool(int(input('Закрашивать? (0,1)')))
  printSquere(l, s, z)  


def DZ_5_1_4(event):
  # Задание 4
  # Напишите функцию, которая возвращает минимальное
  # из пяти чисел. Числа передаются в качестве параметров.

  def min_num(a,b,c,d,e):
    return min(a,b,c,d,e)
  print(min_num(1,4,7,-3,2))

def DZ_5_1_5(event):
  # Задание 5
  # Напишите функцию, которая возвращает произве-
  # дение чисел в указанном диапазоне. Границы диапазона
  # передаются в качестве параметров. Если границы диапа-
  # зона перепутаны (например 5 верхняя граница, а 25
  # нижняя граница), их нужно поменять местами.

  def product(a,b):
    if a == b:
      return 'Диапазон введён не верно' 
    if a > b:
      a,b == b,a 
    c=1
    for i in range (a,b+1):
        c *= i
    return c
  print(product(3,5))

  
def DZ_5_1_6(event):
  # Задание 6
  # Напишите функцию, которая считает количество
  # цифр в числе. Число передаётся в качестве параметра. Из
  # функции нужно вернуть полученное количество цифр.
  # Например, если передали 3456, количество цифр будет 4

  def m5_func_c1_t6(num):
    num_str = str(num)
    return len(num_str)
  print(m5_func_c1_t6(45365))

def DZ_5_1_7(event):
  # Задание 7
  # Напишите функцию, которая проверяет является ли
  # число палиндромом. Число передаётся в качестве параметра.
  # Если число палиндром нужно вернуть из функции
  # true, иначе false.
  # «Палиндром» — это число, у которого первая часть
  # цифр равна второй перевернутой части цифр. Например,
  # 123321 — палиндром (первая часть 123, вторая 321, которая
  # после переворота становится 123), 546645 — палиндром,
  # а 421987 — не палиндром.

  def palindrom(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
      return True
    else:
      return False
  print(palindrom(1233))


def DZ_5_2_1(event):
  # Напишите функцию, вычисляющую произведение
  # элементов списка целых. Список передаётся в качестве па-
  # раметра. Полученный результат возвращается из функции.
  def m5_c2_1(list):
    res = 1
    for i in(list):
      res *= i
    return res
  print(m5_c2_1([2,1,3,6]))


def DZ_5_2_2(event):
  # Напишите функцию для нахождения минимума в
  # списке целых. Список передаётся в качестве параметра.
  # Полученный результат возвращается из функции.
  def m5_c2_2(list):
    return min(list)
  print(m5_c2_2([-6,2,6,4,-123]))

def DZ_5_2_5(event):
  # Напишите функцию, которая получает два списка в
  # качестве параметра и возвращает список, содержащий
  # элементы обоих списков.
  def listSum(list1, list2):
    new_list = list1+list2
    return new_list
  print(listSum([1,2,3,4],[5,6,7,8,9]))

def DZ_5_2_6(event):
# Напишите функцию, высчитывающую степень каждого
# элемента списка целых. Значение для степени передаётся
# в качестве параметра, список тоже передаётся в качестве
# параметра. Функция возвращает новый список, содержа-
# щий полученные результаты.
  def listUp(list,n):
    new_list = []
    for i in (list):
      res=i**n
      new_list.append(res)
    return new_list
  print(listUp([2,3,4], 2))

def DZ_5_3_1(event):
  # Написать рекурсивную функцию нахождения наи-
  # большего общего делителя двух целых чисел.
  def nod(a, b):
    if (b == 0):
      return a
    else:
      return nod(b, a % b)
  a = int(input('Введите первое число: '))
  b = int(input('Введите второе число: '))
  print(nod(a, b))

def DZ_5_3_2(event):
  # Написать игру «Быки и коровы».
  # Программа «загадывает» четырёхзначное число и играющий должен угадать его.
  # После ввода пользователем числа программа
  # сообщает, сколько цифр числа угадано (быки) и сколько
  # цифр угадано и стоит на нужном месте (коровы).
  # После отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток.
  # В программе необходимо использовать рекурсию.
  num = ''.join(random.sample(string.digits, 4))
  count = 0
  print(num)
  def recurcive(num, count):
    count+=1
    userNum = input('Угадай число: ')
    cows = 0
    bulls = 0
    newUserNum = ''
    for n in userNum:
      if n not in newUserNum:
        newUserNum += n
    for n in newUserNum:
      if (n in num):
        bulls+=1
    for i in range(4):
      if num[i]==userNum[i]:
        cows+=1
    if userNum != num:
      print('Bulls: '+str(bulls)+'. Cows: '+ str(cows))
      recurcive(num, count)
    else:
      print('Congrats! I\'s takes ' + str(count) + ' trys')
  recurcive(num, count)

def DZ_7_1_3(event):
  # Написать программу, реализующую сортировку списка
  # методом усовершенствованной сортировки пузырьковым
  # методом. Усовершенствование состоит в том, чтобы ана-
  # лизировать количество перестановок на каждом шагу, если
  # это количество равно нулю, то продолжать сортировку
  # нет смысла — список отсортирован.
  def buble(list):
    list = []
    for i in range(12):
      list.append(randint(-10,10))
    swapped = True
    numStartFromBegin = 0
    numSwapped = 0
    while swapped: 
      numStartFromBegin += 1
      swapped = False 
      for i in range(len(list) - 1):
        if list[i] > list[i + 1]: 
          numSwapped += 1
          swapped = True 
          list[i], list[i + 1] = list[i + 1], list[i] 
    print(list, numStartFromBegin, numSwapped, len(list))

  buble(list)

def DZ_7_3_1(event):
  # Есть четыре списка целых. Необходимо их объединить
  # в пятом списке. Полученный результат в зависимости от
  # выбора пользователя отсортировать по убыванию или
  # возрастанию. Найти значение, введенное пользователем,
  # с использованием линейного поиска.
  def дз7_3_1():
    list1 = [randint(-20, 20) for i in range(5)]
    list2 = [randint(-20, 20) for i in range(5)]
    list3 = [randint(-20, 20) for i in range(5)]
    list4 = [randint(-20, 20) for i in range(5)]
    list5 = list1 + list2 + list3 + list4
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    listSort = int(input('Если хотетите отсортировать по возрастания, то введите 1, если по убыванию, то 0:\n'))
    if listSort == 1:
      list5 == list5.sort(reverse=False)
    elif listSort == 0:
      list5 == list5.sort(reverse=True)
    print(list5)
    def linear_Search(list5, n, key): 
    # Searching list1 sequentially 
      for i in range(0, n): 
          if (list5[i] == key): 
              return i 
      return -1
    key = int(input('Введите искомое число:\n'))
    n = len(list5)
    res = linear_Search(list5,n,key)
    if (res==-1):
      print('Element not found')
    else:
      print('Element found at index: ', res)
  дз7_3_1()

def PZ_5_1_1(event):
#  Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
# Steve Jobs
  def text():
      return print(f'“Don\'t let the noise of others\' opinions\ndrown out your own inner voice.”\n\t\t\tSteve Jobs')
  text()


def PZ_5_1_2(event):
  # Напишите функцию, которая принимает два числа
  # в качестве параметра и отображает все нечетные числа
  # между ними.
  def num(a,b):
    for i in range(a,b):
      if i %3==0:
        print(i)
  a = int(input('Введите целое число:\n'))
  b = int(input('Введите целое число:\n'))
  num(a,b)

def PZ_5_1_4(event):
  # Напишите функцию, которая возвращает макси-
  # мальное из четырёх чисел. Числа передаются в качестве
  # параметров.
  def max_num(a,b,c,d):
      return max(a,b,c,d)
  print(max_num(1,4,7,-3))

def PZ_5_1_5(event):
  # Напишите функцию, которая возвращает сумму чисел
  # в указанном диапазоне. Границы диапазона передаются
  # в качестве параметров.
  def sumNum(a,b):
    sum = 0
    for i in range(a,b):
      sum+=i
      print(sum)
  a = int(input('введите начало диапазона'))
  b = int(input('введите конец диапазона'))
  sumNum(a,b)

def PZ_5_1_6(event):
  # Напишите функцию, которая проверяет является ли
  # число простым. Число передаётся в качестве параметра.
  # Если число простое нужно вернуть из метода true, иначе
  # false.
  def isPrime(n):
    if n <= 1:
      return False
    for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
      return True
  n = int(input('Введите число\n'))  
  print(isPrime(n))

def PZ_5_1_7(event):
  # Напишите функцию, которая проверяет является
  # ли шестизначное число «счастливым». Число передаётся
  # в качестве параметра. Если число счастливое нужно
  # вернуть из функции true, иначе false.
  # «Счастливое шестизначное число» — это число у ко-
  # торого сумма первых трёх цифр равна сумме трёх вторых
  # цифр.
  def happyNum(num):
    if len(num) != 6:
      print("Ошибка! Введите шестизначное число.")
    else:
      digits = [int(digit) for digit in num]
      sum1 = digits[0] + digits[1] + digits[2]
      sum2 = digits[3] + digits[4] + digits[5]
      if sum1 == sum2:
        return True
      else:
        return False
  num = int(input("Введите шестизначное число: "))
  happyNum(num)

def PZ_5_3_1(event):
  # Написать рекурсивную функцию нахождения степени числа.
  def power(num,x):
    if x == 1:
      return num
    else:
      return num ** x
  num = int(input('введите число\n'))
  x = int(input('введите степень\n'))
  print(power(num,x))

def PZ_7_1_1(event):
  #   Написать программу, выполняющую сортировку
  # списка целых чисел методом пузырьковой сортировки.
  myList = [randint(-10,10) for i in range(20)]
  def bubble(myList):
    print(myList)
    swapped = True 
    numStartFromBegin = 0
    numSwapped = 0
    while swapped: 
      numStartFromBegin += 1
      swapped = False 
      for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]: 
          numSwapped += 1
          swapped = True 
          myList[i], myList[i + 1] = myList[i + 1], myList[i]
    print(myList)
  bubble(myList)

def PZ_7_1_2(event):
  #   Написать программу, выполняющую сортировку
  # списка целых чисел методом вставок.
  def insertion_sort(array):
    print(array)
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array
  print(insertion_sort([randint(-10,10) for i in range(20)]))

def PZ_7_2_1(event):
  # Написать программу, выполняющую сортировку
  # списка целых чисел методом Шелла.
  def shell(list):
      list = [randint(-10,10) for i in range(20)]
      n = len(list)
      d = n // 2
      while d > 0:
          for i in range(d, n):
              j = i
              t = list[i]
              while j >= d and list[j - d] > t:
                  list[j] = list[j - d]
                  j -= d
              list[j] = t
          d //= 2
      return list
  print(shell(list))

def PZ_7_2_2(event):
  # Написать программу, выполняющую сортировку
  # списка целых чисел методом пирамидальной сортировки.
  def heapify(nums, heap_size, root_index):  
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
      largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
      largest = right_child
    if largest != root_index:
      nums[root_index], nums[largest] = nums[largest], nums[root_index]
      heapify(nums, heap_size, largest)
  def heap_sort(nums):  
      n = len(nums)
      for i in range(n, -1, -1):
          heapify(nums, n, i)
      for i in range(n - 1, 0, -1):
          nums[i], nums[0] = nums[0], nums[i]
          heapify(nums, i, 0)
  random_list_of_nums = [randint(-20,20)for i in range(20)]
  print(random_list_of_nums)
  heap_sort(random_list_of_nums)  
  print(random_list_of_nums)

def PZ_7_2_3(event):
  # Написать программу, выполняющую сортировку
  # списка целых чисел методом быстрой сортировки.
  def quicksort(nums):
    if len(nums) <= 1:
      return nums
    else:
      q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)

  random_list_of_nums = [randint(-20,20)for i in range(20)]  
  quicksort(random_list_of_nums)  
  print(random_list_of_nums)

def DZ_8_1_1(event):
  # Есть три кортежа целых чисел необходимо найти
  # элементы, которые есть во всех кортежах.
  nums1 = [randint(0,5)for i in range(5)]
  nums2 = [randint(0,5)for i in range(5)]
  nums3 = [randint(0,5)for i in range(5)]
  num1 = tuple(nums1)
  num2 = tuple(nums2)
  num3 = tuple(nums3)
  print(num1)
  print(num2)
  print(num3)
  res = tuple(set(num1) & set(num2) & set(num3))
  print(res)

def DZ_8_1_2(event):
  # Есть три кортежа целых чисел необходимо найти
  # элементы, которые уникальны для каждого списка.
  nums1 = [randint(-5,5)for i in range(5)]
  nums2 = [randint(-5,5)for i in range(5)]
  nums3 = [randint(-5,5)for i in range(5)]
  num1 = tuple(nums1)
  num2 = tuple(nums2)
  num3 = tuple(nums3)
  nums4 = []
  for item in num1:
    if item not in num2 and item not in num3:
      nums4.append(item)
  num4 = tuple(nums4)
  # print(num1)
  # print(num2)
  # print(num3)
  print(num4)

def DZ_8_1_3(event):
  # Есть три кортежа целых чисел необходимо найти эле-
  # менты, которые есть в каждом из кортежей и находятся
  # в каждом из кортежей на той же позиции.

  num1 = (2, 3, 1, 2, 0)
  num2 = (1, 3, 2, 2, 5)
  num3 = (2, 3, 1, 2, 0)
  num4 = ()
  for i in range(min(len(num1), len(num2), len(num3))): 
      if num1[i] == num2[i] == num3[i]: 
          num4 += (num1[i],)
  print(num1)
  print(num2)
  print(num3)
  print(num4)