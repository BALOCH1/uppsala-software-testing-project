import unittest
import pandas as pd
from pandas.testing import assert_series_equal
import pandas.testing as pd_testing
from pandas._testing import assert_frame_equal
import numpy as np


class BlackBoxTesting(unittest.TestCase):
  def test_to_numeric(self):
    s = pd.Series(['1.0', '2', -3])
    s = pd.to_numeric(s)
    assert_series_equal(s, pd.Series([1.0, 2.0, -3.0]))

  def test_str_isupper(self):
    s = pd.Series(['leopard', 'SNAKE', ''])
    s = s.str.isupper()
    assert_series_equal(s, pd.Series([False, True, False]))

  def test_str_contains(self):
    s = pd.Series(['Mouse', 'dog', 'house and parrot', '23'])
    self.assertEqual(s.str.contains('Mouse').any(), True)
    self.assertEqual(s.str.contains('dog').any(), True)
    self.assertEqual(s.str.contains('house and parrot').any(), True)
    self.assertEqual(s.str.contains('23').any(), True)
    self.assertEqual(s.str.contains('not in array').any(), False)
    self.assertEqual(s.str.contains('Mouse').all(), False)

  def test_isnull(self):
    s = pd.Series([5, 'asdf', None])
    assert_series_equal(s.isnull(), pd.Series([False, False, True]))

  def test_notnull(self):
    s = pd.Series([5, 'asdf', None])
    assert_series_equal(s.notnull(), pd.Series([True, True, False]))

def suite1():
  suite = unittest.TestSuite()
  suite.addTest(BlackBoxTesting('test_to_numeric'))
  return suite

def suite2():
  suite = unittest.TestSuite()
  suite.addTest(BlackBoxTesting('test_str_isupper'))
  return suite

def suite3():
  suite = unittest.TestSuite()
  suite.addTest(BlackBoxTesting('test_str_contains'))
  return suite

def suite4():
  suite = unittest.TestSuite()
  suite.addTest(BlackBoxTesting('test_isnull'))
  return suite

def suite5():
  suite = unittest.TestSuite()
  suite.addTest(BlackBoxTesting('test_notnull'))
  return suite

# unittest.main()

if __name__ == '__main__':
  runner = unittest.TextTestRunner(verbosity=3)
  print("")
  print("----------Blackbox testing for to_numeric():-------------")
  runner.run(suite1())
  print("")
  print("----------Blackbox testing for str_isupper():------------")
  runner.run(suite2())
  print("")
  print("----------Blackbox testing for str_contains():------------")
  runner.run(suite3())
  print("")
  print("----------Blackbox testing for isnull():------------")
  runner.run(suite4())
  print("")
  print("----------Blackbox testing for notnull():------------")
  runner.run(suite5())
