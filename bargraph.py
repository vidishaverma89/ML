import matplotlib.pyplot as plt
x=[2,5,8,10]
y=[31,33,34,35]
plt.scatter(x,y)
plt.plot(x,y)
plt.grid(True)
plt.title("Bar Graph")
plt.xlabel("time")
plt.ylabel("temperature")
plt.show()