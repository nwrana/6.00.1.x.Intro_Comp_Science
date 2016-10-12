# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:31:04 2016

@author: w15psnnw
"""

#==============================================================================
#  Problem 6
# (15 points possible)
# 
# Implement a function that meets the specifications below.
# 
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
# 
# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
# 
#==============================================================================

def deep_reverse(L):
     """ assumes L is a list of lists whose elements are ints
     Mutates L such that it reverses its elements and also 
     reverses the order of the int elements in every element of L. 
     It does not return anything.
     """
     
     #final_list = []       
     new_list = list(reversed(L))
     for i in range(len(new_list)):
         temp = new_list[i]
         temp_rev = list(reversed(temp))
         #final_list.append(temp_rev)
         L[i] = temp_rev
     
     