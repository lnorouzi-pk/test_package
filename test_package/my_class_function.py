import pandas as pd
import numpy as np
# /Users/lnorouzi/Documents/Prokarma/Projects/EDA_library/test_package/test_package/my_class_function.py
class FirstClass(object):
    '''
    The class to check
    '''

    def __init__(self,data1):

        '''
        the init function
        '''

        self.data1 = data1
        # self.data2 = data2

    def func1(self):
        '''
        if the data has null in it

        :return: bool
        '''

        # self.data1.isnull().any()

        return self.data1.isnull().any()


# data = pd.read_csv('../data/tips.csv')
#
# cf = FirstClass(data)
#
# print(cf.func1(), type(cf.func1()))