from logging import error
import pandas as pd
import numpy as np
import unittest
from pandas.testing import assert_frame_equal

""" 
Name:               Henrik Wahlström 
Latest version:     2021-12-15"""

"""Code link: https://github.com/pandas-dev/pandas/blob/v1.3.5/pandas/core/frame.py#L6405-L6529


def value_counts(
        self,
        subset: Sequence[Hashable] | None = None,
        normalize: bool = False,
        sort: bool = True,
        ascending: bool = False,
        dropna: bool = True,
    ):
        
        Return a Series containing counts of unique rows in the DataFrame.
        .. versionadded:: 1.1.0
        Parameters
        ----------
        subset : list-like, optional
            Columns to use when counting unique combinations.
        normalize : bool, default False
            Return proportions rather than frequencies.
        sort : bool, default True
            Sort by frequencies.
        ascending : bool, default False
            Sort in ascending order.
        dropna : bool, default True
            Don’t include counts of rows that contain NA values.
            .. versionadded:: 1.3.0
        Returns
        -------
        Series
        See Also
        --------
        Series.value_counts: Equivalent method on Series.
        Notes
        -----
        The returned Series will have a MultiIndex with one level per input
        column. By default, rows that contain any NA values are omitted from
        the result. By default, the resulting Series will be in descending
        order so that the first element is the most frequently-occurring row.

        if subset is None:
            subset = self.columns.tolist()

        counts = self.groupby(subset, dropna=dropna).grouper.size()

        if sort:
            counts = counts.sort_values(ascending=ascending)
        if normalize:
            counts /= counts.sum()

        # Force MultiIndex for single column
        if len(subset) == 1:
            counts.index = MultiIndex.from_arrays(
                [counts.index], names=[counts.index.name]
            )

        return counts

        """
 

class WhiteBoxTesting(unittest.TestCase):
    """docstring fo WhiteBoxTesting."""

    def setUp(self):
        
        self.dataframe1 = pd.DataFrame({"Name": ["Name1", "Name2", "Name3"], "Age": [1, 2, 3], "Boolean": [True, False, True]})
        self.dataframe2 = pd.DataFrame({"Value": [2, 4, 86, 2, 3, 3, 3, 1, 24, 23, 2, 3, 4, 5, 6, 6]})

    #test if subset is none (This will perform valuecounts on all columns)
    def test_if_subset_is_none(self):
        #When the subset is None we should have one of each value count
        self.assertEqual(self.dataframe1.value_counts()[0],1)
        self.assertEqual(self.dataframe1.value_counts()[1],1)
        self.assertEqual(self.dataframe1.value_counts()[2],1)
        #When the subset is None we should have three different results of the value count
        self.assertEqual(len(self.dataframe1.value_counts()), 3)

    def test_if_sort(self):
        #The number 3 appear four times in the dataframe
        self.assertEqual(self.dataframe2.value_counts(sort = True)[3], 4)
        #The number 3 should be in first place
        self.assertEqual(self.dataframe2.value_counts(sort = True).iloc[1], 3)
        #The number 2 should be in second place
        self.assertEqual(self.dataframe2.value_counts(sort = True).iloc[2], 2)

    def test_if_normalize(self):
        #Total numbers in dataframe: 16
        #Since the number 3 appears four times. The normalized value should be 0.25
        self.assertEqual(self.dataframe2.value_counts(normalize = True)[3], 0.25)
        #Since the number 24 appears one time. The normalized value should be 0.0625
        self.assertEqual(self.dataframe2.value_counts(normalize = True)[24], 0.0625)

    def test_if_len_subset_equals_one(self):
        # If the subset length is equal to one, we are indexing the values.
        # Which allows us to see the count based on index
        self.assertEqual(self.dataframe1.value_counts(subset = ["Name"])[0], 1)
        self.assertEqual(self.dataframe1.value_counts(subset = ["Name"])[1], 1)
        self.assertEqual(self.dataframe1.value_counts(subset = ["Name"])[2], 1)


def suite1():
    suite = unittest.TestSuite()
    suite.addTest(WhiteBoxTesting('test_if_subset_is_none'))
    suite.addTest(WhiteBoxTesting('test_if_sort'))
    suite.addTest(WhiteBoxTesting('test_if_normalize'))
    suite.addTest(WhiteBoxTesting('test_if_len_subset_equals_one'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite1())