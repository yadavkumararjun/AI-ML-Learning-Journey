import matplotlib.pyplot as plt 
import numpy as np 

''' Display Multiple Plots
With the subplot() function you can 
draw multiple plots in one figure:
'''
#plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,2,1) #the figure has 1 row, 2 columns, and this plot is the first plot.
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40]) 
plt.subplot(2, 2, 2)  #the figure has 1 row, 2 columns, and this plot is the second plot.
plt.plot(x,y)


#plot3
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40]) 
plt.subplot(2, 2, 3)  
plt.plot(x,y)


#plot 4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40]) 
plt.subplot(2, 2, 4)  
plt.plot(x,y)
plt.show()



''' 
Refer below link for more info
https://www.w3schools.com/python/matplotlib_subplot.asp
'''
