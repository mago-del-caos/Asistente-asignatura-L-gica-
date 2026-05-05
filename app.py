import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="📐 Jared-Lógica | Planeación de Lógica",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

# CSS MEJORADO
css_jared = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stDecoration"] {display: none;}
    .stDeployButton {display: none;}
    [data-testid="stToolbar"] {display: none;}
    
    .stApp {
        background: linear-gradient(135deg, #0a0a2a 0%, #1a1a3a 50%, #0d0d2b 100%);
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #2E7D32, #1B5E20);
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 30px;
        border: 2px solid #FFD700;
    }
    
    .main-header h1 {
        color: #FFD700;
        margin: 0;
        text-shadow: 2px 2px 0 #0a0a2a;
    }
    
    .main-header p {
        color: #E8F5E9;
        margin: 5px 0 0;
    }
    
    .unidad-card {
        background: rgba(25, 25, 45, 0.95);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        border-left: 5px solid #2E7D32;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .stButton button {
        background: linear-gradient(135deg, #2E7D32, #1B5E20);
        color: #FFD700;
        font-weight: bold;
        border-radius: 30px;
        border: none;
        transition: transform 0.2s;
    }
    
    .stButton button:hover {
        transform: scale(1.02);
        background: linear-gradient(135deg, #388E3C, #2E7D32);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #0a0a2a 0%, #1a1a3a 100%);
        border-right: 2px solid #2E7D32;
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #FFD700;
    }
    
    .info-box {
        background: rgba(46, 125, 50, 0.2);
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #2E7D32;
    }
    
    hr {
        border-color: #2E7D32;
    }
</style>
"""
st.markdown(css_jared, unsafe_allow_html=True)

# ENCABEZADO
st.markdown("""
<div class="main-header">
    <h1>📐 Jared-Lógica</h1>
    <p>✨ Especialista en Planeación de Lógica · Argumentación · Pensamiento Crítico ✨</p>
    <p style="font-size: 0.9em;">Basado en Taxonomía de Marzano · Enfoque en habilidades argumentativas</p>
</div>
""", unsafe_allow_html=True)

# BASE DE CONOCIMIENTO DEL CURSO - PROMPT COMPLETO
SYSTEM_PROMPT = """Eres JARED-LÓGICA, un experto en planeación didáctica de la asignatura de Lógica. Toda tu labor se basa en el siguiente programa de estudios:

**FUNDAMENTACIÓN DEL CURSO:**
El curso tiene como objetivo fundamental privilegiar el desarrollo de habilidades lógicas para la argumentación, el diálogo, el análisis de la información y la solución de problemas, habilidades necesarias para la construcción de saberes tanto en el ámbito de las humanidades como el de las ciencias exactas, asimismo, para la búsqueda y construcción de acuerdos en la vida pública.

El enfoque que guía la enseñanza de esta asignatura es el desarrollo de las habilidades básicas argumentativas que un estudiante egresado de bachillerato debe poseer: analizar, comprender, refutar, distinguir, construir, evaluar y reconstruir discursos argumentativos (orales y escritos) en distintos ámbitos del saber, con el fin de dar orden y estructura a su pensamiento y, con ello, posibilitar la búsqueda de posibles alternativas de solución a problemas de su vida personal, académica y colectiva, de manera racional.

**OBJETIVO GENERAL:**
El alumno aplicará las habilidades lógicas, incluidas aquellas del pensamiento crítico y dialógico, en la toma de decisiones de la vida cotidiana que le permitan enfrentarse a los problemas de su entorno (natural, social, cultural, político, personal, entre otros). Asimismo, empleará dichas habilidades en la elaboración de saberes referidos a los ámbitos científicos y humanísticos a partir de la reflexión, el análisis, la identificación de argumentos –orales y escritos–, su construcción, reconstrucción y evaluación. De la misma forma pondrá en práctica la argumentación a través del diálogo razonado para propiciar actitudes y valores propios de una sociedad participativa.

**UNIDADES Y HORAS:**
- Unidad 1. El horizonte de la lógica - 10 horas
- Unidad 2. Las rutas del argumento - 20 horas
- Unidad 3. Para ordenar el razonamiento: lógica deductiva - 15 horas
- Unidad 4. Armando y desarmando argumentos - 15 horas
- Unidad 5. De argumentos engañosos y cosas peores - 10 horas
- Unidad 6. La lógica en acción - 20 horas

**CONTENIDOS POR UNIDAD:**

UNIDAD 1. El horizonte de la lógica (10 horas)
Objetivos: Diferenciará las funciones del lenguaje, Conocerá algunos tipos de lógica
Contenidos conceptuales: Funciones del lenguaje (informativa, expresiva, directiva), La Lógica como ciencia o arte, Tipos de lógica (deductivas e inductivas)
Contenidos procedimentales: Análisis de discursos, Identificación del uso de la lógica
Contenidos actitudinales: Valoración del estudio de la lógica

UNIDAD 2. Las rutas del argumento (20 horas)
Objetivos: Reconocer elementos del argumento, Identificar tipos de argumentos (deductivo, inductivo, analógico, abductivo)
Contenidos conceptuales: Concepto, proposición, premisas, conclusión; Clasificación de argumentos
Contenidos procedimentales: Análisis de argumentos en textos reales, Distinción de problemas científicos y sociales
Contenidos actitudinales: Valoración de postura racional y crítica

UNIDAD 3. Para ordenar el razonamiento: lógica deductiva (15 horas)
Objetivos: Expresar argumentos con símbolos lógicos, Demostrar validez mediante deducción natural y tablas de verdad
Contenidos conceptuales: Formalización, Conectivas lógicas, Reglas de inferencia (Modus Ponens, Modus Tollens, Silogismo Disyuntivo, Silogismo Hipotético, Doble negación, De Morgan, Conjunción, Adición, Simplificación, Conmutación)
Contenidos procedimentales: Traducción lenguaje natural a simbólico, Pruebas de validez

UNIDAD 4. Armando y desarmando argumentos (15 horas)
Objetivos: Describir elementos, supuestos, intenciones e implicaciones; Desarrollar análisis y síntesis
Contenidos conceptuales: Tema, tesis, ideas secundarias; Supuestos, intenciones (demostrar, convencer, denostar); Modelos de reconstrucción; Partes del escrito argumentativo
Contenidos procedimentales: Identificación de elementos, Análisis de supuestos, Reconstrucción de argumentos, Planeación de escrito argumentativo

UNIDAD 5. De argumentos engañosos y cosas peores (10 horas)
Objetivos: Caracterizar falacias y estratagemas para reconocerlas
Contenidos conceptuales: Definición, finalidad y tipos de falacia; Falacias informales
Contenidos procedimentales: Identificación de falacias en discursos reales

UNIDAD 6. La lógica en acción (20 horas)
Objetivos: Elaborar argumentación oral y escrita; Comprender la práctica dialógica
Contenidos conceptuales: Esquemas argumentativos (Weston, Toulmin, Perelman, van Eemeren); Tipos de diálogo (mayéutico, indagación, negociación); Elementos de diálogos argumentativos
Contenidos procedimentales: Elaboración de argumentación, Uso de modelos dialógicos, Debate basado en diálogo argumentativo

**SUGERENCIAS DE TRABAJO:**
- Trabajo colaborativo
- Recursos digitales (infografías, prezi, videos, podcasts)
- Escritos argumentativos
- Comunidad de investigación (Mathew Lipman)
- Análisis de textos reales
- Casos reales de toma de decisiones

**TAXONOMÍA DE MARZANO (para estructurar objetivos):**
Nivel 1: Recuperación (identificar, recordar, ejecutar)
Nivel 2: Comprensión (integrar, simbolizar, parafrasear)
Nivel 3: Análisis (comparar, clasificar, analizar errores, generalizar)
Nivel 4: Utilización (resolver problemas, experimentar, investigar)

**ESTRUCTURA DE SESIÓN (Inicio-Desarrollo-Cierre):**
- INICIO (15%): Activación, preguntas detonadoras, recuperación de saberes
- DESARROLLO (70%): Actividades principales centradas en el estudiante
- CIERRE (15%): Síntesis, metacognición, evaluación

**REGLAS PARA PLANEAR:**
1. Preguntar al usuario: ¿Qué UNIDAD? ¿Cuántas HORAS? ¿NIVEL?
2. Alinear actividades con niveles de Marzano
3. Actividades centradas en el ESTUDIANTE
4. Ofrecer RÚBRICAS cuando se solicite
5. Usar ejemplos de problemas reales del entorno (cambio climático, sustentabilidad, diversidad cultural, tecnología, etc.)

Responde siempre basándote en este programa. Ofrece planeaciones detalladas, con objetivos claros y actividades prácticas."""

# CONEXIÓN CON GROQ
try:
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=st.secrets["GROQ_API_KEY"]
    )
except KeyError:
    st.error("📐 ¡Error! No se encontró GROQ_API_KEY")
    st.info("Configura en Secrets: GROQ_API_KEY = 'tu_api_key'")
    st.stop()
except Exception as e:
    st.error(f"Error de conexión: {str(e)}")
    st.stop()

# FUNCIÓN DE VOZ
def speak_js(text):
    clean_text = text.replace("'", "\\'").replace('"', '\\"').replace("\n", " ")[:500]
    js_code = f"""
    <script>
        var text = "{clean_text}";
        function hablar() {{
            var utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'es-MX';
            utterance.rate = 0.9;
            utterance.pitch = 1.0;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(utterance);
        }}
        setTimeout(hablar, 100);
    </script>
    """
    components.html(js_code, height=0)

# HISTORIAL
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_response" not in st.session_state:
    st.session_state.last_response = ""

# SIDEBAR - SELECCIÓN DE UNIDAD
with st.sidebar:
    st.markdown("## 📚 Unidades del Curso")
    st.markdown("---")
    
    unidad_seleccionada = st.selectbox(
        "Selecciona una unidad para planear:",
        [
            "Unidad 1. El horizonte de la lógica (10 horas)",
            "Unidad 2. Las rutas del argumento (20 horas)",
            "Unidad 3. Para ordenar el razonamiento: lógica deductiva (15 horas)",
            "Unidad 4. Armando y desarmando argumentos (15 horas)",
            "Unidad 5. De argumentos engañosos y cosas peores (10 horas)",
            "Unidad 6. La lógica en acción (20 horas)"
        ]
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Opciones de planeación")
    
    tipo_planeacion = st.radio(
        "¿Qué tipo de planeación necesitas?",
        ["📋 Planeación completa de unidad", "🎯 Solo objetivos", "📝 Actividades para una sesión", "📊 Rúbricas de evaluación"]
    )
    
    horas_sesion = st.selectbox("⏱️ Duración por sesión (horas)", [1, 2, 3], index=1)
    
    incluir_rubricas = st.checkbox("✅ Incluir rúbricas", value=True)
    
    st.markdown("---")
    
    if st.button("🚀 Generar planeación", use_container_width=True):
        unidad_info = unidad_seleccionada.split("(")[0].strip()
        horas = unidad_seleccionada.split("(")[1].replace(")", "")
        
        if tipo_planeacion == "📋 Planeación completa de unidad":
            prompt = f"""Necesito una PLANEACIÓN COMPLETA para:
- {unidad_info}
- Horas totales: {horas}
- Duración por sesión: {horas_sesion} horas

Basada ESTRICTAMENTE en el programa de estudios proporcionado.
Incluye:
1. Objetivos (conceptuales, procedimentales, actitudinales) alineados a Taxonomía de Marzano
2. División en sesiones con Inicio-Desarrollo-Cierre
3. Actividades centradas en el estudiante
4. Alternativas de actividad
{f'5. Rúbricas de evaluación' if incluir_rubricas else ''}

Usa ejemplos de problemas reales del entorno."""
        elif tipo_planeacion == "🎯 Solo objetivos":
            prompt = f"""Genera solo los OBJETIVOS para {unidad_info}:
- Objetivos CONCEPTUALES (Saber)
- Objetivos PROCEDIMENTALES (Saber hacer)
- Objetivos ACTITUDINALES (Ser)
Alineados a los niveles de la Taxonomía de Marzano."""
        elif tipo_planeacion == "📝 Actividades para una sesión":
            prompt = f"""Diseña UNA SESIÓN de {horas_sesion} horas para {unidad_info}:
- INICIO (15%): Actividad de activación
- DESARROLLO (70%): Actividad principal centrada en el estudiante
- CIERRE (15%): Síntesis y metacognición
Incluye el nivel de Marzano que se trabaja."""
        else:
            prompt = f"""Genera RÚBRICAS de evaluación para {unidad_info}:
- Criterios de evaluación
- Niveles de desempeño (Excelente, Satisfactorio, Básico, Insuficiente)
- Indicadores específicos
Basadas en los contenidos del programa."""
        
        procesar_respuesta(prompt)

# MOSTRAR CHAT
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# FUNCIÓN PARA PROCESAR RESPUESTA
def procesar_respuesta(user_input):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("assistant"):
        with st.spinner("📐 Jared-Lógica está planeando..."):
            try:
                mensajes_api = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages[-15:]
                stream = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=mensajes_api,
                    stream=True,
                    temperature=0.7,
                )
                response = st.write_stream(stream)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.last_response = response
            except Exception as e:
                st.error(f"Error: {str(e)}")

# CHAT INPUT
if prompt := st.chat_input("Escribe tu consulta sobre planeación de Lógica... Ej: 'Planea la Unidad 2 completa', 'Objetivos de la Unidad 3', 'Actividad para falacias'"):
    procesar_respuesta(prompt)

# BOTONES RÁPIDOS
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("📋 Unidad 1", use_container_width=True):
        procesar_respuesta("Planea la Unidad 1 'El horizonte de la lógica' completa, con objetivos, actividades centradas en estudiantes y estructura Inicio-Desarrollo-Cierre")
with col2:
    if st.button("🛤️ Unidad 2", use_container_width=True):
        procesar_respuesta("Planea la Unidad 2 'Las rutas del argumento' completa, con énfasis en identificación de argumentos deductivos, inductivos, analógicos y abductivos")
with col3:
    if st.button("📊 Unidad 3", use_container_width=True):
        procesar_respuesta("Planea la Unidad 3 'Para ordenar el razonamiento: lógica deductiva' con actividades prácticas sobre tablas de verdad y reglas de inferencia")
with col4:
    if st.button("🔧 Unidad 4", use_container_width=True):
        procesar_respuesta("Planea la Unidad 4 'Armando y desarmando argumentos' con enfoque en reconstrucción de argumentos usando diagramas")
with col5:
    if st.button("⚠️ Unidad 5", use_container_width=True):
        procesar_respuesta("Planea la Unidad 5 'De argumentos engañosos y cosas peores' con ejemplos de falacias en medios de comunicación")

# SEGUNDA FILA DE BOTONES
col6, col7, col8, col9, col10 = st.columns(5)
with col6:
    if st.button("🎯 Unidad 6", use_container_width=True):
        procesar_respuesta("Planea la Unidad 6 'La lógica en acción' con un debate como actividad final usando esquemas de Toulmin o Weston")
with col7:
    if st.button("📝 Rúbricas", use_container_width=True):
        procesar_respuesta("Genera una rúbrica de evaluación para evaluar un debate o texto argumentativo en la Unidad 6")
with col8:
    if st.button("💡 Consejos Marzano", use_container_width=True):
        procesar_respuesta("Explica cómo aplicar los 4 niveles de la Taxonomía de Marzano en la planeación de Lógica con ejemplos concretos")
with col9:
    if st.button("🔊 Escuchar", use_container_width=True):
        if st.session_state.last_response:
            speak_js(st.session_state.last_response)
with col10:
    if st.button("🔄 Nueva", use_container_width=True):
        st.session_state.messages = []
        st.session_state.last_response = ""
        st.rerun()

# INFO EN SIDEBAR
with st.sidebar:
    st.markdown("---")
    st.markdown("### 💡 Sobre Jared-Lógica")
    st.markdown("""
    **Basado en el programa oficial de Lógica**
    
    **Habilidades que desarrolla:**
    - Analizar y comprender argumentos
    - Refutar y distinguir discursos
    - Construir y evaluar argumentos
    - Reconstruir argumentaciones
    
    **Valores que fomenta:**
    - Respeto y honestidad intelectual
    - Tolerancia y capacidad de escucha
    - Pensamiento crítico y autónomo
    
    **Enfoque:** Taxonomía de Marzano
    **Metodología:** Inicio-Desarrollo-Cierre
    """)
    
    st.markdown("---")
    st.markdown("### 📖 Fuentes de referencia")
    st.markdown("""
    - Copi & Cohen - Introducción a la lógica
    - Weston - Las claves de la argumentación
    - Toulmin - Los usos de la argumentación
    - Lipman - Filosofía en el aula
    """)
