# C:\Users\yilinet.bueno\Desktop\Modelos\Estudio Medico\CardioTech>cd C:\Users\yilinet.bueno\AppData\Local\Programs\Python\Python310\python.exe app1.py
# Correr desde terminal cmd, alla si dejo instalar librerias del modelo C:\Users\yilinet.bueno\Desktop\Modelos\Estudio Medico\CardioTech>streamlit run app1.py 
# APP STREAMLIT: carga el pipeline y predice directo

# import streamlit as st
# import pandas as pd
# from PIL import Image
# import joblib
# from pathlib import Path
# from streamlit_pdf_viewer import pdf_viewer
# from streamlit import session_state as ss


# st.set_page_config(page_title="CardioTech | RCV", layout="wide")

# # ----- Cargar artefactos -----
# ART = Path("artefactos_rcv_simple")
# pipe = joblib.load(ART/"pipeline_modelo.joblib")
# BEST_THRESHOLD = float((ART/"threshold_fijo.txt").read_text().strip())

# # ---- Encabezado ----
# st.title("CardioTech | Calculadora de Riesgo Cardiovascular")
# #st.header("Calculadora de Riesgo Cardiovascular")
# st.caption("Modelo estadístico para estimar probabilidad de riesgo cardiovascular.")

# st.sidebar.image("LogoCardiotechfondo.png", width=200)
# st.sidebar.image("bodytechfondo.png", width=200)
# st.sidebar.image("BIA.png", width=200)
# st.sidebar.caption("Realizado por Investigación BIA")

# # Video
# try:
#     with open("MODELORCV2.mp4", "rb") as video_file:
#                 col1, col2, col3=st.columns([1, 4, 1])
#                 with col2:
#                   st.video(video_file.read(),autoplay=True, loop=True, start_time=3, width=3000)
# except FileNotFoundError:
#     st.info("Video no disponible.")

# with st.form("rcv"):
#     nombre = st.text_input("Nombre")
#     politica = st.selectbox("¿Aceptas nuestra política de protección de datos?", ["SI","NO"])
#     st.link_button("Ver Política", "https://bodytech.com.co/poltica-de-tratamiento-de-datos-personales")

#     #  15 variables del modelo EXACTAS, 2 calculadas 
#     genero = st.selectbox("Género de nacimiento", ["Femenino","Masculino"])
#     estrato = st.selectbox("Estrato", ["1","2","3","4","5","6"])   
#     tipo_vinc = st.selectbox("Tipo de vinculación", ["Contributivo","Subsidiado","Vinculado","Particular ","Otro"])
    
#     st.caption("Contributivo: Personas que tienen una vinculación laboral")
#     st.caption("Subsidiado: Personas que no cuenten con capacidad de pago o en estado de vulnerabilidad")
#     st.caption("Vinculado:  Personas con incapacidad de pago en espera de ser beneficiarios del régimen subsidiado")
#     st.caption("Particular: Personas con servicios personalizados con mayor cubrimiento (medicina prepagada)")

#     ocupacion = st.selectbox("Ocupación", ["Profesional","Tecnólogo/Tecnico","Bachiller"])

#     sedentarismo = st.selectbox("¿Realizas menos de 150 minutos (2.5h) de actividad fisica a la semana?", ["SI","NO"])
#     tabaquismo = st.selectbox("¿Fuma actualmente?", ["SI","NO"])
#     antecedente_fam = st.selectbox("¿Antecedentes familiares de Enfermedad Cardiovascular?", ["SI","NO"])
#     tipo_diagnostico=st.selectbox("Tienes alguna enfermedad Cardiaca, Renal o Diabetes diagnosticada?", ["SI","NO"])

#     peso = st.number_input("Peso (kg)", min_value=5.0, max_value=300.0, step=5.0, format="%.1f")   
#     talla = st.number_input("Talla (m)", min_value=0.50,max_value=2.5, step=0.5, format="%.1f")  
#     mmusc = st.number_input("Porcentaje masa muscular (%)", min_value=10.0, max_value=60.0, step=3.0, format="%.1f")
#     imm = ((peso*mmusc)/100)/(talla*talla)
#     st.caption(f"El resultado del IMM es: {imm}")
#     #imm = st.number_input("IMM", min_value=3.89,max_value=20.0, step=5.0, format="%.1f")
#     fat = st.number_input("Porcentaje de grasa (%)", min_value=2.0, max_value=50.0, step=5.0, format="%.1f")
#     imc = (peso/(talla*talla))
#     st.caption(f"El resultado del IMC es: {imc}")
#     #imc = st.number_input("IMC", min_value=14.0, max_value=55.0, step=0.1, format="%.1f")

