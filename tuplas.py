# Las tuplas, tambien conocidas como "tuples" en inglés, son estructuras de datos en Python que permiten almacenar múltiples elementos en una sola variable.
# A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.

# Indice
tecnologias = ("Python", "Java", "C++", "Python")  # Creación de una tupla. Permite elementos duplicados.
print(tecnologias)  # Salida: ('Python', 'Java', 'C++')
print(tecnologias[1])  # Salida: Java

print(len(tecnologias))  # Salida: 4

print(type(tecnologias))  # Salida: <class 'tuple'>

fruta = ("Manzana")  # Tupla con un solo elemento, se necesita la coma al final.
print(type(fruta))  # Salida: <class 'str'> Porque no tiene la coma.


tupla = ("Mandarina", 5 , 3.14, True)  # Tupla con diferentes tipos de datos.
print(tupla)  # Salida: ('Mandarina', 5, 3.14, True)
print(type(tupla))  # Salida: <class 'tuple'>

# Desempaquetado de tuplas
x, y, z, w = tupla
print(x)  # Salida: Mandarina
print(y)  # Salida: 5
print(z)  # Salida: 3.14
print(w)  # Salida: True

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2  # Concatenación de tuplas
print(tupla3)  # Salida: (1, 2, 3, 4, 5, 6)

print(tupla * 2)  # Repetición de tupla. Salida: ('Mandarina', 5, 3.14, True, 'Mandarina', 5, 3.14, True)

for item in tupla:
    print(item)  # Iteración sobre los elementos de la tupla

print("============")
#Truco para modificar una tupla

tupla_a_modificar = ("A", "B", "C")
lista_temporal = list(tupla_a_modificar)  # Convertir la tupla a una lista
lista_temporal.append("D")  # Modificar la lista
tupla_a_modificar = tuple(lista_temporal)  # Convertir la lista de nuevo a una tupla
print(tupla_a_modificar)  # Salida: ('A', 'B', 'C', 'D')

