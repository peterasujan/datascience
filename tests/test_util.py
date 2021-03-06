import doctest

import datascience as ds
from datascience import util
import numpy as np



def test_doctests():
    results = doctest.testmod(util)
    assert results.failed == 0


def test_percentile():
    assert ds.percentile(0, [1, 3, 5, 9]) == 1
    assert ds.percentile(33, [1, 3, 5, 9]) == 3
    assert ds.percentile(34, [1, 3, 5, 9]) == 5
    assert ds.percentile(66, [1, 3, 5, 9]) == 5
    assert ds.percentile(67, [1, 3, 5, 9]) == 9

    f1 = ds.percentile(67)
    assert f1([1, 3, 5, 9]) == 9

    f2 = ds.percentile(66)
    assert f2([1, 3, 5, 9]) == 5


def test_table_apply():
    data = np.ones([3, 100])
    data[1] = 2
    data[2] = 3
    tab = ds.Table(data, ['a', 'b', 'c'])
    newtab = util.table_apply(tab, np.mean)
    assert newtab.num_rows == 1
    assert all(newtab['a'] == np.mean(tab['a']))

    newtab = util.table_apply(tab, lambda a: a+1)
    assert all(newtab['a'] == tab['a'] + 1)

    newtab = util.table_apply(tab, lambda a: a+1, subset=['b', 'c'])
    assert all(newtab['a'] == tab['a'])
    assert all(newtab['b'] == tab['b'] + 1)
