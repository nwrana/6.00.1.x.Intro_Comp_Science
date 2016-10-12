# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:39:12 2016

@author: w15psnnw
"""

def genPrimes():
    x = 2
    tracker = []
    while True:
        count = 0
        for i in tracker:
            test = x % i 
            if test != 0:
                count += 1
            else:
                break
            
        if count == len(tracker):
            tracker.append(x)
            next = x            
            yield next       
    
        x += 1
  
        
            
        