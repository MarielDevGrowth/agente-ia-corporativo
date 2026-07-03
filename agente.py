import csv
import json
import time

# =========================================================
# 1. CAPA VISUAL Y SIMULACIÓN DE WHATSAPP (Formato Estético)
# =========================================================
def mostrar_interfaz_whatsapp():
    print("\n" + "=" * 55)
    print(" 🟢 CHAT DE WHATSAPP CORPORATIVO - CAFETERÍA CENTRAL ".center(55))
    print("       (Canal Interno Exclusivo para Colaboradores)       ".center(55))
    print("=" * 55)
    print("[Bot]: Hola. El disparador de WhatsApp esta activo.")
    print("[Bot]: Escribe tu consulta o 'salir' para finalizar.\n")

def imprimir_mensaje_bot(texto_respuesta):
    print("\n📲 [WhatsApp Bot - Cafeteria]:")
    print(f"   -> \"{texto_respuesta}\"")
    print("-" * 55)

# =========================================================
# 2. CAPA LÓGICA DE BÚSQUEDA (Procesamiento de Documentos)
# =========================================================
def buscar_en_json(consulta):
    with open('empleados_rh.json', mode='r', encoding='utf-8') as archivo:
        datos_empleados = json.load(archivo)
        encontrados = []
        for empleado in datos_empleados:
            if empleado['puesto'] in consulta.lower():
                texto_empleado = f"   • {empleado['nombre']} (Edad: {empleado['edad']}, Turno: {empleado['turno']})"
                encontrados.append(texto_empleado)
        if encontrados:
            return f"Personal registrado en el puesto '{consulta}':\n" + "\n".join(encontrados)
    return "No encontre empleados registrados en ese puesto."

def buscar_en_txt(consulta):
    with open('protocolo_operaciones.txt', mode='r', encoding='utf-8') as archivo:
        for linea in archivo:
            if ":" in linea:
                clave, contenido = linea.split(":", 1)
                clave_limpia = clave.strip().lower().replace("_", " ")
                consulta_limpia = consulta.strip().lower().replace("_", " ")
                if clave_limpia in consulta_limpia or consulta_limpia in clave_limpia or "higiene" in consulta_limpia:
                    return f"Protocolo Operacional Activo: {contenido.strip()}"
    return "Lo siento, ese protocolo o norma no esta registrado en el manual corporativo."

def buscar_en_csv(consulta):
    with open('datos_empresa.csv', mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            if fila['pregunta'].lower() in consulta.lower():
                return f"Informacion Comercial: {fila['respuesta']}"
    return "Lo siento, no tengo esa informacion en mis documentos corporativos actuales."

# =========================================================
# 3. DISPARADOR DE EVENTOS PRINCIPAL (Bucle Activo)
# =========================================================
mostrar_interfaz_whatsapp()

while True:
    # Simula la entrada de un mensaje de texto del empleado
    consulta_usuario = input("📝 Tu Mensaje (Escribe aqui): ")
    
    if consulta_usuario.lower() == "salir":
        print("\n[Bot]: Desconectando el servicio de WhatsApp de la cafeteria... ¡Adios!")
        break
        
    print("\n⏳ [Disparador]: Mensaje recibido. Procesando base de conocimiento...")
    time.sleep(0.5) # Simula un pequeno retraso de procesamiento de la IA
    
    # CLASIFICADOR INTELIGENTE DE ENTRADA
    if any(puesto in consulta_usuario.lower() for puesto in ["empleado", "puesto", "barista", "mozo", "encargado", "maestranza"]):
        respuesta = buscar_en_json(consulta_usuario)
    elif "protocolo" in consulta_usuario.lower() or "norma" in consulta_usuario.lower() or "higiene" in consulta_usuario.lower():
        respuesta = buscar_en_txt(consulta_usuario)
    else:
        respuesta = buscar_en_csv(consulta_usuario)
        
    # Enviamos el resultado a la funcion que da formato de WhatsApp
    imprimir_mensaje_bot(respuesta)
