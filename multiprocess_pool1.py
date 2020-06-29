# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:04:49 2018

@author: python
"""

import multiprocessing

def function_square(data):
    result =data*data
    return result
    
if __name__=='__main__':
   inputs =list(range(100))
   #generamos una lista 
   pool = multiprocessing.Pool(processes=4)
   #generamos cuatro procesos
   pool_outputs = pool.map(function_square,inputs)
   #map aplica la funcion function_square a un conjunto de datos input
   pool.close()
   #cerramos el pool de procesos 
   pool.join()
   #juntamos los resultados
   print('Process: ', pool_outputs)