# 1. UTILIZAR CONCEPTOS FUNDAMENTALES DE PYTHON PARA LA CONSTRUCCIÓN DE PROGRAMAS (VARIABLES/OPERADORES)
# 2. DISTINGUIR TIPOS DE DATOS Y SENTENCIAS BASICAS DEL LENGUAJE PARA LA CONSTRUCCIÓN DE PROGRAMAS (STRING/INT/FLOAT/BOOLEAN)
# TIENDA DE REGALOS CON DESCUENTO ESPECIAL POR CUMPLEAÑOS SEGÚN TU EDAD

print("\n=== ¡Bienvenido a tu Tienda de Regalos favorita+! ===\n")

# PREGUNTAR SI ES TU CUMPLEAÑOS (RESPUESTA "si" O "no")
cumple_input = input("¿Es hoy tu cumpleaños? (si/no): ")

# CONVERTIR LA RESPUESTA A BOOLEANO (TRUE SI RESPONDE "si", FALSE SI NO)
es_cumpleaños = cumple_input.lower() == "si"

# PEDIR PRECIO Y EDAD
precio = float(input("Ingresa el precio total de tu compra: $ "))
edad = int(input("Ingresa tu edad: "))

# CALCULAR PRECIO FINAL APLICANDO DESCUENTO SOLO SI ES CUMPLEAÑOS (TRUE=1, FALSE=0)
precio_final = precio - (precio * edad / 100) * es_cumpleaños

# MOSTRAR RESULTADOS
print("\nPor ser un día tan especial, recibes un descuento!")
print(f"El valor original de tu compra es $ {precio:.0f}")
print(f"Tu descuento es del {edad * es_cumpleaños}%")
print(f"Felicidades! El precio final de tu compra es: $ {precio_final:.0f}\n")


# 3. UTILIZAR SENTENCIAS CONDICIONALES PARA EL CONTROL  DE FLUJO DE UN ALGORITMO QUE RESUELVA UN PROBLEMA (IF/ELIF/ELSE)

# 4. UTILIZAR SENTENCIAS ITERATIVAS PARA LA ELABORACIÓN DE UN ALGORITMO QUE RESUELVA UN PROBLEMA (FOR/WHILE)

# 5. UTILIZAR ESTRUCTURAS DE DATOS PARA LA RESOLUCIÓN DE PROBLEMAS (LISTAS/TUPLAS/DICCIONARIOS)

# 6. UTILIZAR FUNCIONES PARA LA RESOLUCIÓN DE PROBLEMAS (FUNCIONES/RETORNO)
