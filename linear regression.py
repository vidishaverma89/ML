import matplotlib.pyplot as plt
from scipy import stats

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
slope, intercept, correlationcoefficient, p, slopeerror = stats.linregress(
    x, y
)  # Fit a straight line to the data


def linefunc(x):
    return slope * x + intercept  # y=mx+c wher m is the slope and c is the intecept


model = list(map(linefunc, x))  # Get a fitted line
plt.scatter(x, y, color="red")
plt.plot(x, model)
plt.grid(True)
plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
predictedvalue = linefunc(100)  # Predict the value
print("Predicted value at 100 ", predictedvalue)
plt.show()
