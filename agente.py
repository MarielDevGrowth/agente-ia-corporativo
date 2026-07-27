import csv
import json
import os
import streamlit as st
from groq import Groq

# ==============================================================================
# 0. LECTURA Y CONSOLIDACIÓN MULTI-FUENTE (CSV, TXT, JSON)
# ==============================================================================
def consolidar_bases_de_datos():
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
# 1. CONFIGURACIÓN DEL PROMPT DEL SISTEMA
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

# Inicialización del cliente de Groq
api_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

if not api_key:
    st.warning("⚠️ Configura GROQ_API_KEY en st.secrets de Streamlit Cloud.")

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
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": consulta}
                    ],
                    temperature=0.3
                )

                respuesta_texto = response.choices[0].message.content

                st.markdown(respuesta_texto)
                st.session_state.mensajes.append({"role": "assistant", "content": respuesta_texto})
            except Exception as e:
                st.error(f"Error detectado: {e}")
