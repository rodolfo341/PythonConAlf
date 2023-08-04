"""
    Ejercicios de Tipos de Datos Simples
"""

# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
"""print("Hola mundo")"""

# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego 
# muestre por pantalla el contenido de la variable.
"""saludo = "Hola mundo"
print(saludo)"""

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y 
# después de que el usuario lo introduzca muestre por pantalla la cadena 
# ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""nombre = input("Nombre: ")
print(f"¡Hola {nombre}!")"""

# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
# ( ( 3 + 2 ) / ( 2 - 5 ) ) ** 2
"""resultado = ( ( 3 + 2 ) / ( 2 * 5 ) ) ** 2 
print(f"( ( 3 + 2 ) / ( 2 - 5 ) ) ** 2 = {resultado}"""

# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
# el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input("Hoaras trabajadas: "))
valorHora = int(input("Valor por hora: "))
total = horas * valorHora
print(f"tu sueldo es: {total}")





