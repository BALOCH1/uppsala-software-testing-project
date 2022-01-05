from logging import error
import pandas as pd
import numpy as np
import unittest
from pandas.testing import assert_frame_equal

""" 
Name:               Henrik Wahlström 
Latest version:     2022-01-05"""

class BlackBoxTesting(unittest.TestCase):
    """docstring fo BlackBoxTesting."""

    def setUp(self):

        #Create dataframes 

        self.dataframe1 = pd.DataFrame({"Name": ["Name1", "Name2", "Name3"], "Age": [1, 2, 3], "Boolean": [True, False, True]})
        self.dataframe2 = pd.DataFrame({})
        self.dataframe3 = pd.DataFrame({"Name": [], "Age": [], "Boolean": []})
        self.dataframe4 = pd.DataFrame({"Data1": [1, 2, 3], "Data2": [1, 2, 3]})
        self.dataframe5 = pd.DataFrame({"Data1": ["One", "Two", "Three"], "Data2": ["1", "2", "3"]})
        self.dataframe6 = pd.DataFrame({"Data1": [1.0, 2.0, 3.0], "Data2": [1.0, 2.0, 3.0]})
        self.dataframe7 = pd.DataFrame({"Name": [np.nan], "Age": [np.nan], "Boolean": [np.nan]})


        #Create series

        self.series1 = pd.Series()
        self.series2 = pd.Series([1, 2, 3, 4], index = ['A', 'B', 'C', 'D'])


        ##--------------count()-------------------
        """
        Brief Description: Counts the values for each column
        Params: - axis
                - level
                - numeric_only


        Input Domain Testing 
        c1 = 0
        c2 = >0
        c3 = invalid count
        
        D1          | D2         | D3
        c1 = True   | c1 = False | c1 = False
        c2 = False  | c2 = True  | c2 = False
                    |            | c3 = True  
        """

    #Test c1

    #Count columns of empty dataframe
    def test_count_empty1(self):
        self.assertEqual(self.dataframe3.count()["Name"], 0) 
        self.assertEqual(self.dataframe3.count()["Age"], 0) 
        self.assertEqual(self.dataframe3.count()["Boolean"], 0) 
    
    #Assert that the empty columns only are equal to 0
    def test_count_empty2(self):
        self.assertNotEqual(self.dataframe3.count()["Name"], 3) 
        self.assertNotEqual(self.dataframe3.count()["Age"], 1) 
        self.assertNotEqual(self.dataframe3.count()["Boolean"], 1000) 

    #Count numeric_only = True for dataframe with no numeric data
    def test_count_empty_numeric_only(self):
        self.assertEqual(self.dataframe7.count(numeric_only = True)[1], 0) 
        

    #Test c2 

    #Count columns of non-empty dataframe
    def test_count_not_empty_column1(self):
        self.assertEqual(self.dataframe1.count()["Name"], 3) 
        self.assertEqual(self.dataframe1.count()["Age"], 3) 
        self.assertEqual(self.dataframe1.count()["Boolean"], 3) 
    
    #Assert that the same columns not are equal to 0
    def test_count_not_empty_column2(self):
        self.assertNotEqual(self.dataframe1.count()["Name"], 0) 
        self.assertNotEqual(self.dataframe1.count()["Age"], 0) 
        self.assertNotEqual(self.dataframe1.count()["Boolean"], 0) 

    #Count row of non-empty dataframe
    def test_count_not_empty_row1(self):
        self.assertEqual(self.dataframe1.count(axis = 1)[0], 3) 
        self.assertEqual(self.dataframe1.count(axis = 1)[1], 3) 
        self.assertEqual(self.dataframe1.count(axis = 1)[2], 3) 
    
    #Assert that the same rows not are equal to 0
    def test_count_not_empty_row2(self):
        self.assertNotEqual(self.dataframe1.count(axis = 1)[0], 0) 
        self.assertNotEqual(self.dataframe1.count(axis = 1)[1], 0) 
        self.assertNotEqual(self.dataframe1.count(axis = 1)[2], 0) 

    #Count columns of non-empty dataframe with numeric_only parameter activated
    def test_count_numeric_only(self):
        #Count only the numeric values, the column "Names" should not be counted
        self.assertEqual(self.dataframe1.count(axis = 1, numeric_only = True)[0], 2) 
        self.assertEqual(self.dataframe1.count(numeric_only = True)[0], 3)


    #Test c3 

    #Try to count an unextisting column
    def test_count_axis_out_of_bounds(self):
        self.assertRaises(ValueError, lambda: self.dataframe1.count(axis = 4))


        ##--------------empty()-------------------
        """
        Brief Description: Checks if the dataframe or series is empty or not
        No params


        Input Domain Testing 
        c1 = True
        c2 = False
        
        D1          | D2         
        c1 = True   | c1 = False 
        c2 = False  | c2 = True  
    
        """

    #Test c1

    #dataframe without any labels
    def test_empty_df_true1(self):
        self.assertEqual(self.dataframe2.empty, True) 

    #dataframe with labels, still empty columns
    def test_empty_df_true2(self):
        self.assertEqual(self.dataframe3.empty, True) 

    # serie without index
    def test_empty_serie_true(self):
        self.assertEqual(self.series1.empty, True) 


    #Test c2

    #dataframe with different types
    def test_empty_df_false1(self):
        self.assertEqual(self.dataframe1.empty, False) 

    #dataframe with only Na values
    def test_empty_df_false2(self):
        self.assertEqual(self.dataframe7.empty, False)     

    #serie with values
    def test_empty_serie_false(self):
        self.assertEqual(self.series2.empty, False) 



    ##--------------loc()-------------------
        """
        Brief Description: Access specific part of dataframe or series
        Inputs: - Single label
                - List or array
                - Slice object
                - Boolean array
                - Allignable boolean series
                - Allignable index
                - Callable function


        Input Domain Testing 
        c1 = specific row/rows
        c2 = specific column/columns
        c3 = all columns and rows
        c4 = invalid loc

        
        D1          | D2         | D3         | D4
        c1 = True   | c1 = True  | c1 = False | c1 = False
        c2 = False  | c2 = True  | c2 = False | c2 = False
        c3 = False  | c3 = False | c3 = True  | c3 = False
                                                c4 = True
        """
    
    # Test c1

    #Select the first row of dataframe
    def test_loc_select_first_row(self):
        dataframe = self.dataframe1.loc[[0]]
        assert_frame_equal(dataframe, pd.DataFrame({"Name": ["Name1"], "Age": [1], "Boolean": [True]}))

    #Select the first two rows of dataframe 
    def test_loc_select_first_two_rows(self):
        dataframe = self.dataframe1.loc[[0,1]]
        assert_frame_equal(dataframe, pd.DataFrame({"Name": ["Name1", "Name2"], "Age": [1, 2], "Boolean": [True, False]}))

    #Select row one and three of dataframe
    def test_loc_select_first_and_thrid_row(self):
        dataframe = self.dataframe1.loc[[True, False, True]]
        assert_frame_equal(dataframe, pd.DataFrame({"Name": ["Name1", "Name3"], "Age": [1,3], "Boolean": [True, True]}, index=[0,2]))


    #Test c2 

    #Select value given row and column
    def test_loc_row_and_column1(self):
        self.assertEqual(self.dataframe1.loc[1, "Age"], 2)

    #Select value given row and column
    def test_loc_row_and_column2(self):
        self.assertEqual(self.dataframe1.loc[2, "Name"], "Name3")


    #Test c3

    #Select all rows of dataframe
    def test_loc_select_all_rows1(self):
        dataframe = self.dataframe1.loc[[0,1,2]]
        assert_frame_equal(dataframe, self.dataframe1)
    
    #Select all rows of dataframe
    def test_loc_select_all_rows2(self):
        dataframe = self.dataframe1.loc[[True, True, True]]
        assert_frame_equal(dataframe, self.dataframe1)


    #Test c4

    #Select row out of index
    def test_loc_unexisting_row(self):
        self.assertRaises(KeyError, lambda: self.dataframe1.loc[[5]])

    #Select column out of index
    def test_loc_unexisting_column(self):
        self.assertRaises(KeyError, lambda: self.dataframe1.loc[[1, "column"]])

    #Select loc with invalid input
    def test_loc_with_input_string(self):
        self.assertRaises(KeyError, lambda: self.dataframe1.loc[["one"]])


    ##--------------iloc()-------------------
        """
        Brief Description: Index based access specific part of dataframe or series
        Inputs: - Integer
                - List or array of integers
                - Slice object with integers
                - Boolean array
                - Callable function
        

        Input Domain Testing 
        c1 = specific row
        c2 = specific column
        c3 = all columns and rows
        c4 = invalid iloc

        
        D1          | D2         | D3         | D4
        c1 = True   | c1 = True  | c1 = False | c1 = False
        c2 = False  | c2 = True  | c2 = False | c2 = False
        c3 = False  | c3 = False | c3 = True  | c3 = False
                                                c4 = True
        """
    
    #Test c1 

    #Select the first row of dataframe
    def test_iloc_select_first_row(self):
        dataframe = self.dataframe1.iloc[[0]]
        assert_frame_equal(dataframe, pd.DataFrame({"Name": ["Name1"], "Age": [1], "Boolean": [True]}))

    #Select row one and three of dataframe
    def test_iloc_select_first_and_thrid_row(self):
        dataframe = self.dataframe1.iloc[[True, False, True]]
        assert_frame_equal(dataframe, pd.DataFrame({"Name": ["Name1", "Name3"], "Age": [1,3], "Boolean": [True, True]}, index=[0,2]))


    #Test c2 

    #Select value given row and column
    def test_iloc_row_and_column1(self):
        self.assertEqual(self.dataframe1.iloc[1, 2], False)

    #Select value given row and column
    def test_iloc_row_and_column2(self):
        self.assertEqual(self.dataframe1.iloc[2, 0], "Name3")


    #Test c3

    #Select all rows of dataframe
    def test_iloc_select_all_rows1(self):
        dataframe = self.dataframe1.iloc[[0,1,2]]
        assert_frame_equal(dataframe, self.dataframe1)
    
    #Select all rows of dataframe
    def test_iloc_select_all_rows2(self):
        dataframe = self.dataframe1.iloc[[True, True, True]]
        assert_frame_equal(dataframe, self.dataframe1)


    #Test c4 

    #Select row out of index
    def test_iloc_unexisting_row(self):
        self.assertRaises(IndexError, lambda: self.dataframe1.iloc[[5]])

    #Select column out of index
    def test_iloc_unexisting_column(self):
        self.assertRaises(KeyError, lambda: self.dataframe1.loc[1, 4])

    #Select iloc with invalid input
    def test_iloc_with_input_string(self):
        self.assertRaises(ValueError, lambda: self.dataframe1.iloc[["one"]])


        ##--------------size()-------------------
        """
        Brief Description: Checks the size of the dataframe or series. 
        No params

        
        Input Domain Testing 
        c1 = 0
        c2 = >0
        c3 = invalid size
        
        D1          | D2         | D3
        c1 = True   | c1 = False | c1 = False
        c2 = False  | c2 = True  | c2 = False
                    |            | c3 = True  
        """
    
    #Test c1

    #Size of empty dataframe
    def test_size_empty(self):
        self.assertEqual(self.dataframe2.size, 0) 

     #Size of empty column in dataframe
    def test_size_empty_column(self):
        self.assertEqual(self.dataframe3["Name"].size, 0)

    #Size of empty serie
    def test_size_empty_serie(self):
        self.assertEqual(self.series1.size, 0) 


    #Test c2 

    #Size of non-empty dataframe
    def test_size_not_empty(self):
        self.assertEqual(self.dataframe1.size, 9) 

    #Size of non-empty column in dataframe
    def test_size_not_empty_column(self):
        self.assertEqual(self.dataframe1["Name"].size, 3) 

    #Size of non-empty serie
    def test_size_not_empty_serie(self):
        self.assertEqual(self.series2.size, 4)


    #Test c3 

    #test size()
    def test_size_function(self):
        self.assertRaises(TypeError, lambda: self.dataframe3.size()) 

    #Test size of column
    def test_size_column_invalid1(self):
        self.assertRaises(IndexError, lambda: self.dataframe1.size["Name"]) 

    #Test size of column
    def test_size_column_invalid2(self):
        self.assertRaises(KeyError, lambda: self.dataframe2["Name"].size) 

    