#     abd = st.number_input("Perímetro abdominal (cm)", min_value=40, max_value=250, step=1)
#     sis = st.number_input("Tensión arterial sistólica (mmHg)", min_value=80, max_value=280, step=1)
#     ses_sem = st.number_input("¿En promedio cuántos días a la semana entrenas?", min_value=0, max_value=7, step=1)
#     mean_minentr = st.number_input("¿En promedio cuántos minutos por día entrenas?", min_value=0, max_value=1440, step=1)
#     min_sem=(mean_minentr*ses_sem)
#     st.caption(f"Minutos de entrenamiento por semana en promedio es: {min_sem}")  
#     #min_sem = st.number_input("¿En promedio cuántos minutos a la semana entrenas?", min_value=0, max_value=10000, step=10)

#     ok = st.form_submit_button("Calcular riesgo")

# #Variables del modelo 
# if ok:
#     fila = pd.DataFrame([{
#         'imm': imm,
#         'fat_percentage': fat, 
#         'muscle_mass_percentage': mmusc,
#         'abdominal_perimeter': int(abd),
#         'tension_arte_sis': int(sis),
#         'Sedentarismo': sedentarismo,  # SI/NO tal cual
#         'sesiones_en_la_semana': int(ses_sem),
#         'minutos_por_semana': int(min_sem), 
#         'tipo_vinculacion': tipo_vinc,
#         'ocupacion_validada': ocupacion,
#         'Antecedente Familiar': antecedente_fam,  # SI/NO tal cual
#         'imc': peso/(talla**2), 
#         'Estrato': str(estrato),
#         'genero': genero,
#         'Tabaquismo': tabaquismo  # SI/NO tal cual
#     }])

#     proba = float(pipe.predict_proba(fila)[:,1][0])
#     yhat = int(proba >= 0.6)

#     st.markdown("---")
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Probabilidad de Riesgo", f"{proba*100:.2f}%")
#     col2.caption("Modelo estadístico para estimar probabilidad de riesgo cardiovascular by Bodytech.")

#     if tipo_diagnostico=='SI':
#         st.error(  "🔴 Riesgo **ALTO** según el modelo. Consulta medica por seguimiento a enfermedad diagnosticada.")
#     elif proba>=0.8 :
#         st.error(  "🔴 Riesgo **ALTO** según el modelo. Consulta médica recomendada.")
#     elif 0.7 <= proba < 0.8:
#         st.warning("🟡 Riesgo **MEDIO** según el modelo. Consulta médica recomendada, mejora tus hábitos.")
#     elif 0.6 <= proba < 0.7 :
#         st.warning("🟢 Riesgo **BAJO** según el modelo. Mantén hábitos saludables.")
#     else:
#         st.success("🟢 **SIN RIESGO** según el modelo. Mantén hábitos saludables.")


# app.py
import streamlit as st
import pandas as pd
import json
import io
import joblib
import sys
from pathlib import Path
from PIL import Image
from streamlit import session_state as ss  
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Image as RLImage,
    Paragraph, Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from PyPDF2 import PdfReader, PdfWriter

# =========================================================
# 1. CONFIGURACIÓN Y HACK DE COMPATIBILIDAD (DEBE IR PRIMERO)
# =========================================================
st.set_page_config(page_title="CardioTech | RCV", layout="wide")

# Importar utilidades y registrarlas para que joblib las encuentre
import preprocessing_utils
sys.modules['preprocessing_utils'] = preprocessing_utils
from preprocessing_utils import preprocess_with_schema, preproc_fn

# Registrar en el main para máxima compatibilidad con el pickle
import __main__
__main__.preproc_fn = preproc_fn
__main__.preprocess_with_schema = preprocess_with_schema

# ================================
# 2. CARGAR ARTEFACTOS DEL MODELO
# ================================
ART = Path("artefactos_rcv_simple_2")

