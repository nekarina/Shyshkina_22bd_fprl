import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
z0 = float(input("Enter z0: "))
R = float(input("Enter R: "))
d = math.sqrt((x-x0)**2 + (y - y0)**2 + (z - z0)**2)
if d < R:
    print("Точка знаходиться всередині сфери")
elif d==R:
    print("Точка лежить на поверхні сфери")
else :
    print("Точка знаходиться поза поверхнею сфери")
