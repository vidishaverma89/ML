import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,6,8,9,10]
plt.plot(x,y,color="blue")
plt.grid(True)
plt.title("Graph")
plt.xlabel("pressure")
plt.ylabel("temperature")
plt.savefig("data.png")
plt.show()