@st.cache_resource
def load_model_assets():
    # Cargamos el pipeline (ahora sí encontrará las referencias)
    model = joblib.load(ART / "pipeline_modelo_2_inference.joblib")
    
    # Cargamos el umbral
    threshold = float((ART / "threshold_fijo_2.txt").read_text().strip())
    
    # Cargamos el esquema
    with open(ART / "feature_schema.json") as f:
        schema = json.load(f)
    
    return model, threshold, schema

pipe, BEST_THRESHOLD, FEATURE_SCHEMA = load_model_assets()

# ================================
# 3. ENCABEZADO Y UI
# ================================
st.title("CardioTech | Calculadora de Riesgo Cardiovascular")
st.caption("Modelo de machine learning para estimar probabilidad de riesgo cardiovascular.")

st.sidebar.image("LogoCardiotechfondo.png", width=250)
st.sidebar.image("bodytechfondo.png", width=250)
st.sidebar.image("BIA.png", width=180)
st.sidebar.caption("Realizado por Investigación BIA")

try:
    with open("MODELORCV2.mp4", "rb") as video_file:
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.video(video_file.read(), autoplay=True, loop=True, start_time=3)
except FileNotFoundError:
    st.info("Video no disponible.")

# ================================
# 4. FUNCIONES DE APOYO (PDF)
# ================================
def generar_pdf_completo(datos, limites, pdf_recomendacion, logo_path="LogoCardiotechfondo.png"):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph("Reporte de Resultados - Calculadora RCV", styles['Title'])
    try:
        logo = RLImage(logo_path, width=200, height=200)
        elements.append(logo)
    except:
        pass
    elements.append(title)
    elements.append(Spacer(1, 3))

    cell_style = ParagraphStyle(name="cell_style", fontSize=9, alignment=1, leading=10)
    data_table = [["Variable", "Valor", "Referencia"]]
    for key, value in datos.items():
        referencia = limites.get(key, "")
        data_table.append([
            Paragraph(str(key), cell_style),
            Paragraph(str(value), cell_style),
            Paragraph(str(referencia), cell_style)
        ])

    table = Table(data_table, colWidths=[150, 150, 250])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#FFA500")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    
    pdf_datos = PdfReader(buffer)
    with open(pdf_recomendacion, "rb") as f:
        pdf_reco = PdfReader(f)
        writer = PdfWriter()
        for page in pdf_datos.pages:
            writer.add_page(page)
        for page in pdf_reco.pages:
            writer.add_page(page)

        output_buffer = io.BytesIO()
        writer.write(output_buffer)
        output_buffer.seek(0)
    return output_buffer

