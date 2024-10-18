import numpy as np
array = np.arange(1,11,1)
print(array)
#slicing
'''print(array[1:5])
print(array[:7])
print(array[3:])
print(array[::2])'''
#slicing 2D
array2 = np.random.randint(1,10,(3,4))
print(array2)
'''print(array2[1:3,0:2])'''
#selection by index
print(array[[1,4,7,9]])
#conditinal slicing
print(array[array % 2 == 0])
print(array2[array2 > 5])
#mathe maticle operations
array3 = np.random.randint(11,20,(3,4))
print(array2)
print(array3)
print(array2+array3)
def math(x):
    return 2*x+5
print(math(array))