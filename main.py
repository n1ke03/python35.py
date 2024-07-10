import contextlib
import string
import random
import operator
import re
import time
from abc import ABC, abstractmethod
from random import randint


class NumberSetInterface(ABC):
  @abstractmethod
  def get_number(self):
    pass
class NumberSet(NumberSetInterface):
  def __init__(self, filename):
    self.filename = filename
    self.numbers = []

  def get_number(self):
    with open(self.filename, 'rt') as file:
      self.numbers = [randint(0,100) for _ in range(10)]
    return self.numbers
  def update_numbers(self):
    pass
class NumberSetProxy(NumberSetInterface):
  def __init__(self, number_set):
    self.number_set = number_set
  def get_number(self):
    numbers = self.number_set.get_number()
    with open('log.txt', 'a') as log_file:
      log_file.write(f'Numbers: {numbers}\n')
    return numbers
number_set = NumberSet('numbers.txt')
proxy = NumberSetProxy(number_set)
numbers = proxy.get_number()
print(numbers)