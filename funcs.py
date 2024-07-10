import abc
import contextlib
import string
import random
from random import randint
import re
import time
from abc import ABC, abstractmethod
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

def DZ_10_1_1(event):
  # Реализуйте класс «Автомобиль». Необходимо хранить
  # в полях класса: название модели, год выпуска, произво-
  # дителя, объем двигателя, цвет машины, цену. Реализуйте
  # методы класса для ввода данных, вывода данных, реа-
  # лизуйте доступ к отдельным полям через методы класса.
  class Cars():
    def __init__(self, model, year, brand, engine, color, price):
      self.model = model
      self.year = year
      self.brand = brand
      self.engine = engine
      self.color = color
      self.price = price
    def desc(self):
      print(f"Автомобиль {self.model}, год выпуска {self.year}, производитель {self.brand}, объём двигателя {self.engine} литра, цвет машины {self.color}, цена {self.price}")
  Cars1 = Cars("Vesta", 2017, 'Lada', 1.6, 'White', '900k')
  Cars1.desc()

def DZ_10_1_2(event):
  # Реализуйте класс «Книга». Необходимо хранить в
  # полях класса: название книги, год выпуска, издателя,
  # жанр, автора, цену. Реализуйте методы класса для ввода
  # данных, вывода данных, реализуйте доступ к отдельным
  # полям через методы класса.
  class books():
    def __init__(self, name, year, publisher, genre, autor, price):
      self.name = name
      self.year = year
      self.publisher = publisher
      self.genre = genre
      self.autor = autor
      self.price = price
    def book(self):
      print(f'Книга {self.name} выпущенная в {self.year} году издателем {self.publisher} в жанре {self.genre} написанная автором {self.autor} стоимостью {self.price}')
  book1 = books("Тарас Бульба", 1835, 'Михаилом Погодиным', 'повесть', 'Николай Васильевич Гоголь', '10p')
  book1.book()

  
def DZ_10_1_3(event):
  # Реализуйте класс «Стадион». Необходимо хранить в
  # полях класса: название стадиона, дату открытия, страну,
  # город, вместимость. Реализуйте методы класса для ввода
  # данных, вывода данных, реализуйте доступ к отдельным
  # полям через методы класса.

  class stadiums():
    def __init__(self, name, date, country, city, capacity):
      self.name = name
      self.date = date
      self.country = country
      self.city = city
      self.capacity = capacity
    def stadium(self):
      print(f'Стадион {self.name} построенный в {self.date} году в {self.country} городе {self.city} вместимостью {self.capacity} человек')
  stadium1 = stadiums("Строитель", 1963, 'России', 'Тольятти', 15000)
  stadium1.stadium()

def DZ_10_5_2(event):
    # Создайте класс Complex (комплексное число).
    # Создайте перегруженные операторы для реализации
    # арифметических операций для по работе с комплексными
    # числами (операции +, -, *, /).

  class Complex:
    def __init__(self, real, imag):
      self.real = real
      self.imag = imag
    def __repr__(self):
      return str(self.real) + ('+' if self.imag>=0 else '') + str(self.imag) + 'i'
    def __add__(self, other):
      return Complex(self.real + other.real,self.imag + other.imag)
    def __sub__(self,other):
      return Complex(self.real - other.real,self.imag - other.imag)
    def __mul__(self,other):
      return Complex(self.real * other.real + self.imag * other.imag * -1, self.real*other.imag+self.imag*other.real)
    def __truediv__(self,other):
      z3 = Complex(other.real, -other.imag)
      delitel = (z3*other).real
      z4 = z3*self
      return Complex(z4.real/delitel , z4.imag/delitel)
    
  z1 = Complex(-4,2)
  z2 = Complex(1,-3)
  print(z1,'\n',z2)
  print('сумма = ',z1+z2)
  print('разность = ',z1-z2)
  print('умножение = ',z1*z2)
  print('деление = ',z1/z2)

def DZ_10_декораторы_1(event):
  # Создайте функцию, возвращающую список со всеми
  # простыми числами от 0 до 1000
  # Используя механизм декораторов посчитайте сколько
  # секунд, потребовалось для вычисления всех простых чисел.
  # Отобразите на экран количество секунд и простые числа.
  start_time = time.time()
  def prime(x):
    for i in range(2,x):
      if x % i == 0:
        return False
      return True
  primeNum = [] 
  for number in range(0,1000):
    if prime(number ):
      primeNum.append(number)    
  end_time = time.time()
  print(primeNum)
  print('заняло времени:', end_time - start_time)


def DZ_10_декораторы_2(event):
  start_time = time.time()
  def prime(x):
    for i in range(2,x):
      if x % i == 0:
        return False
      return True

  primeNum = []
  a = int(input('введите начало диапазона: ')) 
  b = int(input('введите конец диапазона: ')) 
  if a<b:
    for number in range(a,b):
      if prime(number ):
        primeNum.append(number)

    end_time = time.time()
    print(primeNum)
    print('time:', end_time - start_time)
  else:
    print('не верный диапазон') 

