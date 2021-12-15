import  pandas as pd
import  pandas.testing as pd_testing
from    pandas._testing import assert_frame_equal
from    pandas.testing import assert_series_equal
import  numpy as np

##https://stackoverflow.com/questions/54365191/python3-unittest-setup-and-teardown-for-the-whole-test-suite
### 

""" 
Name:               Maria Jan 
Class:              IT4
Latest version:     2021-12-03
Functions tested: 
                    head()
                    tail()
                    shape
                    dtypes
                    describe
 """

import unittest
class BlackBoxTesting(unittest.TestCase):

    def setUp(self): 

        #--empty--
        self.df_empty = pd.DataFrame({'empty' : []})
        self.series_simple_empty = pd.Series(["float64"],index = ['empty'])

        #--simple_string--
        self.df_simple_string = pd.DataFrame({'animal':['snake', 'bat', 'tiger', 'lion',
                   'fox', 'eagle', 'shark', 'dog', 'deer']})
        self.df_simple_string_ans_5 = pd.DataFrame({'animal':['snake', 'bat', 'tiger', 'lion',
                   'fox']})
        self.df_simple_string_ans_3 = pd.DataFrame({'animal':['snake', 'bat', 'tiger']})
        self.df_simple_string_ans_minus3 = pd.DataFrame({'animal':['snake', 'bat', 'tiger', 'lion',
                   'fox', 'eagle']})
       
        self.df_simple_string_ans_last_5 = self.df_simple_string[4:]
        self.df_simple_string_ans_last_3 = self.df_simple_string[6:]
        self.df_simple_string_ans_without_first_3 = self.df_simple_string[3:]

        self.series_simple_string = pd.Series(["object"],index = ['animal'])
        
        #--simple_numbers--
        self.df_simple_numbers = pd.DataFrame({'numbers':[1,2,3]})
        self.df_simple_numbers_ans = pd.DataFrame({'numbers':[1]})

        self.series_ans_numbers = pd.Series(["int64"],index = ['numbers'])

        #--nan_simple--
        self.df_nan_simple = pd.DataFrame({"Nan":[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]}) 
        self.df_nan_simple_ans_5 = pd.DataFrame({"Nan":[np.nan, np.nan, np.nan, np.nan, np.nan]}) 

        self.series_simple_nan = pd.Series(["float64"],index = ['Nan'])

        #--none_simple--
        self.df_none_simple = pd.DataFrame({"None":[None, None, None, None, None, None, None]}) 
        self.df_none_simple_ans_5 = pd.DataFrame({"None":[None, None, None, None, None]}) 

        self.series_simple_none = pd.Series(["object"],index = ['None'])

        #--none_mixed--
        self.df_none_mixed = pd.DataFrame({"A":[12, 4, 5, None, 1, 2], 
            "B":[7, 2, 54, 3, None, 3], 
            "C":[20, 16, 11, None, 8, 7], 
            "D":[14, 3, 3, 2, 6, 9]}) 
        
        self.df_none_mixed_ans_5 = pd.DataFrame({"A":[12, 4, 5, None, 1], 
            "B":[7, 2, 54, 3, None], 
            "C":[20, 16, 11, None, 8], 
            "D":[14, 3, 3, 2, 6]}) 
        
        self.series_none = pd.Series(["float64", "float64", "float64", "int64"],index = ['A', 'B', 'C', 'D'])

       #-int_float
        self.df_int_float = pd.DataFrame({"A":[12, 4, 5, 2, 1], ##används bara här
            "B":[7, 2, 54, 3, 3.3], 
            "C":[20, 16, 11, 3, 8], 
            "D":[14, 3, 4.5, 2, 6]})

        self.series_mixed_int_float = pd.Series(["int64", "float64", "int64", "float64"],index = ['A', 'B', 'C', 'D'])

        #--mixed--
        self.df_mixed = pd.DataFrame({"A":[12, 4, 5, "a", 1], 
            "B":[7, 2.2, 54, 3, False], 
            "C":[20, 16.2, pd.Timestamp('20190210'), "c", 8], 
            "D":[14.1, pd.Timestamp('20190210'), False, "d", 6]}) 
        
        self.series_mixed = pd.Series(["object", "object", "object", "object"],index = ['A', 'B', 'C', 'D'])

        #--types--
        self.df_types = pd.DataFrame({'float': [2.0],'int': [2],'datetime': [pd.Timestamp('20190210')],'string': ['f1'], 'bool':[False]})
        
        self.series_dfTypes = pd.Series(["float64","int64","datetime64[ns]","object", "bool"],index = ['float','int','datetime','string', 'bool'])

        #--describe--
        self.df_describe = pd.DataFrame({'categorical1': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'categorical2': ['a', 'b', 'c']
                  })
        
        self.df_describe_num_nan = pd.DataFrame({'nan':([np.nan,np.nan,np.nan]),
                   'numeric': [1, 2, 3]
                  })
        
        #--series_mixed_types--
        self.series_mixed_types = pd.Series([2.0, 2 ,pd.Timestamp('20190210'),"object", False],index = ['float','int','datetime','string', 'bool'])
        
        ##series
        self.series_numers = pd.Series([1, 2, 3, 4], index = ['A', 'B', 'C', 'D'])
        self.series_numbers = pd.Series([1, 2, 3])
        self.series_string = pd.Series(['A', 'B', 'C', 'A'])
        self.series_string_all_unique = pd.Series(['D', 'B', 'C', 'A'])

        ##describe series answers
        self.series_desc_int = pd.Series([3.0, 2.0,1.0,1.0,1.5,2.0,2.5,3.0],index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
        self.series_desc_string = pd.Series([4,3,'A', 2],index = ['count', 'unique', 'top', 'freq'])
        self.series_desc_string_all_unique = pd.Series([4,4,'D', 1],index = ['count', 'unique', 'top', 'freq'])

        ##describe datafram answers

        self.df_desc_int = pd.DataFrame({'numeric':[3.0, 2.0,1.0,1.0,1.5,2.0,2.5,3.0]})
        self.df_desc_int = self.df_desc_int.set_axis(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], axis='index', inplace=False)

        self.df_desc_nan_num = pd.DataFrame({'Nan':[0.0, np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]})
        self.df_desc_nan_num = self.df_desc_nan_num.set_axis(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], axis='index', inplace=False)

        self.df_desc_none_cat = pd.DataFrame({'None':[0, 0, np.nan, np.nan]})
        self.df_desc_none_cat = self.df_desc_none_cat.set_axis(['count', 'unique', 'top', 'freq'], axis='index', inplace=False)
        self.df_desc_none_cat['None'] = self.df_desc_none_cat['None'].astype(object)

        self.df_desc_all_non = pd.DataFrame({'nan':[0.0, np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan], 'numeric':[3.0, 2.0,1.0,1.0,1.5,2.0,2.5,3.0]})
        self.df_desc_all_non = self.df_desc_all_non.set_axis(['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], axis='index', inplace=False)

        self.df_desc_cat1 = pd.DataFrame({'categorical1':[3,3,'f',1]})
        self.df_desc_cat1 = self.df_desc_cat1.set_axis(['count', 'unique', 'top', 'freq'], axis='index', inplace=False)

        self.df_desc_cat2 = pd.DataFrame({'categorical2':[3,3,'a',1]})
        self.df_desc_cat2 = self.df_desc_cat2.set_axis(['count', 'unique', 'top', 'freq'], axis='index', inplace=False)

        self.df_desc_all = pd.DataFrame({'categorical1':[3,3,'d',1,np.nan,np.nan,np.nan,np.nan,np.nan, np.nan, np.nan],
            'numeric':[3.0, np.nan, np.nan, np.nan, 2.0,1.0,1.0,1.5,2.0,2.5,3.0], 'categorical2': [3,3,'a',1,np.nan,np.nan,np.nan,np.nan,np.nan, np.nan, np.nan]})
        self.df_desc_all = self.df_desc_all.set_axis(['count', 'unique', 'top', 'freq', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], axis='index', inplace=False)
    
    ##_____________________________________head()_____________________________________
    """
        dataframe dataframe.head(int n = 5)
    brief: returns the first n rows in the dataframe
    param: dataframe, the dataframe on which the function acts on
    param: n, number of rows returned
    return: dataframe containing the rows that were chosen 

    characteristics:
    c1: gives default number of rows
    c2: gives all rows
    C3: gives all rows except the last given rows
    c4: gives no rows
    c5: other  

    Domain input: 
    |----D1----|----D2----|----D3----|----D4---|----D5----|
    | c1=true, | c2=true  | c3=true  | c4=true | c5=true  |
    | c2=false | c1=false | c2=false |         | c1=false |
               | c3=false | c1=false |         | c2=false |
                                               | c3=false |
                                               | c4=false |
                                    
    """
    
    #---D1---
    #test only head() which should give the first five rows since it´s default
    
    #dataframe consiting only one column and strings
    def test_head_equal_default(self):
        df_head = self.df_simple_string.head()
        assert_frame_equal(df_head, self.df_simple_string_ans_5)
    
    #dataframe consiting only one column and stirngs
    def test_head_not_euqal_default(self):
        df_head = self.df_simple_string.head()
        self.assertFalse(df_head['animal'].equals(self.df_simple_string['animal']))
     
    #dataframe consiting only one column and nan:s
    def test_head_nan_default(self):
        df_head = self.df_nan_simple.head()
        assert_frame_equal(df_head, self.df_nan_simple_ans_5)
    
    #dataframe consiting only one column and nan:s
    def test_head_none_default(self):
        df_head = self.df_none_simple.head()
        assert_frame_equal(df_head, self.df_none_simple_ans_5)
    
    #dataframe consisting mulitple coulmns and None:s
    def test_head_multi_col_default(self):
        df_head = self.df_none_mixed.head()
        assert_frame_equal(df_head, self.df_none_mixed_ans_5)
    
    #---D2---
    ##test if head(n) gives the output whole dataframe
    
    #dataframe consiting only one column and strings
    #n = 100 
    def test_head_input_100(self):
        df_head = self.df_simple_string.head(100)
        assert_frame_equal(df_head, self.df_simple_string)
    
    #---D3---
    #test if head(-n) gives the output of everything but the n last rows 
    
    #dataframe consiting only one column and strings
    #n = -3 
    def test_head_input_minus3(self):
        df_head = self.df_simple_string.head(-3)
        assert_frame_equal(df_head, self.df_simple_string_ans_minus3)
    
    #---D4---
    #test if head(n) gives none of the rows
    
    #dataframe consiting only one column and strings
    #n=-100
    def test_head_input_minus100(self):
        df_head = self.df_simple_string.head(-100)
        nr_rows = df_head.shape[0]
        self.assertEqual(nr_rows, 0)
    
    #dataframe consiting only one column and strings
    #n=0
    def test_head_input_0(self):
        df_head = self.df_simple_string.head(0)
        nr_rows = df_head.shape[0]
        self.assertEqual(nr_rows, 0)

    #---D5---
    #testing other parameters for head(n)

    #dataframe consiting only one column and strings
    #n=1
    def test_head_equal_simple_case_numbers(self):
        df_head = self.df_simple_numbers.head(1)
        assert_frame_equal(df_head, self.df_simple_numbers_ans)
    
    #dataframe consiting only one column and strings
    #n=3
    def test_head_input_3(self):
        df_head = self.df_simple_string.head(3)
        assert_frame_equal(df_head, self.df_simple_string_ans_3)

##_____________________________________tail()_____________________________________
    """
    dataframe dataframe.tail(int n = 5)
    brief: returns the last n rows in the dataframe
    param: dataframe, the dataframe on which the function acts on
    param: n, number of rows returned
    return: dataframe containing the rows that were chosen 

    characteristics:
    c1: gives default number of rows
    c2: gives all rows
    C3: gives all rows except the first given rows
    c4: gives no rows
    c5: other  

    Domain input: 
    |----D1----|----D2----|----D3----|----D4---|----D5----|
    | c1=true, | c2=true  | c3=true  | c4=true | c5=true  |
    | c2=false | c1=false | c2=false |         | c1=false |
               | c3=false | c1=false |         | c2=false |
                                               | c3=false |
                                               | c4=false |
                                
    """

    #---D1---
    #test only tail() which should give the first five rows since it´s default

    #dataframe consiting only one column and strings
    def test_tail_equal_simple_case(self):
        df_head = self.df_simple_string.tail()
        assert_frame_equal(df_head, self.df_simple_string_ans_last_5)

    #dataframe consiting only one column and strings
    def test_tail_not_euqal_simple_case(self):
        df_head = self.df_simple_string.tail()
        self.assertFalse(df_head['animal'].equals(self.df_simple_string['animal']))
    
    #---D2---
    #test if tail(n) outputs the whole dataframe
    
    #dataframe consiting only one column and strings
    #n = 100
    def test_tail_input_100(self):
        df_head = self.df_simple_string.tail(100)
        assert_frame_equal(df_head, self.df_simple_string)
    
    #---D3---
    #test if tail(n) gives the output of everything but the n last rows 

    #dataframe consiting only one column and strings
    #n = -3
    def test_tail_input_minus3(self):
        df_head = self.df_simple_string.tail(-3)
        assert_frame_equal(df_head, self.df_simple_string_ans_without_first_3)

    #---D4---
    #test if tail(n) gives a result with zero number of rows
    
    #dataframe consiting only one column and strings
    #n = 0
    def test_tail_input_0(self):
        df_head = self.df_simple_string.tail(0)
        nr_rows = df_head.shape[0]
        self.assertEqual(nr_rows, 0)
    
    #dataframe consiting only one column and strings
    #n = -100
    def test_tail_input_minus100(self):
        df_head = self.df_simple_string.tail(-100)
        nr_rows = df_head.shape[0]
        self.assertEqual(nr_rows, 0)
    
    #---D5---
    #testing other parameters for tail(n)

    #dataframe consiting only one column and strings
    #n = 3
    def test_tail_input_3(self):
        df_head = self.df_simple_string.tail(3)
        assert_frame_equal(df_head, self.df_simple_string_ans_last_3)


###_____________________________________shape_____________________________________
    """
    row,column dataframe.shape
    brief: returns the shape of the dataframe
    param: dataframe, the dataframe on which the function acts on
    return: a tuple consisting of the numbers of rows and number of columns the dataframe has

    characteristics:
    c1: gives the number of rows and columns of a dataframe 
    c2: gives no rows

    Domain input: 
    |----D1----|----D2----|
    | c1=true, | c2=true  | 
    | c2=false | c1=false |      
              
                                
    """

    #---D1---
    #test if shape gives the correct number of rows and columns in a dataframe
    
    #dataframe consiting only one column and strings
    def test_shape_equal_simple_case(self):
        row,column = self.df_simple_string.shape
        self.assertEqual(row, 9)
        self.assertEqual(column, 1)
    
    #dataframe consiting only one column and strings
    def test_shape_not_equal_simple_case(self):
        row,column = self.df_simple_numbers.shape
        self.assertNotEqual(row, 9)
        self.assertNotEqual(column, 2)
    
    #dataframe consiting only one column and nan:s
    def test_shape_nan_dataframe(self):
        row, column = self.df_nan_simple.shape
        self.assertEqual(row, 6)
        self.assertEqual(column, 1)
    
     #dataframe consiting several columns and mixed types
    def test_shape_multiple_columns(self):
        row, column = self.df_types.shape
        self.assertEqual(row, 1)
        self.assertEqual(column, 5)
    
    #---D2---
    
    #dataframe consiting one column and no rows
    def test_shape_empty_dataframe(self):
        row, column = self.df_empty.shape
        self.assertEqual(row, 0)
        self.assertEqual(column, 1)
    
##_____________________________________dtypes_____________________________________
    """
        Series dataframe.dtypes
    brief: gives a Series with the data type of each column. 
    param: dataframe or Series, the dataframe on which the function acts on
    return: Series listing the datatype of each column and finishing with the datatype as a whole

    characteristics:
    c1: gives all the types of each column in a dataframe 
    c2: gives the default type object for columns in a dataframe
    c3: gives the defualt type float_  
    C4: gives the type of a Series

    Domain input: 
    |----D1----|----D2----|----D3----|----D4----|
    | c1=true, | c2=true  | c3=true  | c4=true  |
    | c2=false | c1=false | c1=false |       
    | c3=false | c3=false | c2=false |

    """ 
    #---D1---
    #tests if dtypes returns the types of each column in a dataframe

    #Dataframe cositing multiple columns and types
    def test_dtypes_multiple_types(self):
        dtype_series = self.df_types.dtypes
        assert_series_equal(self.series_dfTypes, dtype_series)
        self.assertEqual(np.dtype(object), dtype_series.dtype)
    
    #dataframe consiting only one column and strings
    def test_dtypes_simple_string(self):
        dtype_series = self.df_simple_string.dtypes
        assert_series_equal(dtype_series, self.series_simple_string)
        self.assertEqual(np.dtype(object), dtype_series.dtype)
    
    #dataframe consiting only one column and int:s
    def test_dtypes_simple_int(self):
        dtype_series = self.df_simple_numbers.dtypes
        assert_series_equal(dtype_series, self.series_ans_numbers)
        self.assertEqual(np.dtype(object), dtype_series.dtype)
    
    #---D2---
    #tests if dtypes returns the default value object
    
    #dataframe consiting only one column and none:s
    def test_dtypes_none_dataframe(self):
        dtype_series = self.df_none_simple.dtypes
        assert_series_equal(dtype_series, self.series_simple_none)
        self.assertEqual(np.dtype(object), dtype_series.dtype)
    
    #Dataframe cositing multiple columns and mulitple types in each column
    def test_dtypes_mixed_dataframe(self):
        dtype_series = self.df_mixed.dtypes
        assert_series_equal(dtype_series, self.series_mixed)
        self.assertEqual(np.dtype(object), dtype_series.dtype)
    #---D3---
    #tests if dtypes returns the default value float_
    
    #dataframe consiting one column and no rows
    def test_dtypes_empty_dataframe(self):
        dtype_series = self.df_empty.dtypes
        assert_series_equal(dtype_series, self.series_simple_empty)
        self.assertEqual(np.dtype(object), dtype_series.dtype)
    
    #dataframe consiting only one column and nan:s
    def test_dtypes_nan_dataframe(self):
        dtype_series = self.df_nan_simple.dtypes
        assert_series_equal(dtype_series, self.series_simple_nan)
        self.assertEqual(np.dtype(object), dtype_series.dtype)

    #---D4---
    #tests if dtypes gives the type of a Series

    #a Series consiting numbers
    def test_dtypes_series_int(self):
        dtype_series = self.series_numers.dtypes
        self.assertEqual(np.dtype(np.int64), dtype_series)
    
    #a Series consisting strings
    def test_dtypes_series_object(self): 
        dtype_series = self.series_mixed.dtypes
        self.assertEqual(np.dtype(object), dtype_series)
    
    #a Series consisting mixed types
    #Can´t mix types in Series
    def test_dtypes_series_mixed(self): 
        try:
            dtype_series = self.series_mixed_types.dtypes
            self.assertFalse(True)
        except: 
            self.assertTrue(True) 

##______________________________describe()___________________________________________
    """
        Series dataframe.describe
    brief: generates descriptive statitics 
    param: dataframe or Series, the dataframe on which the function acts on
    return: Series listing the statistics
            numeric: count, mean, std, min, 25%, 50%, 75%, max, dtype
            categorical: count, unique, top, freq, dtype

    characteristics:
    c1: gives the numeric statistics
    c2: gives the categorical statistics
    C3: gives by default only the numeric statistics in a dataframe
    c4: gives both numeric and categorial statistics in a dataframe
    c5: gives the statistics of only one column
    c6: gives the statistics for all but one column 

    Domain input: 
    |----D1----|----D2----|----D3----|----D4----|----D5----|----D6----|
    | c1=true, | c2=true  | c3=true  | c4=true  | c5=true  | c6=true  |
    | c3=false | c5=false | c1=false | c6=false | c1=false | c1=false |    
    | c5=false | c6=false | C5=false |          | c2=false | c2=false |
    | c6=false            | c6=false |          | c3=false | c3=false |
                                                | c6=false | c5=false |
                                                  
    """
    #---D1---
    def test_describe_series_int(self):
            desc_series = self.series_numbers.describe()
            assert_series_equal(desc_series, self.series_desc_int)
            self.assertEqual(np.dtype(np.float64), desc_series)
    
    def test_describe_nan_num(self):
            desc_df = self.df_nan_simple.describe()
            assert_frame_equal(desc_df, self.df_desc_nan_num)

    #---D2---
    def test_describe_series_string(self):
            desc_series = self.series_string.describe()
            assert_series_equal(desc_series, self.series_desc_string)
            self.assertEqual(np.dtype(object), desc_series)
    
    ##when all are the same, the top will be the first element in the series 
    def test_describe_series_string_all_unique(self):
            desc_series = self.series_string_all_unique.describe()
            assert_series_equal(desc_series, self.series_desc_string_all_unique)
            self.assertEqual(np.dtype(object), desc_series)
    
    def test_describe_none_cat(self):
            desc_df = self.df_none_simple.describe()
            assert_frame_equal(desc_df, self.df_desc_none_cat)
    
    #---D3---
    def test_describe_default(self):
            desc_df = self.df_describe.describe()
            assert_frame_equal(desc_df, self.df_desc_int)
    
    def test_describe_default_nan(self):
            desc_df = self.df_describe_num_nan.describe()
            assert_frame_equal(desc_df, self.df_desc_all_non)
    
    #---D4---
    def test_describe_all(self):
            desc_df = self.df_describe.describe(include='all')
            assert_frame_equal(desc_df, self.df_desc_all)

    def test_describe_all_nan(self):
            desc_df = self.df_describe_num_nan.describe(include='all')
            assert_frame_equal(desc_df, self.df_desc_all_non)
    
    #---D5---

    def test_describe_include_1(self):
        desc_df = self.df_describe.describe(include=[np.number])
        assert_frame_equal(desc_df, self.df_desc_int)
    
    #includes only the last column with objects 
    def test_describe_include_2(self):
        desc_df = self.df_describe.describe(include=[object])
        assert_frame_equal(desc_df, self.df_desc_cat2)
            
def suite1():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_head_equal_default'))
    suite.addTest(BlackBoxTesting('test_head_not_euqal_default'))
    suite.addTest(BlackBoxTesting('test_head_nan_default'))
    suite.addTest(BlackBoxTesting('test_head_none_default'))
    suite.addTest(BlackBoxTesting('test_head_multi_col_default'))
    suite.addTest(BlackBoxTesting('test_head_equal_simple_case_numbers'))
    suite.addTest(BlackBoxTesting('test_head_input_0'))
    suite.addTest(BlackBoxTesting('test_head_input_3'))
    suite.addTest(BlackBoxTesting('test_head_input_minus3'))
    suite.addTest(BlackBoxTesting('test_head_input_100'))
    suite.addTest(BlackBoxTesting('test_head_input_minus100'))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_tail_equal_simple_case'))
    suite.addTest(BlackBoxTesting('test_tail_not_euqal_simple_case'))
    suite.addTest(BlackBoxTesting('test_tail_input_0'))
    suite.addTest(BlackBoxTesting('test_tail_input_3'))
    suite.addTest(BlackBoxTesting('test_tail_input_minus3'))
    suite.addTest(BlackBoxTesting('test_tail_input_100'))
    suite.addTest(BlackBoxTesting('test_tail_input_minus100'))
    return suite

def suite3():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_shape_equal_simple_case'))
    suite.addTest(BlackBoxTesting('test_shape_not_equal_simple_case'))
    suite.addTest(BlackBoxTesting('test_shape_empty_dataframe'))
    suite.addTest(BlackBoxTesting('test_shape_nan_dataframe'))
    suite.addTest(BlackBoxTesting('test_shape_multiple_columns'))
    return suite

def suite4():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_dtypes_multiple_types'))
    suite.addTest(BlackBoxTesting('test_dtypes_simple_string'))
    suite.addTest(BlackBoxTesting('test_dtypes_simple_int'))
    suite.addTest(BlackBoxTesting('test_dtypes_empty_dataframe'))
    suite.addTest(BlackBoxTesting('test_dtypes_nan_dataframe'))
    suite.addTest(BlackBoxTesting('test_dtypes_none_dataframe'))
    suite.addTest(BlackBoxTesting('test_dtypes_mixed_dataframe'))
    suite.addTest(BlackBoxTesting('test_dtypes_series_object'))
    suite.addTest(BlackBoxTesting('test_dtypes_series_int'))
    suite.addTest(BlackBoxTesting('test_dtypes_series_mixed'))
    return suite

def suite5():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_describe_series_int'))
    suite.addTest(BlackBoxTesting('test_describe_nan_num'))
    suite.addTest(BlackBoxTesting('test_describe_none_cat'))
    suite.addTest(BlackBoxTesting('test_describe_series_string'))
    suite.addTest(BlackBoxTesting('test_describe_series_string_all_unique'))
    suite.addTest(BlackBoxTesting('test_describe_default'))
    suite.addTest(BlackBoxTesting('test_describe_default_nan'))
    suite.addTest(BlackBoxTesting('test_describe_all'))
    suite.addTest(BlackBoxTesting('test_describe_all_nan'))
    suite.addTest(BlackBoxTesting('test_describe_include_1'))
    suite.addTest(BlackBoxTesting('test_describe_include_2'))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    print("")
    print("----------Blackbox testing for head() in pandas-------------")
    runner.run(suite1())
    print("")
    print("----------Blackbox testing for tail() in pandas:------------")
    runner.run(suite2())
    print("")
    print("----------Blackbox testing for shape in pandas:------------")
    runner.run(suite3())
    print("")
    print("----------Blackbox testing for dtypes in pandas:------------")
    runner.run(suite4())
    print("")
    print("----------Blackbox testing for describe() in pandas:------------")
    runner.run(suite5())
