import math
def period(R1, T1, R2) :
    T2 = T1 * math.sqrt((R2**3)/(R1**3))
    return T2
R1 = 1
T1 = 1
R2 = 1.5
T2 = period(R1, T1, R2)
print(f"Період обертання 2 планети: {T2} років")