# Un conjunto (o set) es una colección desordenada de elementos únicos en Python. (No se permiten elementos duplicados y no se puede acceder por índice).

frutas = {"manzana", "banana", "cereza", "manzana"}  # 'manzana' está duplicada
print(frutas)  # Salida: {'manzana', 'banana', 'cereza'} (el duplicado se elimina)
print(type(frutas))  # Salida: <class 'set'>
print(len(frutas))  # Salida: 3

print("banana" in frutas)  # Salida: True
print("naranja" not in frutas)  # Salida: True

# Agregar elementos
# Usamos add() para agregar un solo elemento
frutas.add("naranja")
print(frutas)  # Salida: {'manzana', 'banana', 'cereza', 'naranja'}

# Usamos update() para agregar múltiples elementos
frutas.update(["kiwi", "mango"]) #Se usan corchetes para pasar una lista
print(frutas)  # Salida: {'manzana', 'banana', 'cereza', 'naranja', 'kiwi', 'mango'}

# Otra forma de usar el update:
frutasRaras = {"Carambola", "Pitahaya"}
frutas.update(frutasRaras)
print(frutas)  # Salida: {'manzana', 'banana', 'cereza ', 'naranja', 'kiwi', 'mango', 'Carambola', 'Pitahaya'}

# Eliminar elementos
# Usamos remove() para eliminar un elemento (genera error si el elemento no existe)
frutas.remove("banana")
print(frutas)  # Salida: {'manzana', 'cereza', 'naranja', 'kiwi', 'mango', 'Carambola', 'Pitahaya'}

# Usamos discard() para eliminar un elemento (no genera error si el elemento no existe)
frutas.discard("kiwi")
print(frutas)  # Salida: {'manzana', 'cereza', 'naranja', 'mango', 'Carambola', 'Pitahaya'}

# Usamos pop() para eliminar un elemento aleatorio
frutas.pop()
print(frutas)  # Salida: El conjunto sin un elemento aleatorio

# Usamos clear() para eliminar todos los elementos
frutas.clear()
print(frutas)  # Salida: set()

print("====================================")
conjuntos = {"Python", 42, 3.14, True}
print(conjuntos)  # Salida: {'Python', 42, 3.14, True}
print(type(conjuntos))  # Salida: <class 'set'>

for item in conjuntos:
    print(item)  # Imprime cada elemento del conjunto (el orden puede variar)

print("====================================")

# Operaciones de conjuntos
A = {"a", "b", "c"}
B = {"c", "d", "e"}

# Unión
union = A.union(B)
print("Unión:", union)  # Salida: Unión: {'a', 'b', 'c', 'd', 'e'}

# Intersección
interseccion = A.intersection(B)
print("Intersección:", interseccion)  # Salida: Intersección: {'c'}

# Diferencia
diferencia = A.difference(B)
print("Diferencia (A - B):", diferencia)  # Salida: Diferencia (A - B): {'a', 'b'}