def suite1():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_count_empty1'))
    suite.addTest(BlackBoxTesting('test_count_empty2'))
    suite.addTest(BlackBoxTesting('test_count_empty_numeric_only'))
    suite.addTest(BlackBoxTesting('test_count_not_empty_column1'))
    suite.addTest(BlackBoxTesting('test_count_not_empty_column2'))
    suite.addTest(BlackBoxTesting('test_count_not_empty_row1'))
    suite.addTest(BlackBoxTesting('test_count_not_empty_row2'))
    suite.addTest(BlackBoxTesting('test_count_numeric_only'))
    suite.addTest(BlackBoxTesting('test_count_axis_out_of_bounds'))

    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_empty_df_true1'))
    suite.addTest(BlackBoxTesting('test_empty_df_true2'))
    suite.addTest(BlackBoxTesting('test_empty_serie_true'))
    suite.addTest(BlackBoxTesting('test_empty_df_false1'))
    suite.addTest(BlackBoxTesting('test_empty_df_false2'))
    suite.addTest(BlackBoxTesting('test_empty_serie_false'))

    return suite

def suite3():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_loc_select_first_row'))
    suite.addTest(BlackBoxTesting('test_loc_select_first_two_rows'))
    suite.addTest(BlackBoxTesting('test_loc_select_first_and_thrid_row'))
    suite.addTest(BlackBoxTesting('test_loc_row_and_column1'))
    suite.addTest(BlackBoxTesting('test_loc_row_and_column2'))
    suite.addTest(BlackBoxTesting('test_loc_select_all_rows1'))
    suite.addTest(BlackBoxTesting('test_loc_select_all_rows2'))
    suite.addTest(BlackBoxTesting('test_loc_unexisting_row'))
    suite.addTest(BlackBoxTesting('test_loc_unexisting_column'))
    suite.addTest(BlackBoxTesting('test_loc_with_input_string'))

    return suite

