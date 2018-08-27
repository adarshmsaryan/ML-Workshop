import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('text.csv','r')as csvfile:
	plots=csv.reader(csvfile)
	for col in plots:
		x.append((col[0]))
		y.append((col[1]))
plt.plot(x,y,label="file")
plt.xlabel('x')
plt.ylabel('y')
plt.title('test graph')
plt.legend()
plt.show()
