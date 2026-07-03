import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([35 , 25,25,15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
myexplode = [0.1 , 0,0,0]
plt.pie(x , labels = mylabels , explode=myexplode , shadow=True , colors=mycolors)
plt.legend(title ="xyz" )
plt.show()