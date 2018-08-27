import matplotlib.pyplot as plt
act=['eat','sleep','work','play']
slices=[3,7,8,6]
color=['r','m','g','b']
plt.pie(slices,labels=act,colors=color,startangle=90,shadow=True,explode=(0.1,0,0,0),autopct='%1.2f%%')
plt.legend()
plt.show()
