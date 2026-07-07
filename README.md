# 🟢 Agente de IA Corporativo - Alura ONE (Cafetería Central)

Este es un asistente inteligente desarrollado como parte del Challenge de la capacitación **ONE (Oracle Next Education) AI for Tech con Alura Latam**. El sistema funciona como una **Base de Conocimiento conversacional centralizada y flexible**, diseñada exclusivamente para que los colaboradores de la empresa puedan resolver dudas operativas, comerciales y de Recursos Humanos en tiempo real a través de una interfaz emulada de WhatsApp.

---

## 📋 Características del Proyecto

El agente fue diseñado aplicando los principios del **Pensamiento Computacional** para resolver la búsqueda de información corporativa sin necesidad de recurrir a estructuras rígidas de comandos.

*   **Procesamiento Multi-Documento y Formato:** El sistema es capaz de clasificar la intención del usuario y extraer información de tres formatos de archivo diferentes:
    *   `datos_empresa.csv` (Área Comercial y Ventas Históricas)
    *   `protocolo_operaciones.txt` (Área Operacional y Normas de Higiene/Seguridad)
    *   `empleados_rh.json` (Área de Recursos Humanos y Gestión de Personal)
*   **Flexibilidad de Consulta:** Cuenta con un normalizador de texto integrado que elimina guiones bajos y conectores. El colaborador puede preguntar de forma natural (ej: *"protocolo de higiene"*, *"normas de higiene"* o *"higiene"*) y el sistema comprenderá la consulta.
*   **Gestión del Personal Integrada:** A diferencia de algoritmos rígidos que se detienen en el primer resultado, la lógica implementada acumula y despliega la totalidad del personal que coincide con un puesto determinado (ej: lista todos los baristas o mozos del turno correspondiente).

---

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3
*   **Entorno de Ejecución:** Google Colab (Infraestructura Cloud)
*   **Control de Versiones:** Git y GitHub utilizando el estándar internacional *Conventional Commits* para el historial evolutivo del código.

---

## 📝 Ejemplos de Consultas y Respuestas

El Agente responde de manera automática según el dominio organizacional de la pregunta:

1.  **Consulta Operacional (.txt):**
    *   *Usuario:* `pasame el protocolo de higiene`
    *   *Agente:* `Protocolo Operacional Activo: El personal debe lavarse las manos cada 30 minutos y usar delantal limpio.`
2.  **Consulta de Recursos Humanos (.json):**
    *   *Usuario:* `puesto de barista`
    *   *Agente:*
        ```text
        Personal registrado en el puesto 'barista':
           • Lucas Martinez (Edad: 26, Turno: Manana)
           • Sofia Rodriguez (Edad: 28, Turno: Tarde)
        ```
3.  **Consulta Comercial (.csv):**
    *   *Usuario:* `horario de atencion`
    *   *Agente:* `Informacion Comercial: El horario de atencion en el mostrador es de lunes a viernes de 9 a 18 horas.`

---

## ☁️ Instrucciones para la Ejecución en la Nube (Google Colab)

Para asegurar la total disponibilidad y compatibilidad del sistema de forma pública en línea, el entorno se encuentra alojado en **Google Colab**.

1.  Acceda al cuaderno del proyecto a través del siguiente enlace público: **[https://colab.research.google.com/drive/1Or34uCpYPFhisAdx1M0sulHuQronK9FY?usp=sharing]**
2.  Haga clic en el botón **Conectar** en la esquina superior derecha para inicializar la máquina virtual.
3.  Presione el botón de **Play** en la celda de código principal. El script creará automáticamente las bases de datos temporales (`.csv`, `.txt`, `.json`) e iniciará la interfaz interactiva.
4.  Interactúe con el bot ingresando consultas desde la consola interna o escriba `salir` para apagar el disparador del servicio.

---

## 📸 Evidencia de Ejecución Cloud

*(A continuación se presenta la captura de pantalla que demuestra el correcto funcionamiento del bot de WhatsApp y la correspondencia multi-documento operando en vivo en la nube)*

<img width="1366" height="768" alt="evidencia_nube" src="https://github.com/user-attachments/assets/2ff71d1b-0418-4998-8ce0-a600d7fa86ce" />
