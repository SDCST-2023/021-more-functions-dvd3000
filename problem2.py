#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(i1,i2,i3):
    # find hypotenuse
    if (i1 >= i2) and (i1 >= i3):
        a = i3
        b = i2
        c = i1
    elif (i2 >= i1) and (i2 >= i3):
        a = i3
        b = i1
        c = i2
    else:
        a = i1
        b = i2
        c = i3
    if c ** 2 == (a ** 2) + (b ** 2):
        if a + b < c:
            return 0
        else:
            return 2
    elif c ** 2 < (a ** 2) + (b ** 2):
        if a + b < c:
            return 0
        else:
            return 1
    elif c ** 2 > (a ** 2) + (b ** 2):
        if a + b < c:
            return 0
        else:
            return 3
    else:
        return 0

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
