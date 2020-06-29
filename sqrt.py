# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 08:23:17 2018

@author: python
"""

from multiprocessing import Pool
#import matplotlib.pyplot as plt
import numpy as np
def sqrt(x):
    return np.sqrt(x)
    
if __name__== '__main__':
    pool=Pool()
    #dividir la tarea, inicia un processo en cada procesador fisico de la computadora
    #divide la entrada en fragmentos del mismo tamanño y pone tareas en una lista de tareas pendientes
    #cada proceso toma una tarea de la lista y ejecuta el map
    # y se espera a juntar los resultados al final para unirlos y entergarlos
    roots =pool.map(sqrt,range(100))
    #map aplica la funcion a un rango de datos
    # numpy no es serializable por lo que se le llama de manera indirecta
    print(roots)
    #plt.plot(roots)   
    # Conviene usar esto con entrada unica de info
        