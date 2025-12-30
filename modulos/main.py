# Modulos. Los módulos en Python son archivos que contienen definiciones y declaraciones de Python.
# Se utilizan para organizar y reutilizar el código en diferentes partes de un programa o en diferentes
# proyectos. Un módulo puede contener funciones, clases y variables, y se puede importar en otros
# archivos para utilizar su funcionalidad.  

# import operaciones                    # Importa el módulo operaciones
# print(operaciones.sumar(5, 3))        # Llama a la función sumar del módulo operaciones
# print(operaciones.restar(10, 4))      # Llama a la función restar del módulo operaciones
# print(operaciones.multiplicar(2, 6))  # Llama a la función multiplicar del módulo operaciones
# print(operaciones.dividir(8, 2))      # Llama a la función dividir del módulo operaciones

# Para dejar de llamar tanto a operaciones.sumar, operaciones.restar, etc., podemos importar
# las funciones específicas del módulo operaciones de la siguiente manera:

from operaciones import sumar, restar, multiplicar, dividir  # Importa funciones específicas del módulo operaciones
print(sumar(7, 2))        # Llama a la función sumar directamente
print(restar(15, 5))      # Llama a la función restar directamente
print(multiplicar(3, 4))  # Llama a la función multiplicar directamente
print(dividir(9, 3))      # Llama a la función dividir directamente
