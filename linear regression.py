import matplotlib.pyplot as plt
from scipy import stats

x = [2, 4, 6, 8]
# y = [2*i+3 for i in x]
y = [7, 10, 16, 19]
print(x, y)
slope, intercept, correlationcoefficient, p, slopeerror = stats.linregress(
    x, y
)  # Fit a straight line to the data


def linefunc(x):
    return slope * x + intercept  # y=mx+c where m is the slope and c is the intecept


model = list(map(linefunc, x))  # Get a fitted line
plt.scatter(x, y, color="red")
plt.plot(x, model)
plt.grid(True)
plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
predictedx = 1
predictedvalue = linefunc(predictedx)  # Predict the value
print("Predicted value at ", predictedx, predictedvalue)
plt.show()
