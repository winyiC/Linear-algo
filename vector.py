import matplotlib.pyplot as plt
import numpy as np

# Vector origin location
V=np.array([[2,3],[-1,-1.5]])
origin=np.array([[0,0],[0,0]])


# Creating plot
plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
v12 = V[0] + V[1] # adding up the 1st (red) and 2nd (blue) vectors
plt.quiver(*origin, v12[0], v12[1])


# x-lim and y-lim
plt.xlim(-3, 9)
plt.ylim(-3,10 )

# Show plot with grid
plt.grid()
plt.show()

