from numpy.core.numeric import NaN
import pandas as pd
import unittest
import numpy as np
from pandas._libs.missing import NA
import pandas._testing as pdt

""" 
Software testing
by: Felix Arnestrand

Testing pandas library functions
    sort_index()
    sort_values()
    groupby()
    fillna()
    query() 
"""

class TestSortIndexMethod(unittest.TestCase):
    # These tests are for testing sort_index, the function is supposed to sort the columns based on the index value.
    # It can handle indices of type int or string. When using strings as indices it should sort alfabethically. 
    # It also provides support for multiIndices.
    #
    # DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last',
    #                       sort_remaining=True, ignore_index=False, key=None)
    #
    '''     Pairwise-testing 
    
            Variables Involved
                1. axis = (0, 1)
                2. level = (None, 0, [0, 1])
                3. ascending = (True, False, [True, False])
                4. inplace = (False, True)
                5. kind = (quicksort, mergesort, heapsort, stable)
                6. na_position = ( 'last', 'first')
                7. sort_remaining = (True, False)
                8. ignore_index = (False, True)
                9. key = (None, func())

            To simplify the testing i will not test the multiIndex functionality. 
            I will also look at only one sorting method to keep the testcases down, as well as not care for the
            inplace parameter because the only thing this does if set to True is modifying the existing dataframe
            instead of you having to set it to a new one.
            This means I will use the variables: axis, ascending(without multiindex option),
            na_position, sort_remaining, ignore_index and key.

            This results in 14 test functions.

            	axis	ascending	na_position	    sort_remaining	ignore_index	key
            1	1	    False	    'last'	        False	        False	        None
            2	1	    True	    'first'	        True	        False	        func
            3	0	    True	    'first'	        False	        False	        None
            4	0	    True	    'last'	        True	        True	        func
            5	0	    False	    'first'	        True	        False	        None
            6	1	    True	    'last'	        True	        True	        func
            7	1	    True	    'first'	        False	        False	        None
            8	1	    False	    'last'	        True	        False	        func
            9	1	    True	    'last'	        False	        True	        None
            10	0	    True	    'first'	        True	        True	        None
            11	0	    True	    'last'	        False	        False	        func
            12	0	    False	    'last'	        True	        True	        None
            13	0	    True	    'first'	        True	        False	        func
            14	0	    False	    'last'	        False	        False	        None


            The variations of functions will be tested on two different DataFrames, one with strings,
            one with integers as indices.
    '''

    def setUp(self):
        self.df1 = pd.DataFrame({'A':[1, 2, NaN, 2], 'B':['red', None, 'red', 'blue']}, 
                                index=('1', 'one', '2', 'two'))
        self.df2 = pd.DataFrame({'A':[1, 3, 4, 2], 'B':['a', 'c', 'd', 'b']}, 
                                index=(1, 3, 4, 2))
        
    def test_sort_index_01_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1.,2., NaN, 2.], 'B':['red', None, 'red', 'blue']}, index=['1', 'one', '2', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='last',
                            sort_remaining=False, ignore_index=False, key=None), answer)
    
    def test_sort_index_01_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 3, 4, 2], 'B':['a', 'c', 'd', 'b']}, index=[1, 3, 4, 2])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='last',
                            sort_remaining=False, ignore_index=False, key=None), answer)
    
    def test_sort_index_02_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1.,2., NaN, 2.], 'B':['red', None, 'red', 'blue']}, index=['1', 'one', '2', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='first',
                            sort_remaining=True, ignore_index=False, key=lambda x: x.str.lower()), answer)
    
    def test_sort_index_02_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 3, 4, 2], 'B':['a', 'c', 'd', 'b']}, index=[1, 3, 4, 2])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='first',
                            sort_remaining=True, ignore_index=False, key=lambda x: x*2), answer)

    def test_sort_index_03_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., NaN, 2., 2.], 'B':['red', 'red', None, 'blue']}, index=['1', '2', 'one', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='first',
                            sort_remaining=False, ignore_index=False, key=None), answer)
    
    def test_sort_index_03_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 2, 3, 4], 'B':['a', 'b', 'c', 'd']}, index=[1, 2, 3, 4])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='first',
                            sort_remaining=False, ignore_index=False, key=None), answer)

    def test_sort_index_04_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., NaN, 2., 2.], 'B':['red', 'red', None, 'blue']}, index=[0, 1, 2, 3])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='last',
                            sort_remaining=True, ignore_index=True, key=lambda x: x*2), answer)
    
    def test_sort_index_04_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 2, 3, 4], 'B':['a', 'b', 'c', 'd']}, index=[0, 1, 2, 3])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='last',
                            sort_remaining=True, ignore_index=True, key=lambda x: x*2), answer)

    def test_sort_index_05_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[2., 2., NaN, 1.], 'B':['blue', None, 'red', 'red']}, index=['two', 'one', '2', '1'])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=False, na_position='first',
                            sort_remaining=True, ignore_index=False, key=None), answer)
    
    def test_sort_index_05_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[4, 3, 2, 1], 'B':['d', 'c', 'b', 'a']}, index=[4,3,2,1])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=False, na_position='first',
                            sort_remaining=True, ignore_index=False, key=None), answer)

    def test_sort_index_06_df1(self):

        test = self.df1
        answer = pd.DataFrame({'A':[1., 2., NaN, 2.], 'B':['red', None, 'red', 'blue']}, index=['1', 'one', '2', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='last',
                            sort_remaining=True, ignore_index=True, key=lambda x: x*2), answer)
    
    def test_sort_index_06_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 3, 4, 2], 'B':['a', 'c', 'd', 'b']}, index=[1, 3, 4, 2])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='last',
                            sort_remaining=True, ignore_index=True, key=lambda x: x*2), answer)

    def test_sort_index_07_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., 2., NaN, 2.], 'B':['red', None, 'red', 'blue']}, index=['1', 'one', '2', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='first',
                            sort_remaining=False, ignore_index=False, key=None), answer)
    
    def test_sort_index_07_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 3, 4, 2], 'B':['a', 'c', 'd', 'b']}, index=[1, 3, 4, 2])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='first',
                            sort_remaining=False, ignore_index=False, key=None), answer)

    def test_sort_index_08_df1(self):
        test = self.df1
        answer = pd.DataFrame({'B':['red', None, 'red', 'blue'],'A':[1., 2., NaN, 2.]}, index=['1', 'one', '2', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=False, na_position='last',
                            sort_remaining=True, ignore_index=False, key=lambda x: x*2), answer)
    
    def test_sort_index_08_df2(self):
        test = self.df2
        answer = pd.DataFrame({'B':['a', 'c', 'd', 'b'], 'A':[1, 3, 4, 2]}, index=[1, 3, 4, 2])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=False, na_position='last',
                            sort_remaining=True, ignore_index=False, key=lambda x: x*2), answer)

    def test_sort_index_09_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., 2., NaN, 2.],'B':['red', None, 'red', 'blue']}, index=['1', 'one', '2', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='last',
                            sort_remaining=False, ignore_index=True, key=None), answer)
    
    def test_sort_index_09_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 3, 4, 2], 'B':['a', 'c', 'd', 'b']}, index=[1, 3, 4, 2])
        pdt.assert_frame_equal(test.sort_index(axis=1, ascending=True, na_position='last',
                            sort_remaining=False, ignore_index=True, key=None), answer)

    def test_sort_index_10_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., NaN, 2., 2.],'B':['red', 'red', None, 'blue']}, index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='first',
                            sort_remaining=True, ignore_index=True, key=None), answer)
    
    def test_sort_index_10_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 2, 3, 4], 'B':['a', 'b', 'c', 'd']}, index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='first',
                            sort_remaining=True, ignore_index=True, key=None), answer)

    def test_sort_index_11_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., NaN, 2., 2.],'B':['red', 'red', None, 'blue']}, index=['1', '2', 'one', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='last',
                            sort_remaining=False, ignore_index=False, key=lambda x: x*2), answer)
    
    def test_sort_index_11_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1, 2, 3, 4], 'B':['a', 'b', 'c', 'd']}, index=[1, 2, 3, 4])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='last',
                            sort_remaining=False, ignore_index=False, key=lambda x: x*2), answer)

    def test_sort_index_12_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[2., 2., NaN, 1.],'B':['blue', None, 'red', 'red']}, index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=False, na_position='last',
                            sort_remaining=True, ignore_index=True, key=None), answer)
    
    def test_sort_index_12_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[4, 3, 2, 1], 'B':['d', 'c', 'b', 'a']}, index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=False, na_position='last',
                            sort_remaining=True, ignore_index=True, key=None), answer)

    def test_sort_index_13_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., NaN, 2., 2.],'B':['red', 'red', None, 'blue']}, index=['1', '2', 'one', 'two'])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='first',
                            sort_remaining=True, ignore_index=False, key=lambda x: x*2), answer)
    
    def test_sort_index_13_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[1,2,3,4], 'B':['a', 'b', 'c', 'd']}, index=[1,2,3,4])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=True, na_position='first',
                            sort_remaining=True, ignore_index=False, key=lambda x: x*2), answer)

    def test_sort_index_14_df1(self):
        test = self.df1
        answer = pd.DataFrame({'A':[2., 2., NaN, 1.],'B':['blue', None, 'red', 'red']}, index=['two', 'one', '2', '1'])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=False, na_position='last',
                            sort_remaining=False, ignore_index=False, key=None), answer)
    
    def test_sort_index_14_df2(self):
        test = self.df2
        answer = pd.DataFrame({'A':[4,3,2,1], 'B':['d', 'c', 'b', 'a']}, index=[4,3,2,1])
        pdt.assert_frame_equal(test.sort_index(axis=0, ascending=False, na_position='last',
                            sort_remaining=False, ignore_index=False, key=None), answer)
    

