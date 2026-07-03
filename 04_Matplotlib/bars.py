import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 1])

plt.barh(x,y , color='#4CAF50' , height=0.8)
plt.show()