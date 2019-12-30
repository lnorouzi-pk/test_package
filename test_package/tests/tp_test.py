# https://docs.python.org/3/library/unittest.html
import os
import sys
from unittest import TestCase
#

#
# import pandas as pd
# sys.path.insert(0, os.path.abspath('/Users/lnorouzi/Documents/Prokarma/Projects/EDA_library/test_package/test_package/'))
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from my_class_function import *
#
use_data = pd.read_csv('../test_package/test_package/data/tips.csv')
def test1():
    cf = FirstClass(use_data)
    s = cf.func1()
    print('****************',s)
    assert isinstance(s, pd.Series)

# def test2():

