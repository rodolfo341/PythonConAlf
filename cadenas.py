# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y 
# un número entero e 
# imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.
"""
nombreUsuario = input("Ingrese nombre usuario: ")
numeroEntero = int(input("Ingrese numero: "))
for i in range(numeroEntero):
    print(f"{i + 1} {nombreUsuario}")
"""

# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y 
# después muestre por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, 
# otra con todas las letras mayúsculas y 
# otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input("Ingrese nombre completo: ")
print(f"nombre: {nombre}")
nombreMinusculas = nombre.lower()
print(f"nombre: {nombreMinusculas}")
nombreMayusculas = nombre.upper()
print(f"nombre: {nombreMayusculas}")


