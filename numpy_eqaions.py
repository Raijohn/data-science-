import numpy as np
h = True 
x = np.arange(0,10,1)
while h:
    calculation = int(input("would you like to solve a linier eqaision(1) or a Quadratic Equation(2)"))
    if calculation == 1:
        print("ax+b")
        a = int(input("input a "))
        b = int(input("input b "))
        print(a,"x +",b)
        print(a * x + b)
    elif calculation == 2:
        print("ax^2 + bx + c")
        a = int(input("input a "))
        b = int(input("input b "))
        c = int(input("input c "))
        print(a,"x^2 +",b,"x +",c)
        print(a * x**2 + b * x + c)

    else:
          print("")   