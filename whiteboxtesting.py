""" def mode(values, dropna: bool = True) -> Series:
    from pandas import Series
    import pandas.core.indexes.base as ibase

    values = _ensure_arraylike(values)
    original = values

    # categorical is a fast-path
    if is_categorical_dtype(values):
        if isinstance(values, Series):
            # TODO: should we be passing `name` below?
            return Series(values._values.mode(dropna=dropna), name=values.name)
        return values.mode(dropna=dropna)

    if dropna and needs_i8_conversion(values.dtype):
        mask = values.isnull()
        values = values[~mask]

    values, _ = _ensure_data(values)

    npresult = htable.mode(values, dropna=dropna)
    try:
        npresult = np.sort(npresult)
    except TypeError as err:
        warn(f"Unable to sort modes: {err}")

    result = _reconstruct_data(npresult, original.dtype, original)
    # Ensure index is type stable (should always use int index)
    return Series(result, index=ibase.default_index(len(result))) """

import  pandas as pd
import  pandas.testing as pd_testing
from    pandas._testing import assert_frame_equal
from    pandas.testing import assert_series_equal
import  numpy as np
import warnings

import unittest

""" 
Name:               Maria Jan 
Class:              IT4
Latest version:     2021-12-03

Whitebox testing:   count(axis: Axis = 0, level: Level | None = None, numeric_only: bool = False) 
Describtion of mode: 

                    Count non-NA cells for each column or row.
                    The values `None`, `NaN`, `NaT`, and optionally `numpy.inf` (depending
                    on `pandas.options.mode.use_inf_as_na`) are considered NA.
                    Parameters
                    ----------
                    axis : {0 or 'index', 1 or 'columns'}, default 0
                    If 0 or 'index' counts are generated for each column.
                    If 1 or 'columns' counts are generated for each row.
                    level : int or str, optional
                    If the axis is a `MultiIndex` (hierarchical), count along a
                    particular `level`, collapsing into a `DataFrame`.
                    A `str` specifies the level name.
                    numeric_only : bool, default False
                    Include only `float`, `int` or `boolean` data.
                    Returns
                    -------
                    Series or DataFrame
                    For each column/row the number of non-NA/null entries.
                    If `level` is specified returns a `DataFrame`.
                    
Code: link: https://github.com/pandas-dev/pandas/blob/v1.3.4/pandas/core/frame.py#L10125-L10215
                    axis = self._get_axis_number(axis)
                            if level is not None:
                                warnings.warn(
                                    "Using the level keyword in DataFrame and Series aggregations is "
                                    "deprecated and will be removed in a future version. Use groupby "
                                    "instead. df.count(level=1) should use df.groupby(level=1).count().",
                                    FutureWarning,
                                    stacklevel=2,
                                )
                                return self._count_level(level, axis=axis, numeric_only=numeric_only)

                            if numeric_only:
                                frame = self._get_numeric_data()
                            else:
                                frame = self

                            # GH #423
                            if len(frame._get_axis(axis)) == 0:
                                result = self._constructor_sliced(0, index=frame._get_agg_axis(axis))
                            else:
                                if frame._is_mixed_type or frame._mgr.any_extension_types:
                                    # the or any_extension_types is really only hit for single-
                                    # column frames with an extension array
                                    result = notna(frame).sum(axis=axis)
                                else:
                                    # GH13407
                                    series_counts = notna(frame).sum(axis=axis)
                                    counts = series_counts.values
                                    result = self._constructor_sliced(
                                        counts, index=frame._get_agg_axis(axis)
                                    )

                            return result.astype("int64")

"""
class whiteboxtesting(unittest.TestCase):
    def setUp(self): 
        self.df = pd.DataFrame({"Person":["John", "Myla", "Lewis", "John", "Myla"], "Age": [24., np.nan, 21., 33, 26], "Single": [False, True, True, True, False]})
        self.series_numeric_only = pd.Series([4,5],index = ['Age', 'Single'])
        self.series = pd.Series([5,4,5],index = ['Person', 'Age', 'Single'])
        self.series_axis_1 = pd.Series([3,2,3,3,3],index = [0,1,2,3,4])
        self.ser = pd.Series(["a", "b", "c", "a"], dtype="category")
        self.ext_arr = self.ser.array #create an extension array
        self.df_ext_arr =  pd.DataFrame({"cat":[self.ext_arr]})
        self.ser_ext_arr = pd.Series([1],index = [0])

    #if level is not None:
    def test_if_is_categorical_dtype(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            self.df.set_index(["Person", "Single"]).count(level="Single")
            self.assertTrue(len(w) == 1)
            self.assertTrue(issubclass(w[-1].category, FutureWarning))
    
    #if numeric_only==true:
    def test_if_numeric_only_true(self):
        series = self.df.count(numeric_only=True)
        assert_series_equal(series, self.series_numeric_only)
        self.assertEqual(series.dtype, np.dtype(np.int64))
    
    #else numeric only==false:
    def test_if_numeric_only_false(self):
        series = self.df.count(numeric_only=False)
        assert_series_equal(series, self.series)
        self.assertEqual(series.dtype, np.dtype(np.int64))
    
    #if len(frame._get_axis(axis)) == 0:
    def test_if_axis_0(self):
        series = self.df.count(axis=0)
        assert_series_equal(series, self.series)
        self.assertEqual(series.dtype, np.dtype(np.int64))
    
    #else len(frame._get_axis(axis)) == 1:
    #if frame._is_mixed_type or frame._mgr.any_extension_types:
    def test_if_axis_1_if(self):
        series = self.df_ext_arr.count(axis=1)
        assert_series_equal(series, self.ser_ext_arr)
        self.assertEqual(series.dtype, np.dtype(np.int64))

    #else len(frame._get_axis(axis)) == 1:
    #else:
    def test_if_axis_1_else(self):
        series = self.df.count(axis=1)
        assert_series_equal(series, self.series_axis_1)
        self.assertEqual(series.dtype, np.dtype(np.int64))



def suite1():
    suite = unittest.TestSuite()
    suite.addTest(whiteboxtesting('test_if_is_categorical_dtype'))
    suite.addTest(whiteboxtesting('test_if_numeric_only_true'))
    suite.addTest(whiteboxtesting('test_if_numeric_only_false'))
    suite.addTest(whiteboxtesting('test_if_axis_0'))
    suite.addTest(whiteboxtesting('test_if_axis_1_if'))
    suite.addTest(whiteboxtesting('test_if_axis_1_else'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite1())