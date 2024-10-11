import numpy as np

list = [3,5,1,2,4]
print(list)
print(type(list))
array = np.array(list)
print(array)
print(type(array))

for i in range(len(list)):
    list[i] = list[i]*2


print(list)
print(array*2)

#array of zeros
print(np.zeros(5,int))
#array of ones
print(np.ones(5,int))

print(np.ones((3,4)))
#array in range
array1 = np.arange(1,100,12)
print(array1)
#reshape
array2 = array1.reshape(3,3)
print(array2)
#dimention 
print(array1.ndim)
print(array2.ndim)

#shape 
print(array1.shape)
print(array2.shape)
#size
print(array1.size)
print(array1.size)
#permutation
print(np.random.permutation(array1))
print(np.random.permutation(array1))
print(np.random.permutation(array1))
#array whit random numbers
array3 = np.random.randint(1,100,9)
print(array3)
print(np.random.randint(1,100,(9,3)))
#sorting
print(np.sort(array3))