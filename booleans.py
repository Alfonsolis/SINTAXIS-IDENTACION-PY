v = True
f = False
print("=====================")
print(v)
print(f)
print("=====================")
print(5 > 3) #verdadero
print(3 > 5) #falso
print("=====================")
print(type(v))
print(type(f))
print("=====================")
#Casteo a booleano
print(bool("Hola, mundo")) #verdadero, porque la cadena no está vacía
print(bool(""))     #falso, porque la cadena está vacía

#True
print("=====================")
print(bool("abc"))  #verdadero
print(bool(123))    #verdadero
print(bool(["Manzana", "Pera", "Naranja"]))  #verdadero

#False
print("=====================")
print(bool(0))      #falso
print(bool([]))     #falso
print(bool(""))     #falso
print(bool(None))   #falso

print("=====================")

x = 123
print(isinstance(x, int)) #verdadero

