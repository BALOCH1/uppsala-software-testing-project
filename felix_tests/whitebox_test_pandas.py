import pandas as pd
import unittest
import numpy as np
import pandas._testing as pdt

""" 
Software testing, whitebox
by: Felix Arnestrand

Testing pandas library functions
    insert()
"""


class TestInsertMethod(unittest.TestCase):
    '''     insert - Whitebox testing

    DataFrame.insert(loc, column, value, allow_duplicates=False)

    Insert column into DataFrame at specified location.
    Raises a ValueError if `column` is already contained in the DataFrame,
    unless `allow_duplicates` is set to True.
    Parameters
    ----------
    loc : int
        Insertion index. Must verify 0 <= loc <= len(columns).
    column : str, number, or hashable object
        Label of the inserted column.
    value : int, Series, or array-like
    allow_duplicates : bool, optional


CODE: https://github.com/pandas-dev/pandas/blob/v1.3.5/pandas/core/frame.py#L4361-L4419

    if allow_duplicates and not self.flags.allows_duplicate_labels:
            raise ValueError(
                "Cannot specify 'allow_duplicates=True' when "
                "'self.flags.allows_duplicate_labels' is False."
            )
        if not allow_duplicates and column in self.columns:
            # Should this be a different kind of error??
            raise ValueError(f"cannot insert {column}, already exists")
        if not isinstance(loc, int):
            raise TypeError("loc must be int")

        value = self._sanitize_column(value)
        self._mgr.insert(loc, column, value)

    '''

    def setUp(self):
        self.df1 = pd.DataFrame({'A':[1, 2, 3, 4], 'B':['a', 'b', 'c', 'd']})
    
    # if allow_duplicates and not self.flags.allows_duplicate_labels:
    def test_insert_if_allow_duplicates(self):
        test = self.df1
        # Setting the allows_duplicate_labels flag of the DataFrame to False
        test = test.set_flags(allows_duplicate_labels = False)
        with self.assertRaises(ValueError) as cm:
            test.insert(0,'A',[1,2,3,4],allow_duplicates=True)
        self.assertEqual("Cannot specify 'allow_duplicates=True' when 'self.flags.allows_duplicate_labels' is False.",
                         str(cm.exception))

    # if not allow_duplicates and column in self.columns:
    def test_insert_if_not_allow_duplicates(self):
        test = self.df1
        with self.assertRaises(ValueError) as cm:
            test.insert(0,'A',[1,2,3,4],allow_duplicates=False)
        self.assertEqual("cannot insert A, already exists",
                         str(cm.exception))
        
    # if not isinstance(loc, int):
    # see if the location is of type int
    def test_insert_if_loc_not_int(self):
        test = self.df1
        with self.assertRaises(TypeError) as cm:
            test.insert('0','C',[1,2,3,4])
        self.assertEqual("loc must be int",
                         str(cm.exception))

    # If no problem:
    def test_insert_if_no_problem(self):
        test = self.df1
        test.insert(0,'C',[1,2,3,4])
        answer = pd.DataFrame({'C':[1,2,3,4], 'A':[1, 2, 3, 4], 'B':['a', 'b', 'c', 'd']})
        pdt.assert_frame_equal(test, answer)


def InsertTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(TestInsertMethod('test_insert_if_allow_duplicates'))
    suite.addTest(TestInsertMethod('test_insert_if_not_allow_duplicates'))
    suite.addTest(TestInsertMethod('test_insert_if_loc_not_int'))
    suite.addTest(TestInsertMethod('test_insert_if_no_problem'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(InsertTestSuite())