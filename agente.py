import csv

# 1. FUNCIÓN PARA PROCESAR EL DOCUMENTO
def buscar_en_documento(pregunta_usuario):
    # Abrimos el archivo CSV que creamos antes
    with open('datos_empresa.csv', mode='r', encoding='utf-8') as archivo:
        # Le decimos a Python que lea el archivo como una tabla/diccionario
        lector_csv = csv.DictReader(archivo)
        
        # Recorremos el archivo línea por línea usando un bucle for
        for fila in lector_csv:
            # Comparamos si la pregunta del usuario está dentro de la columna 'pregunta'
            if fila['pregunta'].lower() in pregunta_usuario.lower():
                # Si la encuentra, devuelve (return) la respuesta guardada
                return fila['respuesta']
                
    # Si recorrió todo el archivo y no encontró nada, devuelve este mensaje:
    return "Lo siento, no tengo esa informacion en mis documentos corporativos."

# 2. BUCLE PRINCIPAL DEL AGENTE DE IA
print("=== AGENTE DE IA CORPORATIVO INICIADO ===")
print("Escribe 'salir' para cerrar el asistente.\n")

while True:
    # Pedimos la pregunta al usuario en la terminal
    consulta = input("Tu pregunta: ")
    
    # Condicional para salir del bucle
    if consulta.lower() == "salir":
        print("Cerrando el agente. ¡Hasta luego!")
        break
        
    # Disparador: Llamamos a la función y guardamos el resultado
    respuesta_agente = buscar_en_documento(consulta)
    
    # Mostramos la respuesta en pantalla
    print("Agente:", respuesta_agente)
    print("-" * 40)