class TestSortValuesMethod(unittest.TestCase):
    # These tests are for testing sort_values, which is supposed to sort the dataframe by a specified column.
    # It can handle many types of values, eg. int and string.
    #
    # DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last',
    #                       ignore_index=False, key=None)
    #
    '''     Pairwise-testing 
    
            Variables Involved
                1. axis = (0, 1)
                2. ascending = (True, False, [True, False])
                3. inplace = (False, True)
                4. kind = (quicksort, mergesort, heapsort, stable)
                5. na_position = ( 'last', 'first')
                6. ignore_index = (False, True)
                7. key = (None, func())
                8. by

            To simplify the testing i will not test the option to have a list of ascending bools for each column.
            I will also look at only one sorting method to keep the testcases down, as well as not care for the
            inplace parameter because the only thing this does if set to True is modifying the existing dataframe
            instead of you having to set it to a new one. Axis will also only take the value 0, because there is 
            no point in sorting by columns if not looking at MultiIndex, wich we are not in this case.
            This means I will use the variables: by, ascending(without multicolumn option),
            na_position, ignore_index and key.

            This results in 7 test functions when sorting by three columns.

            	ascending	na_position	ignore_index	key	    by
            1.	True	    'first'	    True	        func	B
            2.	True	    'last'	    False	        None	C
            3.	True	    'first'	    True	        func	A
            4.	False	    'first'	    False	        func	A
            5.	False	    'last'	    True	        None	B
            6.	False	    'first'	    False	        func	C
            7.	False	    'last'	    True	        None	A


            The variations of functions will be tested on one DataFrame with three columns of 
            strings, integers and floats which all contain null values of different kind at different places.
    '''

    def setUp(self):
        self.df1 = pd.DataFrame({'A':[NaN, 2, 1,  2], 'B':['red', None, 'red', 'blue'], 'C':[3.3, 4.4, 1.1, NaN]}, 
                                index=[1,2,3,4])
    
    def test_sort_values_01(self):
        test = self.df1
        answer = pd.DataFrame({'A':[2., 2., NaN, 1.], 'B':[None, 'blue', 'red', 'red',], 'C':[4.4, NaN, 3.3, 1.1]},
                             index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_values(by='B', ascending=True, na_position='first',
                            ignore_index=True, key=lambda x: x*2), answer)
    
    def test_sort_values_02(self):
        test = self.df1
        answer = pd.DataFrame({'A':[1., NaN, 2., 2.], 'B':['red', 'red', None, 'blue'], 'C':[1.1, 3.3, 4.4, NaN]},
                             index=[3,1,2,4])
        pdt.assert_frame_equal(test.sort_values(by='C', ascending=True, na_position='last',
                            ignore_index=False, key=None), answer)
    
    def test_sort_values_03(self):
        test = self.df1
        answer = pd.DataFrame({'A':[NaN, 1., 2., 2.], 'B':['red', 'red', None, 'blue'], 'C':[3.3, 1.1, 4.4, NaN]},
                             index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_values(by='A', ascending=True, na_position='first',
                            ignore_index=True, key=lambda x: x*2), answer)
    
    def test_sort_values_04(self):
        test = self.df1
        answer = pd.DataFrame({'A':[NaN, 2., 2., 1.], 'B':['red', None, 'blue', 'red'], 'C':[3.3, 4.4, NaN, 1.1]},
                             index=[1,2,4,3])
        pdt.assert_frame_equal(test.sort_values(by='A', ascending=False, na_position='first',
                            ignore_index=False, key=lambda x: x*2), answer)

    def test_sort_values_05(self):
        test = self.df1
        answer = pd.DataFrame({'A':[NaN, 1., 2., 2.], 'B':['red', 'red', 'blue', None], 'C':[3.3, 1.1, NaN, 4.4]},
                             index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_values(by='B', ascending=False, na_position='last',
                            ignore_index=True, key=None), answer)

    def test_sort_values_06(self):
        test = self.df1
        answer = pd.DataFrame({'A':[2., 2.,NaN, 1.], 'B':['blue', None, 'red', 'red'], 'C':[NaN, 4.4, 3.3, 1.1]},
                             index=[4,2,1,3])
        pdt.assert_frame_equal(test.sort_values(by='C', ascending=False, na_position='first',
                            ignore_index=False, key=lambda x: x*2), answer)
    
    def test_sort_values_07(self):
        test = self.df1
        answer = pd.DataFrame({'A':[2., NaN, 1., 2.], 'B':[ None, 'red', 'red', 'blue'], 'C':[4.4, 3.3, 1.1, NaN]},
                             index=[0,1,2,3])
        pdt.assert_frame_equal(test.sort_values(by='C', ascending=False, na_position='last',
                            ignore_index=True, key=None), answer)

