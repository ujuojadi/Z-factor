# "NAME: JESSICA OBIANUJU OJADI "
# "LINKEDIN NAME: JESSICA OJADI"
# "LINKEDIN URL: https://www.linkedin.com/in/jessica-ojadi-6b1877118"


from math import exp

pressure= float(input("Enter the value of pressure: "))
sgravity= float(input("Enter the value of specific gravity: "))
temp= float(input("Enter the value of Temperature: "))
temp = 460 + temp
print(f"temp = {temp} R")

Ppc = 677 + (15.0 * (sgravity)) -(37.5 * (sgravity **2))
Tpc = 168+ (325 * (sgravity)) - (12.5 *(sgravity ** 2))
print(f"Ppc = {Ppc}")
print(f"Tpc = {Tpc}")

Ppr = round(pressure / Ppc, 3)
Tpr = round(temp / Tpc, 3)
t = 1/Tpr

print(f"Ppr = {Ppr}")
print(f"Tpr = {Tpr}")
print(f"t =  {t}")

aA = (-0.06125 *(Ppr) * t )* (exp((-1.2) *((1-t) ** 2)))
bB = (14.76 * t) - (9.76 * (t **2)) + (4.58 * (t **3))
cC = (90.7 * t) - (242.2 * (t**2)) + (42.4 * (t**3))
dD = 2.18 +(2.82 * t) 


Yk = (0.0125 * Ppr * t) * (exp(-1.2) * ((1-t)**2))
print(f"Yk = {Yk}")

def looped(Ppr, t, aA, bB, cC, dD, Yk):
	Yk
	for i in range(0, 5000000000):
		one = (Yk + (Yk ** 2) + (Yk ** 3) - (Yk ** 4))/ ((1 - Yk) **3)
		two = bB * (Yk ** 2)
		three = cC * (Yk ** dD)
		F1 = aA + one - two + three
		ones = 1 + (4 * Yk) + (4 * (Yk ** 2)) - (4 * (Yk ** 3)) +(Yk ** 4)
		twos = ((1- Yk) **4)
		threes = 2 * bB * Yk
		fours = cC * dD * (Yk **(dD-1))
		F2 = (ones/twos) - threes + fours 
		Yk2 = Yk -(F1/F2)
		if  abs(Yk -Yk2)< (10**-12):
			return Yk
		else:
			Yk = Yk2

			


FinalYk = looped(Ppr, t, aA, bB, cC, dD, Yk)
print(f"Y = {FinalYk}")

z = ((0.06125 * t * Ppr)/ FinalYk)* (exp((-1.2) *((1-t) ** 2)))
print(f"Compressibility Factor z = {z}")























# Fy2 =  ((1 + (4 * Yk) + (4 * (Yk **2)) - (4 * (Yk ** 3)) + (Yk ** 4))/((1 - Yk) **4)) - (2* bB * Yk ) + (cC * dD * (Yk **(dD -1)))
# print(Fy1)