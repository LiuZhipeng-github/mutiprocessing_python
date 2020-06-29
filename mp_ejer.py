# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:45:22 2018

@author: python
"""


#mpi4py no hay memoria compartida
#multiprocessing hay memoria compartida



import multiprocessing 



def foo(i):
    j=i*2;
    name= multiprocessing.current_process().name
    print('2 x %s = %s  ;  Called function in process: %s'%(i,j,name))
    return
    
if __name__ =='__main__':
    Process_jobs=[]
    for i in range(8):
        p= multiprocessing.Process(target= foo, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()