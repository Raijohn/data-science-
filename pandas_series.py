import pandas as pd
import numpy as np 
array = np.random.randint(1,100,10)
print(array,type(array))
s = pd.Series(array)
print(s)
print(type(s))
#statistical operations
print(s.min())
print(s.max())
print(s.mean())
print(s.median())
print(s.mode())
#sorting series
s2 = s.sort_values()
print(s2)
s2 = s.sort_values(ascending=False)
print(s2)
#count valus
print(s.value_counts())