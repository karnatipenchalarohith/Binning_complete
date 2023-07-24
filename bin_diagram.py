import os, re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


from split_bins_intermediate import splitbins_intermediate as splitbins_intermediate

silicon_length = [20e-6, 10e-6, 1e-6, 0.18e-6]
silicon_width = [10.03e-6,10.03e-6,10.03e-6,10.03e-6]
all_width=[]
all_length=[]
words = ['length', 'width']
for root, _, files in os.walk(r'C:\Users\rkar\PycharmProjects\Binning'):
    for path in filter(lambda p: p.endswith('after_bins_joined.txt'), files):
        with open(os.path.join(root, path)) as f:
            for i, line in enumerate(f.readlines()):
                for word in filter(lambda w: w in line, words):
                    print(f'{path}, {i + 1}, {word}, {line.strip()}')
                    #print(f' {line.strip()}')
                    reExp = re.compile("\s*([+-.\w]+)\s*=\s*([+-.\w]+)\s*", flags=re.S)
                    extLst = dict(reExp.findall(line.strip()))
                    print(extLst)
                    print(extLst['length'])
                    print(extLst['width'])
                    all_width.append(extLst['width'])
                    all_length.append(extLst['length'])

print(all_width)
print(all_length)

all_width_change = [str(round(float(item)*1e6,2)) for item in all_width]

all_width_micron=[]

#all_width = [float(x) * 1e6 for x in all_width]
#all_length = [float(x) * 1e6 for x in all_length]



#    all_width_micron[i]=float(i)*1e6


print (all_width_micron)

fig, ax = plt.subplots()
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.scatter(all_width,all_length)

#ax.scatter(list(map(float,all_width)),list(map(float,all_length)))
#plt.gca().invert_xaxis()
ax.invert_xaxis()
ax.invert_yaxis()
ax.xaxis.tick_top()
ax.grid(b=True, which='major', color='k', linestyle='--')

plt.xlabel('Width (um)', labelpad=-300)
#plt.axis.XAxis.set_label_position('top')
plt.ylabel('Length (um)', labelpad=-10)

'''
data = np.random.rand(10, 10) * 20

print (data)
cmap = colors.ListedColormap(['yellow', 'yellow'])
bounds = [0,10,20]
norm = colors.BoundaryNorm(bounds, cmap.N)
ax.imshow(data, cmap=cmap, norm=norm)
'''
z=1
for i,j in zip(all_width,all_length):
    dim=str(round(float(i)*1e6,2)) + "/" + str(round(float(j)*1e6,2))
    ax.annotate(dim,xy=(i,j))


ax.scatter(list(map(str,silicon_width)),list(map(str,silicon_length)),color='g',marker = '*')


fig, bx = plt.subplots()
bx.scatter(list(map(float,silicon_width)),list(map(float,silicon_length)),color='g',marker = '*')


'''
ax1.scatter(x[:4], y[:4], s=10, c='b', marker="s", label='first')
ax1.scatter(x[40:],y[40:], s=10, c='r', marker="o", label='second')

'''
'''
fig, bx = plt.subplots()


bx.scatter(all_width,all_length)
#plt.gca().invert_xaxis()
bx.invert_xaxis()
bx.invert_yaxis()
bx.xaxis.tick_top()
bx.grid(b=True, which='major', color='k', linestyle='--')

'''

'''
for i,j in zip(silicon_width,silicon_length):
    dim=str(round(float(i)*1e6,2)) + "/" + str(round(float(j)*1e6,2))
    ax.annotate(dim,xy=(i,j))
'''

#    binnumber="Bin_" + str(z)
#    ax.annotate(binnumber, xy=(i, j))


        #ax.annotate(dim, xy=(new_x, new_y))


for i,j in zip(all_width,all_length):
    dim=str('bin')
    q=float(i)//2
    p=float(j)//2
    ax.annotate(dim,xy=(q,0))