def suite4():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_iloc_select_first_row'))
    suite.addTest(BlackBoxTesting('test_iloc_select_first_and_thrid_row'))
    suite.addTest(BlackBoxTesting('test_iloc_row_and_column1'))
    suite.addTest(BlackBoxTesting('test_iloc_row_and_column2'))
    suite.addTest(BlackBoxTesting('test_iloc_select_all_rows1'))
    suite.addTest(BlackBoxTesting('test_iloc_select_all_rows2'))
    suite.addTest(BlackBoxTesting('test_iloc_unexisting_row'))
    suite.addTest(BlackBoxTesting('test_iloc_unexisting_column'))
    suite.addTest(BlackBoxTesting('test_iloc_with_input_string'))

    return suite

def suite5():
    suite = unittest.TestSuite()
    suite.addTest(BlackBoxTesting('test_size_empty'))
    suite.addTest(BlackBoxTesting('test_size_empty_column'))
    suite.addTest(BlackBoxTesting('test_size_empty_serie'))
    suite.addTest(BlackBoxTesting('test_size_not_empty'))
    suite.addTest(BlackBoxTesting('test_size_not_empty_column'))
    suite.addTest(BlackBoxTesting('test_size_not_empty_serie'))
    suite.addTest(BlackBoxTesting('test_size_function'))
    suite.addTest(BlackBoxTesting('test_size_column_invalid1'))
    suite.addTest(BlackBoxTesting('test_size_column_invalid2'))
    
    return suite

    

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    print("")
    print("----------Blackbox testing for count() in pandas-------------")
    runner.run(suite1())
    print("")
    print("----------Blackbox testing for empty in pandas:------------")
    runner.run(suite2())
    print("")
    print("----------Blackbox testing for loc() in pandas:------------")
    runner.run(suite3())
    print("")
    print("----------Blackbox testing for iloc() in pandas:------------")
    runner.run(suite4())
    print("")
    print("----------Blackbox testing for size in pandas:------------")
    runner.run(suite5())

    