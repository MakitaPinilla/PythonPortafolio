# 6. UTILIZAR FUNCIONES PARA LA RESOLUCIÓN DE PROBLEMAS (FUNCIONES/RETORNO)

# FUNCIÓN QUE PREGUNTA Y VALIDA SI ES CUMPLEAÑOS
def pedir_respuesta_cumple():
    respuesta = input("¿ES HOY TU CUMPLEAÑOS? (si/no): ").lower()
    while respuesta != "si" and respuesta != "no":
        print("POR FAVOR RESPONDE SOLO CON 'si' O 'no'")
        respuesta = input("¿ES HOY TU CUMPLEAÑOS? (si/no): ").lower()
    return respuesta == "si"
