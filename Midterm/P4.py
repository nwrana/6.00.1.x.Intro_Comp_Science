# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:35:16 2016

@author: w15psnnw
"""
"""
    closest_power(3,12) returns 2
    closest_power(4,12) returns 2
    closest_power(4,1) returns 0
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    #need to establish reasonable high and low limits/boundaries
    low = 0 #base > 1, therefore do not need to consider negative values
    high = int(num*base) #this is one full exponent above the desired base 
    spread = high 
    minimum_value = 0
    
    for i in range(low,high):
        #print(i)
        #print('Spread: ' + str(spread))
        temp_calc = base**i
        #Need to check to see how close temp_calc is to number
        #print('Calculation: ' + str(temp_calc))
        temp_spread = abs(num-temp_calc)
        if temp_spread > spread:
            break
        elif temp_spread == spread:
            minimum_value == i -1
            break
        else:
            minimum_value = i
            spread = temp_spread
            
    return minimum_value