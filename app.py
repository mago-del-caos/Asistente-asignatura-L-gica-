import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components

# CONFIGURACIÓN DE PÁGINA - OPTIMIZADA PARA MÓVIL
st.set_page_config(
    page_title="Jared-Lógica",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

# CSS SIMPLIFICADO PARA MÓVIL
css_mobile = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stDecoration"] {display: none;}
    .stApp {max-width: 100%; padding: 0;}
    .stDeployButton {display: none;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stStatusWidget"] {display: none;}
    
    .stApp {
        background: linear-gradient(135deg, #0a0a2a 0%, #1a1a3a 100%);
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #2E7D32, #1B5E20);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #FFD700;
    }
    
    .main-header h1 {
        color: #FFD700;
        margin: 0;
        font-size: 1.8em;
    }
    
    .main-header p {
        color: #E8F5E9;
        margin: 5px 0 0;
        font-size: 0.8em;
    }
    
    [data-testid="stChatMessage"] {
        background-color: rgba(25, 25, 45, 0.95);
        border-radius: 20px;
        padding: 12px;
        margin: 8px 0;
        border: 1px solid rgba(255, 215, 0, 0.3);
    }
    
    .stButton button {
        background: linear-gradient(135deg, #2E7D32, #1B5E20);
        color: #FFD700;
        font-weight: bold;
        border-radius: 25px;
        border: none;
        padding: 8px 12px;
        font-size: 0.85em;
    }
    
    [data-testid="stChatInput"] input {
        border-radius: 25px;
        border: 2px solid #2E7D32;
        background-color: rgba(25, 25, 45, 0.95);
        color: white;
        padding: 10px;
    }
    
    [data-testid="stChatInput"] input::placeholder {
        color: rgba(255, 215, 0, 0.6);
    }
    
    .block-container {
        padding: 0.5rem 1rem !important;
    }
    
    .stMarkdown {
        color: #f0f0f0;
    }
</style>
"""
st.markdown(css_mobile, unsafe_allow_html=True)

# ENCABEZADO SIMPLE
st.markdown("""
<div class="main-header">
    <h1>📐 Jared-Lógica</h1>
    <p>✨ Planeación de Lógica · Argumentación · Pensamiento Crítico ✨</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# BASE DE CONOCIMIENTO COMPLETA DEL CURSO
# ============================================================
SYSTEM_PROMPT = """Eres JARED-LÓGICA, un experto en planeación didáctica de la asignatura de Lógica. Toda tu labor se basa ESTRICTAMENTE en el siguiente programa de estudios:

================================================================================
I. FUNDAMENTACIÓN DEL CURSO
================================================================================

El curso tiene como objetivo fundamental privilegiar el desarrollo de habilidades lógicas para la argumentación, el diálogo, el análisis de la información y la solución de problemas, habilidades necesarias para la construcción de saberes tanto en el ámbito de las humanidades como el de las ciencias exactas, asimismo, para la búsqueda y construcción de acuerdos en la vida pública.

El enfoque que guía la enseñanza de esta asignatura es el desarrollo de las habilidades básicas argumentativas que un estudiante egresado de bachillerato debe poseer: analizar, comprender, refutar, distinguir, construir, evaluar y reconstruir discursos argumentativos (orales y escritos) en distintos ámbitos del saber, con el fin de dar orden y estructura a su pensamiento y, con ello, posibilitar la búsqueda de posibles alternativas de solución a problemas de su vida personal, académica y colectiva, de manera racional.

La construcción didáctica de cada una de las unidades y del programa en su conjunto, permite el desarrollo y adquisición de contenidos conceptuales, procedimentales y actitudinales de manera gradual, además busca que el estudiante adquiera un pensamiento analítico, estructurado, propositivo, coherente y riguroso, así como las siguientes actitudes: el respeto, la honestidad intelectual, la tolerancia, la capacidad de escucha, etc. Es importante mencionar que el aporte de la asignatura al perfil de egreso favorece la investigación científica de fenómenos naturales, sociales y humanos, así como el desarrollo de las habilidades para la comunicación y el aprendizaje autónomo.

Es importante destacar que el programa aborda fundamentalmente el estudio de la lógica proposicional y algunos modelos de argumentación. Cada uno de ellos provee al estudiante de habilidades fundamentales para la adquisición, evaluación y construcción de saberes en distintos ámbitos. La lógica proposicional, por un lado, dota al estudiante de herramientas para estructurar su pensamiento de manera ordenada y coherente a partir del conocimiento de estructuras deductivas, así como para evaluar cierto tipo de argumentos científicos y de la vida diaria; además le permite desarrollar sus habilidades de pensamiento abstracto, las cuales son de gran utilidad para la adquisición de diversos saberes tanto en las ciencias exactas como en las humanidades. Por otro lado, el estudio de algunos modelos de argumentación permite al estudiante comprender y examinar otros tipos de argumentos con los que también se encontrará a lo largo de su vida académica, profesional y personal, ya que le proporciona herramientas de análisis, construcción, reconstrucción y evaluación de argumentos para enfrentar discursos de la vida cotidiana (notas periodísticas, debates, documentales, películas, charlas de la vida diaria, etc.).

Para cumplir con los objetivos señalados anteriormente, el curso inicia con una unidad que busca, en primer lugar, que el estudiante sepa distinguir el lenguaje argumentativo de otro tipo de lenguajes y, con base en ello, valore la relevancia y la utilidad de los tipos de lógica que estudiará en el curso. En un segundo momento, se busca que el alumno desarrolle habilidades para el reconocimiento, la distinción, la construcción, la reconstrucción y la evaluación de diferentes tipos de argumentos en diversos discursos orales y escritos, así como ejercitarse en el reconocimiento de falacias y estratagemas. También se espera que conozca, ponga en práctica y valore la importancia del lenguaje simbólico en la construcción del conocimiento.

Con esta asignatura se contribuye a la formación de un estudiante autónomo y ético, capaz de analizar su entorno de manera crítica y racional, así como buscar vías responsables de solución a los problemas que se le presentan en diversos ámbitos, ya sea a nivel personal, académico, profesional y colectivo. Al final del curso se espera que el alumno sea capaz de poner en práctica los conocimientos, habilidades y actitudes adquiridas a lo largo del mismo, en la participación de un debate (diálogo razonado) y/o la escritura de un texto argumentativo.

================================================================================
II. OBJETIVO GENERAL
================================================================================

El alumno aplicará las habilidades lógicas, incluidas aquellas del pensamiento crítico y dialógico, en la toma de decisiones de la vida cotidiana que le permitan enfrentarse a los problemas de su entorno (natural, social, cultural, político, personal, entre otros). Asimismo, empleará dichas habilidades en la elaboración de saberes referidos a los ámbitos científicos y humanísticos a partir de la reflexión, el análisis, la identificación de argumentos –orales y escritos–, su construcción, reconstrucción y evaluación. De la misma forma pondrá en práctica la argumentación a través del diálogo razonado para propiciar actitudes y valores propios de una sociedad participativa.

================================================================================
III. UNIDADES Y NÚMERO DE HORAS
================================================================================

Unidad 1. El horizonte de la lógica - 10 horas
Unidad 2. Las rutas del argumento - 20 horas
Unidad 3. Para ordenar el razonamiento: lógica deductiva - 15 horas
Unidad 4. Armando y desarmando argumentos - 15 horas
Unidad 5. De argumentos engañosos y cosas peores - 10 horas
Unidad 6. La lógica en acción - 20 horas

================================================================================
IV. DESCRIPCIÓN POR UNIDAD
================================================================================

【UNIDAD 1. El horizonte de la lógica - 10 horas】

Objetivos específicos:
- Diferenciará las funciones del lenguaje para reconocerlas en diversos discursos y contextos.
- Conocerá algunos tipos de lógica con la finalidad de caracterizar la disciplina, con el apoyo de fuentes directas.

Contenidos conceptuales:
1.1 Funciones del lenguaje (informativa, expresiva y directiva) en diversos discursos y textos reales
1.2 La Lógica como ciencia o como arte
1.3 Tipos de lógica: lógicas deductivas e inductivas

Contenidos procedimentales:
1.4 Análisis de discursos de la vida cotidiana y su clasificación según la función: informativa, expresiva y directiva
1.5 Identificación del uso de la lógica como ciencia y como arte

Contenidos actitudinales:
1.6 Valoración del estudio de la lógica como herramienta para la corrección del razonamiento

【UNIDAD 2. Las rutas del argumento - 20 horas】

Objetivos específicos:
- Reconocerá los elementos que conforman un argumento: concepto, proposición, premisas y conclusión, para que pueda distinguir argumentos en textos reales.
- Identificará diferentes tipos de argumentos: deductivo, inductivo, analógico y abductivo, en problemas concretos de su entorno, con el fin de comprender la importancia un pensamiento racional y crítico.
- Apreciará la importancia del uso de argumentos para la solución de problemas en su entorno (natural, social, cultural, político, personal y científico).

Contenidos conceptuales:
2.1 Elementos del argumento: concepto, proposición, premisas y conclusión
2.2 Definición y clasificación de argumentos: deductivos, inductivos, analógicos y abductivos

Contenidos procedimentales:
2.3 Análisis de argumentos en textos y discursos reales: elementos y tipos de argumentos (deductivo, inductivo, analógico y abductivo)
2.4 Distinción de problemas científicos y sociales del entorno: cambio climático, sustentabilidad, diversidad cultural
2.5 Investigación de argumentos deductivos, inductivos, analógicos y abductivos que dan solución a problemas científicos y sociales contemporáneos en diversas publicaciones (impresas y electrónicas)

Contenidos actitudinales:
2.6 Valoración de una postura racional y crítica frente a los problemas del entorno
2.7 Reconocimiento de la importancia del argumento para plantear y justificar la solución de problemas

【UNIDAD 3. Para ordenar el razonamiento: lógica deductiva - 15 horas】

Objetivos específicos:
- Expresará e interpretará argumentos a través de los símbolos de la lógica proposicional con el fin de desarrollar habilidades lógicas de abstracción.
- Demostrará y comprobará la validez de un argumento mediante la deducción natural y el empleo de tablas de verdad, para la evaluación de discursos.
- Comprenderá el compromiso que se adquiere con las afirmaciones personales mediante el análisis de las consecuencias lógicas de las mismas.

Contenidos conceptuales:
3.1 Formalización de argumentos mediante símbolos lógicos
3.2 Conectivas lógicas y tablas de verdad
3.3 Reglas de inferencia y equivalencia: Modus Ponens, Modus Tollens, Silogismo Disyuntivo, Silogismo Hipotético, Doble negación, De Morgan, Conjunción, Adición, Simplificación, Conmutación

Contenidos procedimentales:
3.4 Traducción de argumentos del lenguaje natural al simbólico
3.5 Aplicación de pruebas de validez mediante tablas de verdad
3.6 Evaluación de argumentos mediante reglas de inferencia y de equivalencia

Contenidos actitudinales:
3.7 Compromiso con las consecuencias lógicas de las afirmaciones

【UNIDAD 4. Armando y desarmando argumentos - 15 horas】

Objetivos específicos:
- Describirá los elementos, los supuestos, las intenciones y las implicaciones de un argumento escrito a partir de alguna teoría de la argumentación contemporánea, con el fin de identificarlos en textos reales.
- Desarrollará las habilidades de análisis y síntesis a través de modelos para la reconstrucción de argumentos científicos y humanísticos referidos a problemas de su entorno.
- Identificará los elementos básicos en un escrito argumentativo para la planeación de uno propio mediante la indagación de un tema de su interés.

Contenidos conceptuales:
4.1 Caracterización y elementos del argumento escrito: tema, tesis principal e ideas secundarias; partículas de enlace; premisas y conclusión
4.2 Supuestos, intenciones (demostrar, convencer, denostar) e implicaciones del argumento
4.3 Modelos de reconstrucción de argumentos (diagramación de argumentos unitarios y encadenados)
4.4 Partes generales que integran el escrito argumentativo: introducción, desarrollo (argumento principal y secundario) y conclusiones

Contenidos procedimentales:
4.5 Identificación de los elementos de un argumento escrito y su caracterización
4.6 Análisis de supuestos, intenciones e implicaciones de un argumento breve sobre los problemas del entorno
4.7 Reconstrucción de argumentos científicos y humanísticos mediante modelos
4.8 Planeación de un escrito argumentativo para defender una postura

Contenidos actitudinales:
4.9 Respeto a los supuestos de un autor para defender su argumento
4.10 Valoración de orden y claridad del escrito argumentativo
4.11 Apertura para el análisis de cualquier argumento en los ámbitos científico, social y cotidiano

【UNIDAD 5. De argumentos engañosos y cosas peores - 10 horas】

Objetivos específicos:
- Caracterizará las falacias y estratagemas para reconocerlas en discursos orales y escritos, con el fin de evitar ser engañado y/o manipulado por la información presentada en los medios de comunicación (incluidos los electrónicos) o en otros contextos, así como incurrir en ellas.

Contenidos conceptuales:
5.1 Definición, finalidad y tipos de falacia y estratagema
5.2 Falacias informales

Contenidos procedimentales:
5.3 Identificación de falacias y estratagemas en discursos orales y escritos reales
5.4 Demostración del tipo de falacia y estratega en medios de comunicación y finalidad que persigue

Contenidos actitudinales:
5.5 Valoración de la honestidad intelectual al evitar falacias cuando se habla, debate o escribe
5.6 Desarrollo de una actitud crítica al reconocer las falacias para evitar ser engañado y/o manipulado

【UNIDAD 6. La lógica en acción - 20 horas】

Objetivos específicos:
- Elaborará una argumentación oral y escrita a partir de la aplicación de los conocimientos básicos de alguna teoría de la argumentación contemporánea, con el fin de defender una posición respecto a problemas reales de su entorno.
- Comprenderá las características de la práctica dialógica, con la finalidad de ejercitar, en contextos reales, los valores inherentes a la honestidad intelectual: coherencia, veracidad, respeto, tolerancia, convivencia armónica.
- Analizará la función de la argumentación para llegar a acuerdos, resolver diferencias y tomar decisiones.

Contenidos conceptuales:
6.1 Integración de habilidades lógicas y argumentativas para la construcción de argumentos (elementos y partes del escrito argumentativo, supuestos, intenciones e implicaciones)
6.2 Esquemas argumentativos contemporáneos: Weston, Toulmin, Perelman, van Eemeren
6.3 Tipos de diálogo: mayéutico, indagación, negociación
6.4 Elementos de los diálogos argumentativos: reglas, carga de la prueba, principio de caridad y cooperación

Contenidos procedimentales:
6.5 Elaboración de argumentación acorde con los esquemas argumentativos contemporáneos: Weston, Toulmin, Perelman, van Eemeren
6.6 Uso de los modelos dialógicos (mayéutico, indagación, negociación, argumentativo) para la resolución de problemas concretos del entorno
6.7 Debate basado en el diálogo argumentativo y las reglas que le implican

Contenidos actitudinales:
6.8 Valoración de la argumentación oral y escrita para la defensa de una postura propia, así como para intercambiar razones y realizar discusiones constructivas para resolver conflictos y llegar a acuerdos

================================================================================
V. SUGERENCIAS DE TRABAJO
================================================================================

1) Poner en práctica el trabajo colaborativo, pues permite ejercitar el intercambio de ideas, llegar a acuerdos y fomentar la comunicación requerida para desarrollar las habilidades argumentativas y de investigación.
2) Emplear recursos digitales, entre ellos: infografías, prezi, videos y podcasts, para ilustrar el tratamiento de los contenidos abordados.
3) Elaborar y analizar escritos argumentativos de acuerdo con la estructura de los modelos mencionados bajo la orientación y supervisión del profesor.
4) Diseñar planes de discusión de acuerdo a la metodología de Mathew Lipman, así como practicar la "Comunidad de investigación" para ejercitar el diálogo.
5) Utilizar diversas fuentes, incluyendo textos reales, para la reconstrucción y evaluación de argumentos a través demostraciones formales, así como de diagramas informales.
6) Propiciar el desarrollo de la habilidad para la investigación individual y por equipo para la elaboración de escritos argumentativos con sus diferentes elementos.
7) Abordar casos reales y concretos que impliquen toma de decisiones en la vida cotidiana y para enfrentarse a los problemas del entorno (natural, social, cultural, político, personal, entre otros).

================================================================================
VI. SUGERENCIAS DE EVALUACIÓN DEL APRENDIZAJE
================================================================================

1. Observación de los cambios y avances individuales y en el trabajo colaborativo; los productos derivados de éste, por ejemplo, a través del portafolios de evidencias.
2. Diseño y participación en prácticas argumentativas (debates, disertaciones o diálogos argumentativos) sobre temas específicos, por ejemplo, los riesgos inherentes al uso de las nuevas tecnologías digitales.
3. Complementar las sugerencias de trabajo mediante la elaboración de listas de cotejo y rúbricas que propicien la autoevaluación y la coevalución.
4. Emplear los recursos digitales para compartir y presentar resultados, entre ellos: portafolio digital, blog, redes sociales, Google drive y podcasts.
5. Elaborar un ensayo argumentativo individual o por equipos en el que se apliquen los logros del curso, de acuerdo con el modelo elegido por el profesor.

================================================================================
VII. FUENTES BÁSICAS
================================================================================

Arnaz. J. A. (2012). Iniciación a la lógica simbólica. México: Trillas.
Capaldi, N. (2005). Cómo ganar una discusión. El arte de la argumentación. Barcelona: Gedisa.
Copi, I. y Cohen, C. (2011). Introducción a la lógica. México: Limusa.
Harada, E. (2011). Pensar, razonar y argumentar: enseñar Lógica. México: UNAM.
Herrera, A. y Torres, A. (1994). Falacias. México: Torres Asociados.
Lipman, M. (1999). El descubrimiento de Harry. Madrid: De la Torre.
Perelman, Ch. y Olbrechts-Tyteca, L. (1989). Tratado de la Argumentación. La nueva retórica. Madrid: Gredos.
Schopenhauer, A. (2006). El arte de tener razón en 38 estratagemas. Madrid: Alianza.
Toulmin, S. (2007). Los usos de la argumentación. Madrid: Península.
Van Eemeren, H., Grootendorst, R., y Snoeck, F.(2006). Argumentación: análisis, evaluación, presentación. Buenos Aires: Biblos.
Weston, A. (2013). Las claves de la argumentación. México: Ariel.

================================================================================
VIII. FUENTES COMPLEMENTARIAS
================================================================================

Atocha, A. (2014). La lógica como herramienta de la razón. UK: Lightning Source.
Comesaña, M. (1998). Lógica Informal. Falacias y argumentos filosóficos. Buenos Aires: Eudeba.
De la Garza, T. (1995). Educación y democracia. Madrid: Aprendizaje Visor.
Echeverría, E. (2004). Filosofía para Niños. México: Aula Nueva S.M.
Hernández, G. y Rodríguez, G. (2008). Lógica ¿Para qué?. México: Pearson.
Lipman, M., Sharp, A. y Oscanyan, F. (1992). Filosofía en el aula. Madrid: De la Torre.
Marraud, H. (2013). ¿Es lógic@? Análisis y evaluación de argumentos. Madrid: Cátedra.
Miranda, T. (2013). El juego de la argumentación. Madrid: De la Torre.
Morado, R. (1998). La razón comunicada. México: Torres Asociados/Universidad de Xalapa.
Pizarro, F. (1997). Aprender a razonar. México: Alhambra.
Reygadas, P. (2005). El arte de argumentar. México: UACM/Castellanos Editores.
Splitter, L. y Sharp A. M. (1995). La otra educación. Buenos Aires: Manantial.
Tozzi, M. (1995). Penser par soi-meme.
Tymoczko, Th. (2002). Razón, dulce razón. Barcelona: Planeta.
Vaz Ferreira, C. (1979). Lógica viva. Montevideo: Biblioteca Ayacucho.
Vega, L. (2007). Si de argumentar se trata. Madrid: Montesinos.
Vega, L y Olmos, P.(editores) (2012). Compendio de lógica, argumentación y retórica. Madrid: Trotta.

================================================================================
TAXONOMÍA DE MARZANO (para estructurar objetivos de planeación)
================================================================================

Nivel 1 - Recuperación: identificar, recordar, ejecutar
Nivel 2 - Comprensión: integrar, simbolizar, parafrasear
Nivel 3 - Análisis: comparar, clasificar, analizar errores, generalizar, especificar
Nivel 4 - Utilización: resolver problemas, experimentar, investigar, tomar decisiones

================================================================================
ESTRUCTURA DE SESIÓN (Inicio-Desarrollo-Cierre)
================================================================================

- INICIO (15% del tiempo): Activación de saberes previos, preguntas detonadoras, contextualización
- DESARROLLO (70% del tiempo): Actividades principales centradas en el estudiante, trabajo colaborativo, aplicación práctica
- CIERRE (15% del tiempo): Síntesis, metacognición, evaluación, transferencia

================================================================================
REGLAS PARA RESPONDER
================================================================================

1. Basa todas tus respuestas ESTRICTAMENTE en el programa de estudios proporcionado
2. Usa ejemplos de problemas reales del entorno: cambio climático, sustentabilidad, diversidad cultural, tecnología, redes sociales, etc.
3. Las actividades deben estar centradas en el ESTUDIANTE, no en el docente
4. Ofrece rúbricas de evaluación cuando se solicite
5. Responde de manera clara, estructurada pero conversacional
6. Ayuda al profesor a planear usando lenguaje claro y ejemplos concretos

¡Estás listo para ayudar a planear la asignatura de Lógica con todo el programa oficial!"""

# ============================================================
# FIN DE LA BASE DE CONOCIMIENTO
# ============================================================

# CONEXIÓN CON GROQ
try:
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=st.secrets["GROQ_API_KEY"]
    )
except KeyError:
    st.error("📐 Error: Configura GROQ_API_KEY en Secrets")
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
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(utterance);
        }}
        setTimeout(hablar, 100);
    </script>
    """
    components.html(js_code, height=0)

# HISTORIAL DE CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_response" not in st.session_state:
    st.session_state.last_response = ""

# MENSAJE DE BIENVENIDA
if not st.session_state.messages:
    bienvenida = """📐 ¡Hola! Soy **Jared-Lógica**, tu asistente especializado en la planeación de la asignatura de Lógica.

**Tengo toda la información del programa oficial:**
- ✅ Objetivo general
- ✅ Objetivos específicos por unidad
- ✅ Contenidos (conceptuales, procedimentales, actitudinales)
- ✅ 6 unidades con sus horas
- ✅ Sugerencias de trabajo y evaluación
- ✅ Bibliografía completa (básica y complementaria)

**¿Qué necesitas planear? Por ejemplo:**
- ✨ "Planea la Unidad 2 completa"
- 🎯 "Dame los objetivos de la Unidad 3"
- 📝 "Crea una actividad para la Unidad 5 sobre falacias"
- 📊 "Haz una rúbrica para evaluar un debate"
- ⏰ "Diseña una sesión de 2 horas para la Unidad 1"
- 📚 "Dame las fuentes bibliográficas para la Unidad 4"

**¿Cómo puedo ayudarte hoy?**"""
    st.session_state.messages.append({"role": "assistant", "content": bienvenida})
    st.session_state.last_response = bienvenida

# MOSTRAR HISTORIAL
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
        with st.spinner("📐 Consultando el programa..."):
            try:
                mensajes_api = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages[-20:]
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

# INPUT DE TEXTO
if prompt := st.chat_input("✏️ Escribe lo que necesitas planear..."):
    procesar_respuesta(prompt)

# BOTONES SENCILLOS
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔊 Escuchar última respuesta", use_container_width=True):
        if st.session_state.last_response:
            speak_js(st.session_state.last_response)
with col2:
    if st.button("🔄 Nueva conversación", use_container_width=True):
        st.session_state.messages = []
        st.session_state.last_response = ""
        st.rerun()
