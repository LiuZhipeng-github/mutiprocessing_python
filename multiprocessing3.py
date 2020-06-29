# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:31:28 2018

@author: python
"""


import multiprocessing

def function_square(data):
       result = data*data
       return result

if __name__ == '__main__':
       inputs = list(range(100))
       pool = multiprocessing.Pool(processes=4)
       pool_outputs = pool.map(function_square, inputs)
       pool.close()
       pool.join()
print ('Pool    :', pool_outputs)