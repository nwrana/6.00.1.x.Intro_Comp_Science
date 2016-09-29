#==============================================================================
# Intro to Computer Science and Programming Using Python
# Week 2
#Polysum
#(10/10 points)

#A regular polygon has n number of sides. Each side has length s.

#    The area of a regular polygon is: 
#    The perimeter of a polygon is: length of the boundary of the polygon

#Write a function called polysum that takes 2 arguments, n and s. This function should 
#sum the area and square of the perimeter of the regular polygon. The function returns 
#the sum, rounded to 4 decimal places.

#==============================================================================

def polysum(n, s):
    '''
    input: n, s > 0,int or float
        n = number of sides
        s = length of ecah side
    output: (area + permieter^2) of a polygon, int or float, accurate to 4 decimals
    '''
    #import specific functions from 'math' module
    from math import pi,tan 
    
    #introduce rule to prevent negative inputs
    if n <= 0 or s <= 0:
        return 'Arguments must be positive integers or floats'
    
    #create variables and convert to float
    poly_area = float((0.25 * n * (s**2)) / (tan(pi/n)))
    poly_perim = float(n * s)
    
    #return calculation, rounded to 4 decimals
    return round(poly_area + poly_perim**2, 4)