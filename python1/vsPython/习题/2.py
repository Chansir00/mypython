import matplotlib.pyplot as plt

x = [1,2,3,4,5] 
y = [2,4,6,8,10]

plt.plot(x, y) 
plt.title('A Pig') 
plt.xlabel('X-Axis') 
plt.ylabel('Y-Axis')

plt.scatter(x, y, color='red', marker='o', s=50)

plt.show()