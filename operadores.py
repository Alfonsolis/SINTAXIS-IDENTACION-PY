#Operadores aritméticos

x = 5
y = 10

#Suma
print("Suma:", x + y)

#Resta
print("Resta:", x - y)

#Multiplicación
print("Multiplicación:", x * y)

#División / (resultado float)
print("División:", x / y)

#Módulo % (resto de la división)
print("Módulo:", x % y)
par = 10
print(par % 2 == 0) # True, porque 10 es par

#Exponente **
print("Exponente:", x ** 2) # 5^2 = 25
print("Exponente:", y ** 3) # 10^3 = 1000
print("Exponente:", x ** y) # 5^10 = 9765625
print("Exponente:", y ** x) # 10^5 = 100000

#División entera //
print("División entera:", y // x) # 10 // 5 = 2
print("División entera:", x // y) # 5 // 10 = 0
print("División entera:", 15 // 4) # 15 // 4 = 3
print("División entera:", 14 // 4) # 14 // 4 = 3

#Jerarquía de operadores

# Parentesis
# Exponentes
# Multiplicación, División, Módulo, División entera
# Suma, Resta
# Comparaciones de identidad y pertenencia
# Logicos
