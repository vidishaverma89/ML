import matplotlib.pyplot as plt
from scipy import stats
x=[2,5,8,10]
y=[31,33,34,35]
slope, intercept, correlationcoefficient, p, slopeerror = stats.linregress(x,y)
def linefunc(x):
  return slope * x + intercept

model = list(map(linefunc, x))
plt.scatter(x,y)
plt.plot(x,model)
plt.grid(True)
plt.title("Bar Graph")
plt.xlabel("time")
plt.ylabel("temperature")
predictedvalue=linefunc(100)
print(predictedvalue)
plt.show()
