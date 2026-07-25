import csv
import json
import os
import streamlit as st
from google import genai

# ==============================================================================
# 0. LECTURA Y CONSOLIDACIÓN MULTI-FUENTE (CSV, TXT, JSON)
# ==============================================================================
def consolidar_bases_de_datos():
    """
    Carga y consolida la información desde los tres archivos corporativos:
    - datos_empresa.csv (Preguntas Frecuentes / Comercial)
    - protocolo_operaciones.txt (Normas y Protocolos)
    - empleados_rh.json (Nómina y Turnos de Personal)
    """
    contexto = ""

    # 1. Carga de CSV
    if os.path.exists('datos_empresa.csv'):
        contexto += "\n--- FUENTE 1: DATOS COMERCIALES Y FAQ (datos_empresa.csv) ---\n"
        try:
            with open('datos_empresa.csv', mode='r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    contexto += f"Pregunta: {fila.get('pregunta', '')} | Respuesta: {fila.get('respuesta', '')}\n"
        except Exception as e:
            contexto += f"Error al leer CSV: {e}\n"

    # 2. Carga de TXT
    if os.path.exists('protocolo_operaciones.txt'):
        contexto += "\n--- FUENTE 2: PROTOCOLOS OPERATIVOS (protocolo_operaciones.txt) ---\n"
        try:
            with open('protocolo_operaciones.txt', mode='r', encoding='utf-8') as f:
                contexto += f.read() + "\n"
        except Exception as e:
            contexto += f"Error al leer TXT: {e}\n"

    # 3. Carga de JSON
    if os.path.exists('empleados_rh.json'):
        contexto += "\n--- FUENTE 3: NÓMINA DE PERSONAL DE RRHH (empleados_rh.json) ---\n"
        try:
            with open('empleados_rh.json', mode='r', encoding='utf-8') as f:
                datos_json = json.load(f)
                contexto += json.dumps(datos_json, ensure_ascii=False, indent=2) + "\n"
        except Exception as e:
            contexto += f"Error al leer JSON: {e}\n"

    return contexto

base_conocimiento_completa = consolidar_bases_de_datos()

# ==============================================================================
# 1. CONFIGURACIÓN DEL PROMPT DEL SISTEMA (INTERPRETACIONAL Y MULTI-DIALECTAL)
# ==============================================================================
SYSTEM_PROMPT = f"""
Eres un Asistente Virtual Corporativo amigable, extremadamente respetuoso, empático y profesional, diseñado para la Cafetería Central.
Tu misión es atender consultas de clientes, dueños y colaboradores internos.

BASE DE CONOCIMIENTO DISPONIBLE:
{base_conocimiento_completa}

INSTRUCCIONES DE COMPORTAMIENTO Y COMPRENSIÓN MULTI-DIALECTAL:
1. COMPRENSIÓN SEMÁNTICA ABIERTA: Debes comprender la INTENCIÓN detrás de la pregunta sin exigir palabras clave exactas. Adapta tu interpretación a cualquier modismo, regionalismo o dialecto (expresiones de Argentina, Bolivia, Paraguay, Chile, Uruguay, etc.).
2. TONO EDUCADOS Y RESOLUTIVO: Responde siempre con amabilidad, calidez y cortesía.
3. PREGUNTAS AMBIGUAS: Si la pregunta no es totalmente clara pero intuyes sobre qué consulta, responde amablemente y pide con respeto que te confirme o reformule si necesita más detalles.
4. AUSENCIA DE INFORMACIÓN: Si la consulta aborda un tema que NO está contemplado en ninguna de las fuentes de conocimiento, responde de manera muy educada indicando que no posees el registro exacto y sugiere comunicarse directamente con el Departamento de Recursos Humanos o la Administración.
"""

# ==============================================================================
# 2. INTERFAZ DE USUARIO EN STREAMLIT
# ==============================================================================
st.set_page_config(page_title="Chatbot Corporativo - Cafetería", page_icon="☕", layout="centered")

st.title("☕ Asistente Virtual Corporativo")
st.caption("🟢 Canal de Atención e Información Interna - Cafetería Central")

# Inicialización del cliente de Gemini
client = None
try:
    api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if api_key:
        client = genai.Client(api_key=api_key)
    else:
        st.warning("⚠️ Configura GEMINI_API_KEY en st.secrets de Streamlit Cloud.")
except Exception as e:
    st.error(f"Error al inicializar la clave API: {e}")

# Historial de conversación
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {"role": "assistant", "content": "¡Hola! Soy el asistente de la Cafetería Central. ¿En qué puedo ayudarte hoy?"}
    ]

# Renderizar chat
for msg in st.session_state.mensajes:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Entrada de usuario
if consulta := st.chat_input("Escribe tu consulta aquí..."):
    st.session_state.mensajes.append({"role": "user", "content": consulta})
    with st.chat_message("user"):
        st.write(consulta)

    with st.chat_message("assistant"):
        with st.spinner("Procesando consulta en la base de datos..."):
            try:
                if not client:
                    api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
                    client = genai.Client(api_key=api_key)

                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=consulta,
                    config={"system_instruction": SYSTEM_PROMPT}
                )

                respuesta_texto = response.text

                st.markdown(respuesta_texto)
                st.session_state.mensajes.append({"role": "assistant", "content": respuesta_texto})
            except Exception as e:
                st.error("Ocurrió un inconveniente al procesar la solicitud con el modelo de IA.")
