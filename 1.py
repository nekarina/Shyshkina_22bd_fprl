import math
T1 = float(input("Enter T1: "))
R1 = float(input("Enter R1: "))
R2 = float(input("Enter R2: "))
T2 = T1 * math.sqrt((R2**3)/(R1**3))
print(f"Період обертання 2 планети: ", T2)
