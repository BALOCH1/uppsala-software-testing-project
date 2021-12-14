import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_series_equal


class BlackBoxTesting(unittest.TestCase):

    def test_upper(self):
        s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])

        assert_series_equal(s.str.upper(), pd.Series(
            ["LOWER", "CAPITALS", "THIS IS A SENTENCE", "SWAPCASE"]))

    def test_isna(self):
        sr = pd.Series([12, 5, None, 5, None, 11])

        assert_series_equal(sr.isna(), pd.Series(
            [False, False, True, False, True, False]))

    def test_lower(self):
        s = pd.Series(['lower', 'CAPITALS', 'this is a SENTENCE', 'SwApCaSe'])
        assert_series_equal(s.str.lower(), pd.Series(
            ["lower", "capitals", "this is a sentence", "swapcase"]))

    def test_notna(self):
        sr = pd.Series([12, 5, None, 5, None, 11])

        assert_series_equal(sr.notna(), pd.Series(
            [True, True, False, True, False, True]))

    def test_unique(self):
        s = pd.Series([2, 1, 1, 3, 3, 4, 5])
        results = pd.Series([2, 1, 3, 4, 5])
        unique_values = pd.unique(s)
        series_values = pd.Series(unique_values)
        assert_series_equal(series_values, results)


def suite1():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_upper'))
    return suite


def suite2():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_isna'))
    return suite


def suite3():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_lower'))
    return suite


def suite4():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_notna'))
    return suite


def suite5():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_unique'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    print(" ")
    print("     " + "Black Box Testing for upper(): " + "        ")
    runner.run(suite1())

    print(" ")
    print("     " + "Black Box Testing for isna(): " + "        ")
    runner.run(suite2())

    print(" ")
    print("     " + "Black Box Testing for lower(): " + "        ")
    runner.run(suite3())

    print(" ")
    print("     " + "Black Box Testing for notna(): " + "        ")
    runner.run(suite4())

    print(" ")
    print("     " + "Black Box Testing for unique(): " + "        ")
    runner.run(suite5())
