import csv
import json
import time

# =========================================================
# 0. TRUCO AUTOMÁTICO: CREACIÓN DE ARCHIVOS EN LA NUBE
# =========================================================

# 1. Crear el archivo CSV de Atención
contenido_csv = [
    ["pregunta", "respuesta"],
    ["producto mas vendido diciembre 2015", "El producto mas vendido en diciembre de 2015 fue el Smartphone X con 1500 unidades."],
    ["horario de atencion", "El horario de atencion en el mostrador es de lunes a viernes de 9 a 18 horas."]
]
with open('datos_empresa.csv', mode='w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(contenido_csv)

# 2. Crear el archivo TXT de Operaciones
contenido_txt = (
    "protocolo_higiene: El personal debe lavarse las manos cada 30 minutos y usar delantal limpio.\n"
    "protocolo_servicio: La atencion en el mostrador siempre debe iniciar con un saludo amable.\n"
    "norma_seguridad: Ante cualquier falla de las maquinas de cafe, avisar de inmediato al supervisor.\n"
)
with open('protocolo_operaciones.txt', mode='w', encoding='utf-8') as f:
    f.write(contenido_txt)

# 3. Crear el archivo JSON de Recursos Humanos
contenido_json = [
  {"puesto": "encargado", "nombre": "Claudio Fernandez", "edad": 45, "turno": "Manana"},
  {"puesto": "encargado", "nombre": "Patricia Gomez", "edad": 42, "turno": "Tarde"},
  {"puesto": "barista", "nombre": "Lucas Martinez", "edad": 26, "turno": "Manana"},
  {"puesto": "barista", "nombre": "Sofia Rodriguez", "edad": 28, "turno": "Tarde"},
  {"puesto": "mozo", "nombre": "Mateo Silva", "edad": 24, "turno": "Manana"},
  {"puesto": "mozo", "nombre": "Camila Benitez", "edad": 25, "turno": "Manana"},
  {"puesto": "mozo", "nombre": "Bruno Diaz", "edad": 29, "turno": "Tarde"},
  {"puesto": "mozo", "nombre": "Elena Paz", "edad": 27, "turno": "Tarde"},
  {"puesto": "maestranza", "nombre": "Jorge Lopez", "edad": 30, "turno": "Manana"},
  {"puesto": "maestranza", "nombre": "Marta Quiroga", "edad": 26, "turno": "Tarde"}
]
with open('empleados_rh.json', mode='w', encoding='utf-8') as f:
    json.dump(contenido_json, f, indent=2)


# =========================================================
# 1. CAPA VISUAL Y SIMULACIÓN DE WHATSAPP
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
# 2. CAPA LÓGICA DE BÚSQUEDA (Procesamiento Multi-Documento)
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
    consulta_usuario = input("📝 Tu Mensaje (Escribe aqui): ")
    
    if consulta_usuario.lower() == "salir":
        print("\n[Bot]: Desconectando el servicio de WhatsApp de la cafeteria... ¡Adios!")
        break
        
    print("\n⏳ [Disparador]: Mensaje recibido. Procesando base de conocimiento...")
    time.sleep(0.3)
    
    if any(puesto in consulta_usuario.lower() for puesto in ["empleado", "puesto", "barista", "mozo", "encargado", "maestranza"]):
        respuesta = buscar_en_json(consulta_usuario)
    elif "protocolo" in consulta_usuario.lower() or "norma" in consulta_usuario.lower() or "higiene" in consulta_usuario.lower():
        respuesta = buscar_en_txt(consulta_usuario)
    else:
        respuesta = buscar_en_csv(consulta_usuario)
        
    imprimir_mensaje_bot(respuesta)
