import unittest
# Создайте класс, содержащий набор целых чисел.
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

class IntNum:
  def __init__(self, *args):
    self.list = []
    for el in args:
      if isinstance(el, int):
        self.list.append(el)
  def sum(self):
    return sum(self.list)
  def mid(self):
    return sum(self.list)/len(self.list)
  def max(self):
    return max(self.list)
  def min(self):
    return min(self.list)
  
class TestSum(unittest.TestCase):
  def test_list1(self):
    num = IntNum(1,.2,3,.5,6)
    self.assertEqual(num.sum(),10,'Should be 10')
    self.assertEqual(num.mid(),10/3,'Should be 10/3')
    self.assertEqual(num.max(),6,'Should be 6')
    self.assertEqual(num.min(),1,'Should be 1')
if __name__ == '__main__':
  unittest.main()