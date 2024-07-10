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