'''

for i in range(len(all_width)-1):
#    print(all_width[i])
#    print(all_width[i+1]) round(float(i)*1e6,2)
    new_x=(float(all_width[i]) + float(all_width[i+1]))//2
    print(new_x)
    dim2= "binnable"
    for j in range(len(all_length) - 1):
        new_y = (float(all_length[j]) + float(all_length[j+1]))//2
        print(new_y)
        ax.annotate(dim2, xy=(new_x, new_y))

'''
#        print(all_length[j])
#        print(all_length[j + 1])

#    print(round(float(all_width[i])*1e6,2))




#    ax.annotate(dim,xy=(i))


#ax.annotate('BIN1', xy=(100e-6, 5e-6))

plt.show()




for i in range(len(all_width)-1):
#    print(all_width[i])
#    print(all_width[i+1]) round(float(i)*1e6,2)
    new_x=(round(float(all_width[i])*1e6,2) + round(float(all_width[i+1])*1e6,2))//2
#    print(new_x)
    dim= "binnable"
    print(round(float(all_width[i])*1e6,2))


'''
    for j in range(len(all_length) - 1):

#        print(all_length[j])
#        print(all_length[j + 1])
        new_y = (round(float(all_length[j])*1e6,2) + round(float(all_length[j+1])*1e6,2))//2
        print(new_x)
        print(new_y)


'''

fig, ax = plt.subplots()

# Add some data
ax.scatter([1, 2, 3, 4], [10, 20, 25, 30])

# Add the labels
ax.text(1, 10, 'Label 1')
ax.text(2, 20, 'Label 2')
ax.text(3, 25, 'Label 3')
ax.text(4, 30, 'Label 4')

# Show the plot
plt.show()

'''
count=0
for i,j in zip(all_width,all_length):
    print(i,j)


print(count)

'''


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.invert_yaxis()
ax1.xaxis.tick_top()


ax1.scatter(list(map(str,all_length)), list(map(str,all_width)), s=10, c='b', marker="s", label='first')
ax1.scatter(list(map(str,silicon_length)),list(map(str,silicon_width)), s=10, c='r', marker="o", label='second')
ax1.invert_xaxis()
ax1.invert_yaxis()
ax1.xaxis.tick_top()
ax1.grid(b=True, which='major', color='k', linestyle='--')

plt.legend(loc='upper left')
plt.show()




fig = plt.figure()
ax2 = fig.add_subplot(111)
ax2.invert_yaxis()
ax2.xaxis.tick_top()


ax2.scatter(list(map(float,all_length)), list(map(float,all_width)), s=10, c='b', marker="s", label='first')
ax2.scatter(list(map(float,silicon_length)),list(map(float,silicon_width)), s=10, c='r', marker="o", label='second')
ax2.invert_xaxis()
ax2.invert_yaxis()
ax2.set_yscale('log')
ax2.set_xscale('log')
#ax2.set_aspect('equal', adjustable='box')
ax2.xaxis.tick_top()
ax2.grid(b=True, which='major', color='k', linestyle='None')

plt.legend(loc='upper left')


for i,j in zip(list(map(float,all_width)),list(map(float,all_length))):
    dim=str(round(float(i)*1e6,2)) + "/" + str(round(float(j)*1e6,2))
    ax2.annotate(dim,xy=(i,j))



for i in range(len(all_width)-1):
#    print(all_width[i])
#    print(all_width[i+1]) round(float(i)*1e6,2)
    new_x=(float(all_width[i]) + float(all_width[i+1]))//2
    print(new_x)
    dim2= "binnable"
    for j in range(len(all_length) - 1):
        new_y = (float(all_length[j]) + float(all_length[j+1]))//2
        print(new_y)
        ax2.annotate(dim2, xy=(new_x, float(all_length[j])))



plt.show()




for i in range(len(all_width)-1):
#    print(all_width[i])
#    print(all_width[i+1]) round(float(i)*1e6,2)
    new_x=(round(float(all_width[i])*1e6,2) + round(float(all_width[i+1])*1e6,2))//2
#    print(new_x)
    dim= "binnable"
    print(round(float(all_width[i])*1e6,2))




print(type(all_width))
print(type(silicon_width))

print((all_width))
print((silicon_width))

print((all_length))
print((silicon_length))


print(list(map(str,all_length)))
print(list(map(str,silicon_length)))

print(all_width_change)