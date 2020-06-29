# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:45:22 2018

@author: python
"""
#mpi4py no hay memoria compartida
#multiprocessing hay memoria compartida



import multiprocessing 
def foo(i):
    print('Called function in process: %s'%i)
    return
    
if __name__ =='__main__':
    Process_jobs=[]
    for i in range(5):
        p= multiprocessing.Process(target= foo, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()