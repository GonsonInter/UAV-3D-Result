import matplotlib.pyplot as plt
from Experiment import tools
from mpl_toolkits.mplot3d import Axes3D


filename = r'C:\Users\王子杰\Desktop\experiment\\' + 'map.txt'

tp = tools.readfile(filename)

xs = tp[0]
ys = tp[1]
zs = tp[2]



fig = plt.figure(figsize=(8,6))
ax = Axes3D(fig)
ax.scatter(xs, ys, zs, c = 'black', marker = '.') #点为红色三角形

plt.xlabel("X")
plt.xticks(range(0, max(xs)+1))
plt.ylabel("Y")
plt.yticks(range(0, max(ys)+1))
ax.set_zlabel("Z")
ax.set_zticks(range(0, max(zs)+1))

plt.show()