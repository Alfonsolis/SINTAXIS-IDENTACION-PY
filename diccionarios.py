# Coleccion de pares clave-valor

auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

auto_clasico = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1967,
    "color": "Rojo",
    "transmisión": "Manual"
}
print(auto) # {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2020}
print(auto["marca"]) # Toyota
print(auto.get("modelo")) # Corolla

print(auto.keys()) # dict_keys(['marca', 'modelo', 'año'])
print(auto.values()) # dict_values(['Toyota', 'Corolla', 2020])

if "marca" in auto:
    print("La clave 'marca' existe en el diccionario.")

auto["año"] = 2025
print(auto) # {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2025}

auto["color"] = "Rojo"
print(auto) # {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2025, 'color': 'Rojo'}

auto.update({"año": 2023})
auto.update({"color": "Azul"})
print(auto) # {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2023, 'color': 'Azul'}

# Eliminar elementos
auto.pop("modelo") # Elimina el par clave-valor con clave 'modelo'
print(auto) # {'marca': 'Toyota', 'año': 2023, 'color': 'Azul'}

auto.popitem() # Elimina el último par clave-valor agregado
print(auto) # {'marca': 'Toyota', 'año': 2023}

auto.clear() # Elimina todos los elementos del diccionario
print(auto) # {}

print("================================")

for k in auto_clasico:
    print(k) # Itera sobre las claves del diccionario

print("----")

for v in auto_clasico.values():
    print(v) # Itera sobre los valores del diccionario

print("----")

for k, v in auto_clasico.items():
    print(k,v) # Itera sobre los pares clave-valor del diccionario

# Diccionarios anidados

familia = {
    "hijo1" : {
        "nombre" : "Pedro",
        "edad" : 9,
    },
    "hijo2" : {
        "nombre" : "Ana",
        "edad" : 7,
    },
    "hijo3" : {
        "nombre" : "Miguel",
        "edad" : 12,
    }
}

print(familia["hijo1"]["nombre"]) # Pedro