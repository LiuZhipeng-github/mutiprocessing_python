# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:37:40 2018

@author: python
"""

from multiprocessing import Process
from multiprocessing import Pipe 

def f(conn):
    conn.send([42,None, 'hello'])
    conn.close()
    
if __name__== '__main__':
    parent_conn ,child_conn=Pipe()
    #child es el canal de ida , parent es el de vuelta
    p = Process(target= f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()
    #las tuberías son canales bidireccionales 
    

    
