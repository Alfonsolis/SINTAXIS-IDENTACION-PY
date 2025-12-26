"""
Listas.
Recordemos que las listas son coelecciones ordenadas, 
mutables y permiten elementos duplicados.
Podemos crear listas utilizando corchetes [] y separando los elementos con comas.
Ejemplo:
mi_lista = [1, 2, 3, 4, 5]
"""
print("===PRIMERA LISTA===")
frutas = ["Manzana", "Naranja", "Mandarina"] # indices por fruta: 0, 1, 2
print(frutas) # Imprimir la lista completa
print(type(frutas)) # Verificar el tipo de dato
print(frutas[1])  # Acceder al segundo elemento (Naranja)
frutas[0] = "Pera"  # Modificar el primer elemento
print(frutas) # Imprimir la lista modificada
print(len(frutas))  # Obtener la longitud de la lista

print("===SEGUNDA LISTA===")

frutas2 = ["Banana", "Kiwi", "Cereza", "Cereza"] # Lista con elemento duplicado
print(frutas2) # Imprimir la segunda lista
print(type(frutas2)) # Verificar el tipo de dato
print(frutas2[2])  # Acceder al tercer elemento (Cereza)
frutas2[1] = "Uva"  # Modificar el segundo elemento
print(frutas2) # Imprimir la lista modificada
print(len(frutas2))  # Obtener la longitud de la lista

print("===TERCERA LISTA===")

lista = [10, "Hola", 3.14, True] # Lista con diferentes tipos de datos
print(lista) # Imprimir la tercera lista
print(type(lista)) # Verificar el tipo de dato
print(len(lista))  # Obtener la longitud de la lista

print("===OPERACIONES COMUNES===")
print(frutas[0:2])  # Slicing: Obtener los dos primeros elementos de la primera lista
if "Cereza" in frutas2:
    print("Cereza está en la lista frutas2")  # Verificar si "Cereza" está en la segunda lista


print("===LISTA VEHICULOS===")

vehiculos = ["Auto", "Moto", "Camioneta"]
#Metodo append(): Agrega un elemento al final de la lista
vehiculos.append("Bicicleta")
print(vehiculos)

#Metodo insert(): Agrega un elemento en una posicion especifica
vehiculos.insert(1, "Camion")
print(vehiculos)

#Metodo remove(): Elimina un elemento especifico de la lista
vehiculos.remove("Moto")
print(vehiculos)

#Metodo pop(): Elimina el ultimo elemento de la lista y lo devuelve
vehiculos.pop(1) # Elimina el elemento en la posicion 1
print(vehiculos)

#Metodo sort(): Ordena los elementos de la lista
vehiculos.sort()
print(vehiculos) # Imprime la lista ordenada

#Metodo reverse(): Invierte el orden de los elementos en la lista
vehiculos.reverse()
print(vehiculos) # Imprime la lista en orden inverso

#Unir dos listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3) # Imprime la lista unida

coleccion1.extend(coleccion2)
print(coleccion1) # Imprime la lista extendida