# ind 012345...
#Un lenguaje de programación inicia a contar desde cero 0 y contará también los espacios
texto = "Esto es un texto"
print(texto[0])  # E
print(texto[5])  # (espacio)
print(texto[11]) # t

# Podemos usar índices negativos para contar desde el final de la cadena
print(texto[-1]) # o

# Podemos usar slicing para obtener subcadenas
print(texto[0:4])  # Esto
#Siempre que hagamos un slicing, el índice final no se incluye, entonces hay que contar uno de más.
print(texto[5:-2]) #s un tex

curso = "Esto es un curso de Javascript, Javascript es un lenguaje de programación"
print(curso.replace("Javascript", "Python")) #Esto es un curso de Python

# Método split

textoDividido = texto.split(" ")
print(textoDividido) #['Esto', 'es', 'un', 'texto ']

# Normalizar mayúsculas y minúsculas
mensaje = "hOlA cÓmO eStÁs?"
print("Hola" in mensaje) # False
print("hola".lower() in mensaje.lower()) # True
