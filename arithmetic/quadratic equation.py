a = 4
b = 8
c = 0

d = (b**2) - (4 * a * c)
d = d**0.5
# print(100**.5)
x = (-b - d) / (2 * a)
y = (-b + d) / (2 * a)
print("solutions are{0},{1}".format(x, y))
