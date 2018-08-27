import matplotlib.pyplot as plt
ages=[2,5,70,40,50,60,79,30,67,78,45,65,18,90,32,40,21,20,30]
range=(0,100)
bins=10
plt.hist(ages,bins,range,color='pink',histtype='bar',rwidth=0.8)
plt.xlabel('ages')
plt.ylabel('n of ppls')
plt.title('my histogram')
plt.show()