def DZ_12_1_1(event):
  # Создайте реализацию паттерна Builder. Протестируйте
  # работу созданного класса.
  class Pasta:
    def __init__(self, settings):
      self.base = settings['base']
      self.sauce = settings['соус']
      self.ham = settings['ветчина']
      self.cheese = settings['сыр']
      self.pepper = settings['перец']
      self.chicken = settings['курица']
      self.fish = settings['рыба']
      self.pork = settings['свинина'] 
      self.beef = settings['говядина']

  class PastaBuilder:
    settings = {
    'base': 1,
    'соус': 0,
    'ветчина': 0,
    'сыр': 0,
    'перец': 0,
    'курица': 0,
    'рыба': 0,
    'свинина': 0,
    'говядина': 0,
    }
      
    def addBase(self):
      self.settings['base'] += 1
      return self
    
    def addSauce(self):
      self.settings['соус'] += 1
      return self
    
    def addHam(self):
      self.settings['ветчина'] += 1
      return self
    
    def addCheese(self):
      self.settings['сыр'] += 1
      return self
    
    def addPepper(self):
      self.settings['перец'] += 1
      return self
    
    def addChicken(self):
      self.settings['курица'] += 1
      return self
    
    def addFish(self):
      self.settings['рыба'] += 1
      return self
    
    def addPork(self):
      self.settings['свинина'] += 1
      return self
    
    def addBeef(self):
      self.settings['говядина'] += 1
      return self
    
    def build(self):
      return Pasta(self.settings)
  print(PastaBuilder().addCheese().addHam().addHam().addChicken().addPepper().build().__dict__)

def DZ_12_1_2(event):
  # Создайте приложение для приготовления пасты. При-
  # ложение должно уметь создавать минимум три вида па-
  # сты. Классы различной пасты должны иметь следующие
  # методы:
  # ■ Тип пасты;
  # ■ Соус;
  # ■ Начинка;
  # ■ Добавки.
  # Для реализации используйте порождающие паттерны.

  class Pasta:
    def __init__(self, settings):
      self.base = settings['base']
      self.sauce = settings['соус']
      self.ham = settings['ветчина']
      self.cheese = settings['сыр']
      self.pepper = settings['перец']
      self.chicken = settings['курица']
      self.fish = settings['рыба']
      self.pork = settings['свинина'] 
      self.beef = settings['говядина']

  class PastaBuilder:
    settings = {
    'base': 1,
    'соус': 0,
    'ветчина': 0,
    'сыр': 0,
    'перец': 0,
    'курица': 0,
    'рыба': 0,
    'свинина': 0,
    'говядина': 0,
    }
      
    def addBase(self):
      self.settings['base'] += 1
      return self
    
    def addSauce(self):
      self.settings['соус'] += 1
      return self
    
    def addHam(self):
      self.settings['ветчина'] += 1
      return self
    
    def addCheese(self):
      self.settings['сыр'] += 1
      return self
    
    def addPepper(self):
      self.settings['перец'] += 1
      return self
    
    def addChicken(self):
      self.settings['курица'] += 1
      return self
    
    def addFish(self):
      self.settings['рыба'] += 1
      return self
    
    def addPork(self):
      self.settings['свинина'] += 1
      return self
    
    def addBeef(self):
      self.settings['говядина'] += 1
      return self
    
    def build(self):
      return Pasta(self.settings)
  print(PastaBuilder().addCheese().addHam().addHam().addChicken().addPepper().build().__dict__)

