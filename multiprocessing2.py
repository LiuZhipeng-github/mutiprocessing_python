# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:52:14 2018

@author: python
"""

import multiprocessing
import time
 
def foo():
    name= multiprocessing.current_process().name
    print('Called function in process: %s \n' %name)
    time.sleep(3)
    print('Exiting %s \n '%name)    
    return
    
if __name__ =='__main__':
    Process_with_name=multiprocessing.Process(name ='foo_process', target=foo)
    Process_with_default_name=multiprocessing.Process(target=foo)
    Process_with_name.start()
    Process_with_default_name.start()
    