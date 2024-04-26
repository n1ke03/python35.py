import contextlib
import string
import random
import re
# node makehtml.js

with contextlib.suppress(ImportError):
  from pyscript import window
  input = window.prompt
  print = window.alert


def Дз5_часть1_задание1(event):
  # Задание 1
  # Напишите функцию, которая отображает на экран
  # форматированный текст, указанный ниже:
  # “Don't compare yourself with anyone in this world…
  # if you do so, you are insulting yourself.”
  # Bill Gates

  def text():
      return print(f"“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\nBill Gates")
  text()

def Дз5_часть1_задание2(event):
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

def Дз5_часть1_задание3(event):
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


def Дз5_часть1_задание4(event):
  # Задание 4
  # Напишите функцию, которая возвращает минимальное
  # из пяти чисел. Числа передаются в качестве параметров.

  def min_num(a,b,c,d,e):
    return min(a,b,c,d,e)
  print(min_num(1,4,7,-3,2))

def Дз5_часть1_задание5(event):
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

  
def Дз5_часть1_задание6(event):
  # Задание 6
  # Напишите функцию, которая считает количество
  # цифр в числе. Число передаётся в качестве параметра. Из
  # функции нужно вернуть полученное количество цифр.
  # Например, если передали 3456, количество цифр будет 4

  def m5_func_c1_t6(num):
    num_str = str(num)
    return len(num_str)
  print(m5_func_c1_t6(45365))

def Дз5_часть1_задание7(event):
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


def Дз5_часть2_задание1(event):
  # Напишите функцию, вычисляющую произведение
  # элементов списка целых. Список передаётся в качестве па-
  # раметра. Полученный результат возвращается из функции.
  def m5_c2_1(list):
    res = 1
    for i in(list):
      res *= i
    return res
  print(m5_c2_1([2,1,3,6]))


def Дз5_часть2_задание2(event):
  # Напишите функцию для нахождения минимума в
  # списке целых. Список передаётся в качестве параметра.
  # Полученный результат возвращается из функции.
  def m5_c2_2(list):
    return min(list)
  print(m5_c2_2([-6,2,6,4,-123]))

def Дз5_часть2_задание5(event):
  # Напишите функцию, которая получает два списка в
  # качестве параметра и возвращает список, содержащий
  # элементы обоих списков.
  def listSum(list1, list2):
    new_list = list1+list2
    return new_list
  print(listSum([1,2,3,4],[5,6,7,8,9]))

def Дз5_часть2_задание6(event):
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

def Дз5_часть3_задание1(event):
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

def Дз5_часть3_задание2(event):
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