class TestGroupByMethod(unittest.TestCase):
    # These tests are for testing groupby, which is supposed to group the columns or rows of a dataframe 
    # by a specified function applied to the values.   

    '''
        These tests have no strategy behind them, only thinking about edge cases and possible problems.
    '''

    def setUp(self):
        self.df1 = pd.DataFrame({'A':[1, 2, 3, 4, 5],'B':[NaN, 7, 8, 9, 10]}, index= [100, 29, 234, 1, 150])

        self.df2 = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                                    'Parrot', 'Parrot'],
                            'Max Speed': [380., 370., 24., 26.]})

    def test_groupby_1(self):
        answer1 = pd.DataFrame({'A':[4, 2, 1, 5, 3],'B':[9., 7., 0., 10., 8.]}, index= [1, 29, 100, 150, 234])
        pdt.assert_frame_equal(self.df1.groupby(level=0).sum(), answer1)
        
    def test_groupby_2(self):
        # See that it groups the same no matter the column, when taking the sum
        answer2 = pd.DataFrame({'A':[4, 2, 1, 5, 3],'B':[9., 7., 0., 10., 8.]}, index= [1, 29, 100, 150, 234])
        pdt.assert_frame_equal(self.df1.groupby(by='A',level=0).sum(), answer2)
    
    def test_groupby_3(self):
        # See that it groups the same no matter the column, when taking the sum
        answer3 = pd.DataFrame({'A':[4, 2, 1, 5, 3],'B':[9., 7., 0., 10., 8.]}, index= [1, 29, 100, 150, 234])
        pdt.assert_frame_equal(self.df1.groupby(by='B',level=0).sum(), answer3)
    
    def test_groupby_4(self):
        answer4 = pd.DataFrame({'A':[4, 2, 1, 5, 3],'B':[9., 7., 0., 10., 8.]}, index= [1, 29, 100, 150, 234])
        pdt.assert_frame_equal(self.df1.groupby(level=0, group_keys=False).sum(), answer4)

    def test_groupby_5(self):
        # See if the .mean() function works together with groupby when applied to the Animals column
        answer = pd.DataFrame({'Max Speed': [375., 25.], 'Animal':['Falcon', 'Parrot']}).set_index('Animal')
        pdt.assert_frame_equal(self.df2.groupby(['Animal']).mean(), answer)

    def test_groupby_6(self):
        # Same as abow but the sum
        answer = pd.DataFrame({'Max Speed': [750., 50.], 'Animal':['Falcon', 'Parrot']}).set_index('Animal')
        pdt.assert_frame_equal(self.df2.groupby(['Animal']).sum(), answer)

