import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,-9,10]
y=[x*x for x in x]

plt.plot(y,x)
plt.grid(True)
plt.show()