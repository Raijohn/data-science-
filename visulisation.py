import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(1,11)
print(x)
y = np.random.randint(1,20,10)
print(y)

#line plot
plt.figure(figsize=(8,6))
plt.plot(x,y,"c-p",linewidth=3,label="randomY")
#title of plot
plt.title("plot1")

plt.xlabel("x")
plt.ylabel("y")

plt.legend()

#plt.yticks(ticks=y,labels=np.arange(2,21,2))
plt.axis([0,10,0,20])

plt.show()

#mutiple lines on a single graph
x = np.arange(1,11,0.01)
plt.plot(x,x**2,"b-",label="plot²")
plt.plot(x,x**3,"r-",label="plot³")
plt.legend()
plt.show()

#bar graph
plt.bar([1,3,5,7],[21,94,62,84])
plt.bar([2,4,6,8],[12,49,26,48])
plt.show()