class TestFillNaMethod(unittest.TestCase):
    # These tests are for testing fillna, which is supposed to fill all the null values of a dataframe 
    # by a specified value or method.   

    '''
        These tests have no strategy behind them, only thinking about edge cases and possible problems.
    '''

    def setUp(self):
        self.df1 = pd.DataFrame({'A':[1, 2, 3, 4, 5],'B':[NaN, 7, 8, 9, 10]}, index= [100, 29, 234, 1, 150])
        self.df2 = pd.DataFrame({'A':[1, None, NaN, NaN, 5],'B':[NaN, 7, 8, 9, 10]}, index= [100, 29, 234, 1, 150])
        self.df3 = pd.DataFrame({'A':[1, None, NaN, NaN, None],'B':[NaN, 7, 8, 9, 10]})

    def test_fillna_1(self):
        # See if it fills all null values with the value 0.
        answer = pd.DataFrame({'A':[1, 2, 3, 4, 5],'B':[0., 7., 8., 9., 10.]}, index= [100, 29, 234, 1, 150])
        pdt.assert_frame_equal(self.df1.fillna(0), answer)

    def test_fillna_2(self):
        # Same as above just more null values to fill, also different kinds of null syntax None and NaN
        answer = pd.DataFrame({'A':[1., 0., 0., 0., 5],'B':[0., 7., 8., 9., 10.]}, index= [100, 29, 234, 1, 150])
        pdt.assert_frame_equal(self.df2.fillna(0), answer)
    
    def test_fillna_3(self):
        # See if we can replace all null values so they are in the same syntax
        answer = pd.DataFrame({'A':[1., NaN, NaN, NaN, 5],'B':[NaN, 7., 8., 9., 10.]}, index= [100, 29, 234, 1, 150])
        pdt.assert_frame_equal(self.df2.fillna(NaN), answer)

    def test_fillna_4(self):
        # See if a method called 'bfill' is working as intended. It should fill the null values by the 
        # upcoming non-null value. It even works with multiple null in a sequence
        answer = pd.DataFrame({'A':[1., 5., 5., 5., 5],'B':[7, 7., 8., 9., 10.]}, index= [100, 29, 234, 1, 150])
        pdt.assert_frame_equal(self.df2.fillna(method='bfill'), answer)
    
    def test_fillna_5(self):
        # Same as above but taking the value before the null value instead. This time we can see that if 
        # the null value appears before any other value has been detected, it stays as null.
        answer = pd.DataFrame({'A':[1., 1., 1., 1., 5],'B':[NaN, 7., 8., 9., 10.]}, index= [100, 29, 234, 1, 150])
        pdt.assert_frame_equal(self.df2.fillna(method='ffill'), answer)
    
    def test_fillna_6(self):
        # See if it is the same as above for 'bfill'
        answer = pd.DataFrame({'A':[1., None, NaN, NaN, NaN],'B':[7., 7., 8., 9., 10.]})
        pdt.assert_frame_equal(self.df3.fillna(method='bfill'), answer)
    
    def test_fillna_7(self):
        # See if the 'limit' option works. It should only fill in the first n numbers of null values identified
        answer = pd.DataFrame({'A':[1., 1., 1., NaN, NaN],'B':[NaN, 7., 8., 9., 10.]})
        pdt.assert_frame_equal(self.df3.fillna(method='ffill', limit=2), answer)

