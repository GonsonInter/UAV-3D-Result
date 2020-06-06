import matplotlib.pyplot as plt
from Experiment import tools
from mpl_toolkits.mplot3d import Axes3D
import time

fig = plt.figure(figsize=(8,6))
#ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)

filename = r'C:\Users\王子杰\Desktop\experiment\\' + 'path.txt'

tp = tools.readfile(filename)

xs = tp[0]
ys = tp[1]
zs = tp[2]
aps = tp[3]


color = ['r', 'g', 'b', 'y']


# 设置坐标轴
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


#设置刻度
plt.xticks(range(max(xs) + 1))
plt.yticks(range(max(ys) + 1))
ax.set_zticks(range(max(zs) + 1))

for i in range(len(xs)):

    ax.scatter(xs[i], ys[i], zs[i], c=color[aps[i]], marker='.')

    x_pair = []
    x_pair.append(xs[i])
    x_pair.append(xs[(i+1)%len(xs)])
    y_pair = []
    y_pair.append(ys[i])
    y_pair.append(ys[(i+1)%len(xs)])
    z_pair = []
    z_pair.append(zs[i])
    z_pair.append(zs[(i+1)%len(xs)])

    plt.plot(x_pair, y_pair, z_pair, color=color[aps[i]])
    time.sleep(0.01)




# 显示图像
plt.show()







