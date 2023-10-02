from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_ALEX_MARZA_MANUEL.pdf"
image_alex = current_dir / "assets" / "alex.png"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Alex Marzá Manuel"
PAGE_ICON = ":wave:"
NAME = "Alex Marzá Manuel"
DESCRIPTION = """
Junior Data Scientist, ayudo a las empresas a tomar decisiones basadas en datos.
"""
EMAIL = "alexmarzadatascience@gmail.com"
SOCIAL_MEDIA = {
    "WhatsApp": "http://wa.me/34695802887?text=%C2%A1Hola!%20He%20revisado%20su%20perfil%20y%20parece%20encajar%20con%20lo%20que%20estamos%20buscando.%20Por%20ello,%20desde%20nuestro%20departamento%20de%20RRHH%20nos%20gustar%C3%ADa%20concertar%20una%20entrevista%20con%20usted%20para%20profundizar%20en%20el%20puesto%20laboral%20y%20conocernos%20mejor.%20%C2%A1Espero%20su%20respuesta!",
    "LinkedIn": "https://www.linkedin.com/in/alex-marza-data-science/",
    "GitHub": "https://github.com/AlexCapis",
    "Page-Links": "https://alex-links-page.streamlit.app/",
}
PROJECTS = {
    "🏆 Recursos Humanos Power BI - Investigación de los empleados, sueldos y evaluación": " ENLACE",
    "🏆 Indicadores Mundiales - Informe de población, mortalidad infantil y esperanza de vida":  " ENLACE ",
    "🏆 Venta de Videojuego Power BI - Análisis de ventas ": "ENLACE",
    "🏆 HEATLY - Aplicación web para olas de calor": " ENLACE",
    "🏆 PASSODI - Generador de contraseñas automático": "https://generador-claves.streamlit.app/",
    "🏆 Corazón Digital - Prediciendo enfermedades cardíacas con machine learning": " ENLACE"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- CARGA CSS, PDF E IMAGEN ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_alex = Image.open(image_alex )


# --- SECCIÓN PRINCIPAL---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_alex, width=230)

with col2:
    st.header(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- LINKS SOCIAL MEDIA ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SOBRE MI ---
st.write('\n')
st.subheader("😊 Sobre Mí")
st.write("---")
st.write(
    """
- ✔️ Curiosidad insaciable por los datos buscando contribuir al éxito con insights.
- ✔️ Gran capacidad analítica y creatividad en la búsqueda de soluciones.
- ✔️ Conocimientos y experiencia práctica en Python y Excel.
- ✔️ Buena comprensión de los principios estadísticos y sus respectivas aplicaciones.
- ✔️ Excelente capacidad de trabajo en equipo y gran sentido de la iniciativa en las tareas.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("🧠 Habilidades")
st.write("---")
st.write(
    """
- 👩‍💻 Programación: Python (Pandas, Numpy), SQL
- 📊 Visulización de datos: PowerBi, MS Excel, Matplotlib, Seaborn, Streamlit
- 📚 Modelización: Regresión logística, regresión lineal, árboles de decisión
- 🗄️ Bases de datos: MySQL
- 🤖 Inteligencia Artificial: OpenAI
"""
)


# --- EDUCACIÓN---
st.write('\n')
st.subheader("🎓 Educación")
st.write("---")
st.write("""
- ✔️ UJI- GRADO DE PUBLICIDAD Y RELACIONES PÚBLICAS  
  Septiembre 2014 - Junio 2015

- ✔️ UB-UPO-USAL - GRADO DE CRIMINOLOGÍA  
  Septiembre 2015 - Enero 2020

- ✔️ THE BRIDGE- BOOTCAMP DATA SCIENCE  
  Abril 2023 - Agosto 2023
""")


# --- CURSOS---
st.write('\n')
st.subheader("📝 Cursos y Certificaciones")
st.write("---")
st.write(
    """
- ✔️ Power BI- Análisis de Datos y Business Intelligence (22h)
- ✔️ SQL- Bases de Datos (20h)
- ✔️ Elementos de Inteligencia Artificial (50h)
- ✔️ Machine Learning para Data Science (50h)
- ✔️ Trading Algorítmico (50h)
- ✔️ Método Harvard de Negociación (50h)
- ✔️ Introducción al Análisis Técnico (25h)
"""
)



# --- EXPERIENCIA LABORAL ---
st.write('\n')
st.subheader("💼 Experiencia Laboral")
st.write("---")

# --- Trabajo 1
st.write("🚧", "**Operador de Mercados Financieros**")
st.write("Septiembre 2021 - Septiembre 2023")
st.write(
    """
- ►  Utilización de datos para informar sobre decisiones financieras.
- ►  Evaluación y mitigación de riesgos en operaciones financieras.
- ►  Logro de un crecimiento del '47%' de inversión personal en los últimos 12 meses.
- ►  Diseño y ejecución de estrategias efectivas de inversión.
- ►  Capacidad de mantener la calma y decidir con claridad bajo presión.
- ►  Aplicación de análisis gráfico, patrones e indicadores para la toma de decisiones.
- ►  Evaluación de activos financieros y análisis de tendencias para optimizar rendimientos.
"""
)


# --- Trabajo 2
st.write('\n')
st.write("🚧", " **Trabajos en Brighton**")
st.write("Mayo 2019 - Marzo 2020")
st.write(
    """

- ✔️ Botones, Hilton Brighton Metropole
- ✔️ Ayudante de cocina, Brighton Palace Pear
- ✔️ Camarero, Brighton PRYZM
    

"""
)


# --- PROYECTOS ESTRELLA ---
st.write('\n')
st.subheader("⭐ Proyectos Estrella")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# Manejar el clic del botón
st.write('\n')
st.subheader("🛑 ¡Espera! Todavía no hemos terminado")
st.write("---")


if st.button("🎉PAQUETE SORPRESA 🎉"):
    st.write('''
             ¡Prepárate para descubrir un talento apasionado por la ciencia de datos! Este CV interactivo es solo el comienzo. 
             Estoy listo para aportar mi pasión, creatividad y dedicación a su equipo. 
             ¡Descubre más sobre mí, solo tienes que contactarme haciendo click en 
             [WhatsApp](http://wa.me/34695802887?text=%C2%A1Hola!%20He%20revisado%20su%20perfil%20y%20parece%20encajar%20con%20lo%20que%20estamos%20buscando.%20Por%20ello,%20desde%20nuestro%20departamento%20de%20RRHH%20nos%20gustar%C3%ADa%20concertar%20una%20entrevista%20con%20usted%20para%20profundizar%20en%20el%20puesto%20laboral%20y%20conocernos%20mejor.%20%C2%A1Espero%20su%20respuesta!)!
             
             ''')

