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