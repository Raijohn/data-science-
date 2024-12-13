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
x2 = np.arange(1,11,0.01)
plt.plot(x2,x2**2,"b-",label="plot²")
plt.plot(x2,x2**3,"r-",label="plot³")
plt.legend()
plt.show()

#bar graph
plt.bar([1,3,5,7],[21,94,62,84])
plt.bar([2,4,6,8],[12,49,26,48])
plt.show()
#showing catagorical data in bar plot
plt.bar(["male","female"],[10,7])
plt.show()
#histogram
age = np.random.randint(1,80,20)
print(age)
bins = np.arange(1,81,10)
plt.hist(age,bins,rwidth=0.8)
plt.show()
#scatter plot
plt.scatter(x,y,color="blue",marker="x",s=40)
plt.show()
#pie chart
piechart = np.random.randint(1,20,5)
piechartsubject = ["pizza","burger","saled","spegetie","rice"]
colors = ["c","m","g","r","b"]
plt.pie(piechart,labels=piechartsubject,colors=colors,startangle=45,autopct='%1.1f%%',shadow=True)
plt.show()
#stack plot
Days = ["Monday","thuesday","wednesday","thursday","friday"]
eating = [2,4,1,3,5]
studiing = [6,9,7,8,10]
playing = [2,8,3,5,0]
sleeping = [10,8,9,12,13]
names = ["eating","studiing","playing","sleeping"]
plt.stackplot(Days,eating,studiing,playing,sleeping,labels=names)
plt.legend()
plt.show()
#subplots
plt.subplot(2,2,3)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.pie(piechart,labels=piechartsubject,colors=colors,startangle=45,autopct='%1.1f%%',shadow=True)
plt.show()
#bar graph
plt.bar([1,3,5,7],[21,94,62,84])
plt.bar([2,4,6,8],[12,49,26,48])
plt.show()
