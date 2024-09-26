import math
def point(x, y, z, x0, y0, z0, R):
    d = math.sqrt((x-x0)**2 + (y - y0)**2 + (z - z0)**2)
    return d < R
x, y, z = 1, 2, 3
x0, y0, z0 = 0, 0, 0
R = 5
inside=point(x, y, z, x0, y0, z0, R)
print(f"Точка всередині сфери: {inside}")