# ================================
# 5. FORMULARIO Y LÓGICA
# ================================
with st.form("rcv"):
    nombre = st.text_input("Nombre")
    politica = st.selectbox("¿Aceptas nuestra política de protección de datos?", ["SI","NO"])
    st.link_button("Ver Política", "https://bodytech.com.co/poltica-de-tratamiento-de-datos-personales")

    genero_1 = st.selectbox("Género de nacimiento", ["Femenino", "Masculino"])
    genero = 0 if genero_1 == "Femenino" else 1

    estrato_1 = st.selectbox("Estrato", ["1","2","3","4","5","6"])
    estrato = int(estrato_1) - 1

    tipo_vinc_1 = st.selectbox("Tipo de vinculación", ["Contributivo","Subsidiado","Vinculado","Particular","Otro"])
    tipo_map = {"Contributivo":0,"Otro":2,"Subsidiado":4,"Particular":3,"Vinculado":5}
    tipo_vinc = tipo_map.get(tipo_vinc_1, 5)

    ocupacion_1 = st.selectbox("Ocupación", ["Profesional","Tecnólogo/Tecnico","Bachiller"])
    ocup_map = {"Profesional":2,"Tecnólogo/Tecnico":3,"Bachiller":0}
    ocupacion = ocup_map.get(ocupacion_1,0)

    sedentarismo = st.selectbox("¿Realizas menos de 150 minutos (2.5h) de actividad fisica a la semana?", ["SI","NO"])
    tabaquismo = st.selectbox("¿Fuma actualmente?", ["SI","NO"])
    antecedente_fam = st.selectbox("¿Antecedentes familiares de Enfermedad Cardiovascular?", ["SI","NO"])
    tipo_diagnostico = st.selectbox("Tienes alguna enfermedad Cardiaca, Renal o Diabetes diagnosticada?", ["No aplica","Cardio",'Renal/Diabetes'])

    peso = st.number_input("Peso (kg)", min_value=5.0, max_value=300.0, value=70.0, step=1.0)
    talla = st.number_input("Talla (m)", min_value=0.50, max_value=2.5, value=1.70, step=0.01)
    mmusc = st.number_input("Porcentaje masa muscular (%)", min_value=10.0, max_value=60.0, value=30.0)
    
    imm = ((peso*mmusc)/100)/(talla*talla)
    st.caption(f"El resultado del IMM es: {imm:.2f}")
    
    fat = st.number_input("Porcentaje de grasa (%)", min_value=2.0, max_value=50.0, value=20.0)
    imc = (peso/(talla*talla))
    st.caption(f"El resultado del IMC es: {imc:.2f}")

    abd = st.number_input("Perímetro abdominal (cm)", min_value=40, max_value=250, value=85)
    sis = st.number_input("Tensión arterial sistólica (mmHg)", min_value=80, max_value=280, value=120)
    ses_sem = st.number_input("¿Días a la semana entrenas?", min_value=0, max_value=7, value=3)
    mean_minentr = st.number_input("¿Minutos por día entrenas?", min_value=0, max_value=1440, value=60)
    
    min_sem = (mean_minentr * ses_sem)
    st.caption(f"Minutos promedio por semana: {min_sem}")

    ok = st.form_submit_button("Calcular mi riesgo cardiovascular 🧡")

if ok:
    fila = pd.DataFrame([{
        'imm': imm, 'fat_percentage': fat, 'muscle_mass_percentage': mmusc,
        'abdominal_perimeter': int(abd), 'tension_arte_sis': int(sis),
        'Sedentarismo': sedentarismo, 'sesiones_en_la_semana': int(ses_sem),
        'minutos_por_semana': int(min_sem), 'tipo_vinculacion': tipo_vinc,
        'ocupacion_validada': ocupacion, 'Antecedente Familiar': antecedente_fam,
        'imc': imc, 'Estrato': estrato, 'Tabaquismo': tabaquismo, 'genero_1': genero
    }])

    proba = float(pipe.predict_proba(fila)[:, 1][0])

    if tipo_diagnostico != "No aplica" or proba >= 0.8:
        riesgo = "ALTO"; pdf_path = "pdf/alto.pdf"; st.error("🔴 Riesgo **ALTO**.")
    elif 0.7 <= proba < 0.8:
        riesgo = "MEDIO"; pdf_path = "pdf/medio.pdf"; st.warning("🟡 Riesgo **MEDIO**.")
    elif 0.6 <= proba < 0.7:
        riesgo = "BAJO"; pdf_path = "pdf/bajo.pdf"; st.warning("🟢 Riesgo **BAJO**.")
    else:
        riesgo = "SIN RIESGO"; pdf_path = "pdf/sinriesgo.pdf"; st.success("🟢 **SIN RIESGO**.")

    datos_usuario = {
        "Nombre": nombre, "Probabilidad": f"{proba*100:.2f}%", "Clasificación": riesgo,
        "IMM": f"{imm:.2f}", "IMC": f"{imc:.2f}", "TAS (mmHg)": int(sis),
        "Grasa %": f"{fat:.2f}%", "Músculo %": f"{mmusc:.2f}%", "Abd (cm)": int(abd)
    }

    datos_limites = {
        "Clasificación": "Sin riesgo <60% / Bajo 60-70% / Medio 70-80% / Alto >=80%",
        "IMM": "H: >=7.26 M: >=5.45", "IMC": "Normal 18.5-24.9",
        "TAS (mmHg)": "Normal <120"
    }

    try:
        pdf_final = generar_pdf_completo(datos_usuario, datos_limites, pdf_path)
        st.download_button(
            label="📄 Descargar reporte completo en PDF",
            data=pdf_final,
            file_name=f"Reporte_RCV_{nombre}.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"Error al generar el PDF: {e}")
