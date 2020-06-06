import matplotlib.pyplot as plt
import numpy as np

algorithms = ['C0', 'C1', 'C2', 'C3']


####################################结果图#####################################################
costs = [65100, 202075, 83275, 258400]
ap_switch_num = [2, 323, 2, 427]

x1 = [x - 0.2 for x in range(len(algorithms))]
y1 = [n * 2 for n in range(len(algorithms))]
x2 = [x + 0.2 for x in range(len(algorithms))]
y2 = [x ** 2 for x in x2]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

w = 0.2

idx = np.arange(0,len(algorithms))

plt.xticks(idx, algorithms)

l1 = plt.bar(idx - 0.12, costs, width=0.2)

for i in l1:
    h=i.get_height()
    plt.text(i.get_x() + i.get_width() / 2, h, '%d'%int(h), ha='center')

plt.xlabel('Different Conditions')
plt.ylabel('Total Energy Consumption')


ax1 = ax.twinx()

l2 = plt.bar(idx + 0.12, ap_switch_num, width=0.2, color='red')

plt.xlabel('Algorithms')

plt.legend(handles=[l1, l2], labels=['Total Energy Consumption', 'AP Switching Num'], loc='upper left')

plt.ylim(0, max(ap_switch_num) + 100)

for i in l2:
    h=i.get_height()
    plt.text(i.get_x() + i.get_width() / 2, h, '%d'%int(h), ha='center')

plt.ylabel('The Num of AP Switching')

#################################################################################################################


##########################################粒度对比图##############################################################
fig = plt.figure(figsize=(10, 6))

granularity = ['3m', '1.5m', '1m']

C0_cost = [11575, 49675, 115525]
C1_cost = [15300, 119925, 402800]
C2_cost = [12025, 51300, 176255]
C3_cost = [17300, 148500, 499525]

C0_ap = [2, 2, 2]
C1_ap = [25, 193, 649]
C2_ap = [1, 2, 2]
C3_ap = [29, 247, 829]

#plt.subplot(121)
plt.plot(granularity, C0_cost, ms=5, marker='o')
plt.plot(granularity, C1_cost, ms=5, marker='o')
plt.plot(granularity, C2_cost, ms=5, marker='o')
plt.plot(granularity, C3_cost, ms=5, marker='o')

plt.xlabel('''Granularity''')
plt.ylabel('Total Energy Consumption')

plt.legend(labels=['C0', 'C1', 'C2', 'C3'], loc='upper left')


# plt.subplot(122)
# plt.plot(granularity, C0_ap, ms=5, marker='o')
# plt.plot(granularity, C1_ap, ms=5, marker='o')
# plt.plot(granularity, C2_ap, ms=5, marker='o')
# plt.plot(granularity, C3_ap, ms=5, marker='o')
#
# plt.xlabel('''Granularity
#
# (b)''')
# plt.ylabel('AP Switching Num')
#
# #plt.yticks([0,1,2,3,4,5,6], [1, 2, 10, 100, 200, 500, 100])
#
# plt.legend(labels=['C0', 'C1', 'C2', 'C3'], loc='upper left')



#################################################################################################################

##################################障碍物设置对比图#################################################################
fig1 = plt.figure(figsize=(10, 6))

obstacles = ['O0', 'O1', 'O2', 'O3']

C0_cost = [21925, 21775, 21275, 20375]
C1_cost = [69900, 60450, 59175, 50875]
C2_cost = [30700, 29175, 26425, 23150]
C3_cost = [80500, 77725, 71200, 61750]


#plt.subplot(121)
plt.plot(obstacles, C0_cost, ms=5, marker='o')
plt.plot(obstacles, C1_cost, ms=5, marker='o')
plt.plot(obstacles, C2_cost, ms=5, marker='o')
plt.plot(obstacles, C3_cost, ms=5, marker='o')

plt.xlabel('Obstacle Settings')
plt.ylabel('Total Energy Consumption')

plt.legend(labels=['C0', 'C1', 'C2', 'C3'], loc='upper right')


#################################################################################################################

###########################不同AP设置实验结果#####################################################################
fig2 = plt.figure(figsize=(10, 6))

AP_Set = ['C0', 'C1', 'C2', 'C3']

A0_cost = [5425, 5375, 6375, 6225]
A1_cost = [13025, 26500, 15650, 43350]
A2_cost = [20300, 52200, 24000, 81525]



#plt.subplot(121)
plt.plot(AP_Set, A0_cost, ms=5, marker='o')
plt.plot(AP_Set, A1_cost, ms=5, marker='o')
plt.plot(AP_Set, A2_cost, ms=5, marker='o')


for s, x, y ,z in zip(AP_Set, A0_cost, A1_cost, A2_cost):
    plt.text(s, x + 50, str(x), ha='center', va='bottom', fontsize=10, rotation=0)
    plt.text(s, y + 50, str(y), ha='center', va='bottom', fontsize=10,rotation=0)
    plt.text(s, z + 50, str(z), ha='center', va='bottom', fontsize=10, rotation=0)



plt.xlabel('')
plt.ylabel('Total Energy Consumption')

plt.legend(labels=['A0', 'A1', 'A2'], loc='upper left')

#################################################################################################################


plt.show()



