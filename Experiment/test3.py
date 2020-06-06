import matplotlib.pyplot as plt
from Experiment import tools
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 6))
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

#设置坐标范围
plt.xlim(min(xs), max(xs))
plt.ylim(min(ys), max(ys))
ax.set_zticks([0,1,2])


def init():
    pass

def update(frame):
    if frame < len(xs):
        x_pair = []
        x_pair.append(xs[frame])
        x_pair.append(xs[(frame + 1) % len(xs)])
        y_pair = []
        y_pair.append(ys[frame])
        y_pair.append(ys[(frame + 1) % len(xs)])
        z_pair = []
        z_pair.append(zs[frame])
        z_pair.append(zs[(frame + 1) % len(xs)])

        #画点
        if aps[frame] == aps[(frame + 1) % len(xs)]:
            if frame == 0 or frame == len(xs) - 1:
                ax.scatter(xs[frame], ys[frame], zs[frame], c=color[aps[frame]], marker='*', s=150)        #出发点和终止点
            else:
                ax.scatter(xs[frame], ys[frame], zs[frame], c=color[aps[frame]], marker='.')
        else:
            ax.scatter(xs[frame], ys[frame], zs[frame], c=color[aps[(frame + 1) % len(xs)]], marker='^', s=100)        #AP切换处

        #画线
        if frame < len(xs) - 1 :
            plt.plot(x_pair, y_pair, z_pair, color=color[aps[frame]])



ani = FuncAnimation(fig, update, init_func=init, blit=False, interval=50)


# 显示图像
plt.show()