def DZ_14_1_1(event):
  # Пользователь вводит с клавиатуры набор чисел. По-
  # лученные числа необходимо сохранить в список (тип
  # списка нужно выбрать в зависимости от поставленной
  # ниже задачи). После чего нужно показать меню, в котором
  # предложить пользователю набор пунктов:
  #   1 Добавить новое число в список (если такое число су-
  # ществует в списке, нужно вывести сообщение поль-
  # зователю об этом, без добавления числа).
  #   2 Удалить все вхождения числа из списка (пользователь
  # вводит с клавиатуры число для удаления).
  #   3 Показать содержимое списка (в зависимости от вы-
  # бора пользователя список нужно показать с начала
  # или с конца).
  #   4 Проверить есть ли значение в списке.
  #   5 Заменить значение в списке (пользователь опреде-
  # ляет заменить ли только первое вхождение или все
  # вхождения).
  # В зависимости от выбора пользователя выполняется
  # действие, после чего меню отображается снова.

  numbers = []
  
  def add_number():
      num = int(input("Введите число: "))
      if num in numbers:
          print("Это число уже есть в списке")
      else:
          numbers.append(num)
          print("Число успешно добавлен")
  
  def remove_number():
      num = int(input("Введите число для удаления: "))
      numbers[:] = [x for x in numbers if x != num]
      print("Все вхождения числа удалены")
  
  
  def show_list():
      direction = input("Введите направление (начало/конец): ")
      if direction == "начало":
          print(numbers)
      elif direction == "конец":
          print(numbers[::-1])
  
  
  def check_value():
      num = int(input("Введите число для проверки: "))
      if num in numbers:
          print("Значение есть в списке")
      else:
          print("Значение отсутствует в списке")
  
  
  def replace_value():
      global numbers
      num = int(input("Введите число для замены: "))
      replace_num = int(input("Введите новое число: "))
      replace_all = input("Заменить все совпадения? (да/нет): ")
      if replace_all == "да":
          numbers = [replace_num if x == num else x for x in numbers]
      else:
          index = numbers.index(num)
          numbers[index] = replace_num
      print("Значение успешно заменено")
  
  
  while True:
      print("Меню:")
      print("1. Добавить новое число в список")
      print("2. Удалить все вхождения числа из списка")
      print("3. Показать содержимое списка")
      print("4. Проверить есть ли значение в списке")
      print("5. Заменить значение в списке")
      print("6. Выход")
  
      choice = input("Выберите пункт меню: ")
  
      if choice == "1":
          add_number()
      elif choice == "2":
          remove_number()
      elif choice == "3":
          show_list()
      elif choice == "4":
          check_value()
      elif choice == "5":
          replace_value()
      elif choice == '6':
          break 
      else:
          print("Некорректный выбор. Попробуйте еще раз.")
  print(numbers)

def DZ_12_1_3(event):

  class Point:
    def __init__(self, x,y):
      self.x = x
      self.y = y
    def clone(self):
      return Point(self.x, self.y)
    # def __repr__(self) -> str:
    #   return f'({self.x},{self.y})'

  class Shape(abc.ABC):
    @abc.abstractmethod
    def clone(self):
      pass
    
  class Rectangle(Shape):
    def __init__(self, p1:Point, p2:Point):
      self.p1 = p1 
      self.p2 = p2
    def clone(self):
      return Rectangle(self.p1.clone(),self.p2.clone())
  
  class Circle(Shape):
    def __init__(self, p:Point, r:float):
      self.p = p 
      self.r = r 
    def clone(self):
      return Circle(self.p.clone(),self.r)
    
  myRect = Rectangle(Point(0,0), Point(5,3))
  myRectClone = myRect.clone()
  print(myRect,myRect.__dict__)
  print(myRectClone,myRectClone.__dict__)
  myRect.p1.x = 90
  print(myRectClone.p1.x)

def DZ_12_2_2(event):
  
  #  Есть класс, предоставляющий доступ к набору чисел.
  # Источником этого набора чисел является некоторый файл. 
  #  С определенной периодичностью данные в файле
  # меняются (надо реализовать механизм обновления).
  #  Приложение должно получать доступ к этим данным и
  # выполнять набор операций над ними (сумма, максимум, минимум и т.д.). 
  #  При каждой попытке доступа к этому
  # набору необходимо вносить запись в лог-файл. При ре-
  # ализации используйте паттерн Proxy (для логгирования)
  # и другие необходимые паттерны.
  
  class NumberSetInterface(ABC):
    @abstractmethod
    def get_number(self):
      pass
  class NumberSet(NumberSetInterface):
    def __init__(self, filename):
      self.filename = open("numbers.txt","a")
      self.numbers = []
      self.filename = filename
      
    def get_sum(self):
      return sum(numbers)
    
    def get_max(self):
      return max(numbers)
    
    def get_min(self):
      return min(numbers)
    
    def get_number(self):
      with open("numbers.txt", 'a') as filename:
        self.numbers = [randint(-100,100) for _ in range(30)]
        filename.write(f"numbers: {self.numbers}\n")
      return self.numbers
    
    def update_numbers(self):
      pass

  class NumberSetProxy(NumberSetInterface):
    def __init__(self, number_set):
      self.number_set = number_set
      self.log_file = open("log.txt", "a")
    
    def _write_to_log(self, message):
      self.log_file.write(message + "\n")
    
    def get_number(self):
      numbers = number_set.get_number()
      with open('log.txt', 'a') as log_file:
        log_file.write(f'Numbers: {numbers}\n')
      return numbers
    
    def get_sum(self):
      result = number_set.get_sum()
      self._write_to_log(f"Sum calculated: {result}")
      return result
    
    def get_max(self):
      result = number_set.get_max()
      self._write_to_log(f"Max number found: {result}")
      return result
    
    def get_min(self):
      result = number_set.get_min()
      self._write_to_log(f"Min number found: {result}")
      return result

  number_set = NumberSet('numbers.txt')
  proxy = NumberSetProxy(number_set)
  numbers = proxy.get_number()
  print(numbers)
  print(proxy.get_sum())
  print(proxy.get_max())
  print(proxy.get_min())

