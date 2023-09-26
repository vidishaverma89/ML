a, b, c = int(input("A=")), int(input("B=")), int(input("C="))
if a >= b and a >= c:
    highest = a
elif b >= c:
    highest = b
else:
    highest = c

print(highest)

