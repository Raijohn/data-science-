import numpy as np
list1 = []
list2 = []
rows = int(input("rows "))
coloms = int(input("coloms"))
for i in range(rows):
    row = []
    for i in range(coloms):
        row.append(int(input("value ")))
    list1.append(row)
for i in range(rows):
    row = []
    for i in range(coloms):
        row.append(int(input("value ")))
    list2.append(row)   
array1 = np.array(list1)
array2 = np.array(list2)
print(array1)
print(array2)
print(array1+array2)
print(array1-array2)