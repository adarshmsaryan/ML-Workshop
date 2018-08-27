import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[2,4,3,5,6,7]
plt.plot(x,y, color='yellow',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='red',markersize=12)
plt.ylim(1,7)
plt.xlim(1,7)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('some cool customization!')
plt.show()
