# ☕ Agente Virtual Corporativo - Cafetería Central

Este proyecto consiste en el desarrollo de un **Agente Virtual Inteligente** integrado con **Google Generative AI (Gemini 1.5 Flash)** y **Streamlit**, diseñado para actuar como canal de atención tanto para clientes externos como para personal interno (RRHH y Operaciones) de una cafetería.

El agente destaca por su capacidad de **comprensión semántica multi-dialectal**, permitiendo interpretar consultas en diversos regionalismos y modismos de Latinoamérica sin exigir coincidencias exactas de texto.

---

## 🛠️ Arquitectura y Fuentes de Datos (Multi-Fuente)

El sistema procesa y consolida información en tiempo real desde tres fuentes independientes ubicadas en el repositorio:

1. **`datos_empresa.csv`**: Base de conocimientos de preguntas frecuentes comerciales y de atención al cliente.
2. **`protocolo_operaciones.txt`**: Manual de procedimientos operativos, normas de higiene, seguridad y políticas internas de ausencias y licencias.
3. **`empleados_rh.json`**: Registro estructurado de la nómina de personal, roles, turnos de trabajo y días de vacaciones.

---

## 🚀 Características Principales

* **Interpretación Semántica:** Capacidad de entender el contexto e intención del usuario (soporta variaciones dialectales y expresiones regionales).
* **Flexibilidad Operativa:** Respuesta a protocolos de salud (aviso de ausencias dentro de las primeras 3 horas y certificado médico con alta), fechas de cobro de aguinaldo (SAC) y asignación de turnos.
* **Interfaz Gráfica Interactiva:** Desplegado con Streamlit para ofrecer una experiencia limpia e intuitiva tipo chat.
* **Manejo de Respuestas Ambiguas o No Registradas:** Solicitud cordial de reformulación en preguntas no claras y derivación automática al área de Recursos Humanos ante falta de información.

---

## 🔧 Instalación y Ejecución Local

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/MarielDevGrowth/agente-ia-corporativo.git](https://github.com/MarielDevGrowth/agente-ia-corporativo.git)
   cd agente-ia-corporativo
