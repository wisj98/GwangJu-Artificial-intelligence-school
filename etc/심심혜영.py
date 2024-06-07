import matplotlib.pyplot as plt
import numpy as np
def make_func(x):
    x_multi = 1
    x_square = 1
    multi = False
    square = False
    num = 0
    for i in x:
        if num == 0 and i in ['1','2','3','4','5','6','7','8','9']:
            num = int(i)
            print('a')
        elif num != 0 and i in ['0','1','2','3','4','5','6','7','8','9']:
            num = num*10 + int(i)
            print('b')
        if i == ' ' and square == True:
            x_square = num
            num = 0
            print('c')

        if i in ['x','X'] and num != 0:
            x_multi = num
            num = 0
            print('d')
        
        if i == '*' and multi == False:
            multi = True
            print('e')
        elif i == '*' and multi == True:
            square = True
            print('f')
        print(num)
        
    a = np.arange(-100,100)
    print(x_multi, x_square)
    b = x_multi * a ** x_square

    plt.plot(a,b)
    plt.show()

make_func("555x**1 ")