
"""  Ejercicios de Tipos de Datos Simples   """

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
"""horas = int(input("Hoaras trabajadas: "))
valorHora = int(input("Valor por hora: "))
total = horas * valorHora
print(f"tu sueldo es: {total}")"""

# Ejercicio 6
# Escribir un programa que lea un entero positivo introducido por el usuario y después 
# muestre en pantalla la suma de todos los enteros desde 1 hasta n 
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# ( n ( n + 1 ) ) / 2
"""n = int(input("ingrese n: "))
suma = ( n * ( n + 1 ) ) // 2
print(f"La suma de los {n} numeros positivos es: {suma}")"""

# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros)
# calcule el índice de masa corporal y lo almacene en una variable muestre por pantalla la frase 
# Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
# calculado redondeado con dos decimales.
"""peso = float(input("peso: "))
estatura = float(input("estatura: "))
IMC = round(peso / (estatura) ** 2, 2)
print(f"Tu índice de masa corporal es {IMC}")"""

# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros
# muestre por pantalla el cociente y el resto.
"""num1 = float(input("ingrese num1: "))
num2 = float(input("ingrese num2: "))
cociente = round(num1 / num2, 2)
resto = int(num1 % num2)
print(f"cociente de {num1} / {num2} = {cociente}")
print(f"el resto de {num1} % {num2} = {resto}")"""

# Ejercicio 9
# Escribir un programa que pregunte al usuario una:
#           .- cantidad a invertir
#           .- el interés anual y 
#           .- el número de años, y 
# 
# muestre por pantalla el capital obtenido en la inversión. 
"""inversion = float(input("inversion: "))
interesAnual = float(input("Interes anual: "))
aniosDeInversion = int(input("Años de inversion: "))
A = inversion * ( 1 + interesAnual / 100 ) ** ( aniosDeInversion )
print(f"Capital obtenido = {round(A)}")"""

# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: 
#               .- payasos y 
#               .- muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""pesoPayaso = 112
pesoMuñeca = 75
payasos = int(input("cantidad de payasos: "))
muñecas = int(input("cantidad de muñecas: "))
pesoTotal = pesoPayaso * payasos + pesoMuñeca * muñecas
print(f"el peso total es de: {pesoTotal}")"""

# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
# la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.









