import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_series_equal


class BlackBoxTesting(unittest.TestCase):

    def test_add(self):
        s1 = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])

        s3 = pd.Series([2.0, 1.0, 1.0, 1.0, np.nan], index=['a', 'b', 'c', 'd', 'e'])

        assert_series_equal(s1.add(s2, fill_value=0), pd.Series(s3))

    def test_combine(self):
        s1 = pd.Series({'falcon': 330.0, 'eagle': 160.0})
        s2 = pd.Series({'falcon': 345.0, 'eagle': 200.0, 'duck': 30.0})

        s3 = pd.Series({'duck': np.nan, 'eagle': 200.0, 'falcon': 345.0})

        assert_series_equal(s1.combine(s2, max), pd.Series(s3))

    def test_combine_first(self):
        s1 = pd.Series({'falcon': np.nan, 'eagle': 160.0})
        s2 = pd.Series({'eagle': 200.0, 'duck': 30.0})

        s3 = pd.Series({'duck': 30.0, 'eagle': 160.0, 'falcon': np.nan})

        assert_series_equal(s1.combine_first(s2), pd.Series(s3))

    def test_divide(self):
        s1 = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])
        s2 = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])

        s3 = pd.Series([1.0, np.inf, np.inf, 0.0, np.nan], index=['a', 'b', 'c', 'd', 'e'])

        assert_series_equal(s1.divide(s2, fill_value=0), pd.Series(s3))

    def test_append(self):
        s1 = pd.Series([1,2,3])
        s2 = pd.Series([4,5,6])
        s3 = pd.Series([4,5,6], index=[3, 4, 5])
       
        assert_series_equal(s1.append(s2), pd.Series([1,2,3,4,5,6],index=[0,1,2,0,1,2]))

def suite1():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_add'))
    return suite


def suite2():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_combine'))
    return suite


def suite3():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_combine_first'))
    return suite


def suite4():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_divide'))
    return suite


def suite5():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_append'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    print(" ")
    print("     " + "Black Box Testing for add(): " + "        ")
    runner.run(suite1())

    print(" ")
    print("     " + "Black Box Testing for combine(): " + "        ")
    runner.run(suite2())

    print(" ")
    print("     " + "Black Box Testing for combine_first(): " + "        ")
    runner.run(suite3())

    print(" ")
    print("     " + "Black Box Testing for divide(): " + "        ")
    runner.run(suite4())

    print(" ")
    print("     " + "Black Box Testing for append(): " + "        ")
    runner.run(suite5())
