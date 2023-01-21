import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2


"""
figure = plt.figure()

cube = figure.add_axes([0.1,0.1,0.8,0.8])
cube.plot(x,y,'b')
cube.set_xlabel("X Axis")
cube.set_ylabel('Y Axis')
cube.set_title('Cube')

square = figure.add_axes([0.2,0.6,0.3,0.3])
square.plot(x,y,'r')
square.set_xlabel("X Axis")
square.set_ylabel('Y Axis')
square.set_title('Square')

"""

"""
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend()
"""

fig,axes = plt.subplots(nrows=2,ncols=1)
axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
plt.show()