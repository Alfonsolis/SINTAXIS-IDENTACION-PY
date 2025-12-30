#Funciones. Una función es un bloque de código reutilizable que realiza una tarea específica.

def mi_funcion(): # usando la palabra reservada def para definir una función
    print("¡Hola desde mi función!") # cuerpo de la función

mi_funcion() # llamando a la función para ejecutarla

def saludar(nombre): # función con un parámetro (Argumento)
    print("Hola,", nombre) # cuerpo de la función

saludar("Ana") # llamando a la función con un argumento (Parámetro)
saludar("Luis") # llamando a la función con otro argumento

def saludar_completo(nombre, apellido): # función con múltiples parámetros
    print("Hola,", nombre, apellido) # cuerpo de la función

saludar_completo("Ana", "García") # llamando a la función con dos argumentos
saludar_completo("Luis", "Martínez") # llamando a la función con otros dos argumentos

a = 9
b = 6

def sumar(a, b): # función que suma dos números
    return a + b # devuelve la suma de los dos números

def restar(a, b): # función que resta dos números
    return a - b # devuelve la resta de los dos números

def multiplicar(a, b): # función que multiplica dos números
    return a * b # devuelve la multiplicación de los dos números

def dividir(a, b): # función que divide dos números
    return a / b # devuelve la división de los dos números

resultado = sumar(a, b) # llamando a la función sumar con dos argumentos
print("La suma es:", resultado) # mostrando el resultado de la suma

resultado = restar(a, b) # llamando a la función restar con dos argumentos
print("La resta es:", resultado) # mostrando el resultado de la resta

resultado = multiplicar(a, b) # llamando a la función multiplicar con dos argumentos
print("La multiplicación es:", resultado) # mostrando el resultado de la multiplicación

resultado = dividir(a, b) # llamando a la función dividir con dos argumentos
print("La división es:", resultado) # mostrando el resultado de la división

def funcion_desconocida(): # función sin cuerpo (placeholder)
    pass # la palabra reservada pass indica que no hay implementación aún