class TestQueryMethod(unittest.TestCase):
    # These tests are for testing query, which is supposed to return the dataframe queried by a specified 
    # column value or relationship. 

    '''
        These tests have no strategy behind them, only thinking about edge cases and possible problems.
    '''

    def setUp(self):
        self.df1 = pd.DataFrame({'A':[1, 3, 5, 7, 5],'B':[0, 2, 8, 4, 10]}, index= [100, 29, 234, 1, 150])
        self.df2 = pd.DataFrame({'A':[1, 3, 5, 7, 5],'B':[0, 2, 8, 4, 10], 'A + B':[1, 5, 13, 11, 15]})
        self.df3 = pd.DataFrame({'A':['banana', 'apple', 'grape', 'orange', 'kiwi'],'B':[NaN, 7, 8, 9, 10]}, index= [100, 29, 234, 1, 150])

    def test_query_1(self):
        # See if the query to get all rows where the value of A is bigger than B.
        answer1 = pd.DataFrame({'A':[1, 3, 7],'B':[0, 2, 4]}, index= [100, 29, 1])
        pdt.assert_frame_equal(self.df1.query('A > B'), answer1)

    def test_query_2(self):
        # Opposite
        answer2 = pd.DataFrame({'A':[5, 5],'B':[8, 10]}, index= [234, 150])
        pdt.assert_frame_equal(self.df1.query('A < B'), answer2)

    def test_query_3(self):
        # See if a column name including some syntax is a problem
        answer = pd.DataFrame({'A':[1, 3, 5, 7, 5],'B':[0, 2, 8, 4, 10], 'A + B':[1, 5, 13, 11, 15]})
        pdt.assert_frame_equal(self.df2.query('`A + B` == (A + B)'), answer)

    def test_query_4(self):
        # See if checking equal correctly
        answer = pd.DataFrame({'A':[1],'B':[0], 'A + B':[1]})
        pdt.assert_frame_equal(self.df2.query('`A + B` == A'), answer)
    
    def test_query_5(self):
        # See if checking equal correctly
        answer = pd.DataFrame({'A':[],'B':[], 'A + B':[]})
        pdt.assert_frame_equal(self.df2.query('A == B'), answer, check_dtype=False)

    def test_query_6(self):
        # See if the functionality of using defined variables in the query is working, using the @ sign.
        answer = pd.DataFrame({'A':['apple', 'grape'],'B':[7., 8.]}, index= [29, 234])
        maxPrice = 8
        pdt.assert_frame_equal(self.df3.query('B <= @maxPrice'), answer)



def fillnaSuite():
    print('\nTesting fillna function')
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFillNaMethod))
    return suite

def sortIndexSuite():
    print('\nTesting sort_index function')
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSortIndexMethod))
    return suite

def sortValuesSuite():
    print('\nTesting sort_values function')
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSortValuesMethod))
    return suite

def groupbySuite():
    print('\nTesting group_by function')
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGroupByMethod))
    return suite


def querySuite():
    print('\nTesting query function')
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestQueryMethod))
    return suite

def completeSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFillNaMethod))
    suite.addTest(unittest.makeSuite(TestSortIndexMethod))
    suite.addTest(unittest.makeSuite(TestSortValuesMethod))
    suite.addTest(unittest.makeSuite(TestGroupByMethod))
    suite.addTest(unittest.makeSuite(TestQueryMethod))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)

    #runner.run(completeSuite())
    runner.run(fillnaSuite())
    runner.run(groupbySuite())
    runner.run(querySuite())
    runner.run(sortIndexSuite())
    runner.run(sortValuesSuite())
    #unittest.main(verbosity=3)