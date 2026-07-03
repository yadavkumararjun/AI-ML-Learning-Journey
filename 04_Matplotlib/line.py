import matplotlib.pyplot as plt
import numpy as np 

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

# marker ='*'
#Format Strings fmt
# syntax:
# marker|line|color 
''' Line Syntax	    Description
    '-' 	        Solid line	
    ':'	            Dotted line	
    '--'	        Dashed line	
    '-.'	        Dashed/dotted line 
'''
# plt.plot(x1,y1 ,'o-b')  #marker is user to highlight points with different shape
# plt.plot(x1,y1,marker='o' , ms=20 , mfc='g',mec='g')   # ms=>marker size , mfc=> marker face color  , mec=> marker edge color


#LINE STYLING 

# plt.plot(x1,y1, ls='dashed' , color='hotpink' , linewidth='10.4')   # ls => linestyle
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.grid()
plt.show()


