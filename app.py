import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO

# Datos de referencia que ya cargas
df_ref = pd.read_excel("C:/Users/yilinet.bueno/Desktop/Modelos/Estudio Medico/predicionmodelo11_07_25v3.xlsx")

# Inicializa un contenedor en sesión para las respuestas
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []  # lista de dicts

def main():
    st.title("CardioTech by Bodytech")
    st.header("Calculadora de Riesgo Cardiovascular")
    st.subheader("Creada por el equipo de BI Bodytech 2025")

    img = Image.open("LogoCardiotech.png")
    st.image(img, width=800)

    # ----- Formulario -----
    with st.form("form_rcv", clear_on_submit=False):
        nombre = st.text_input("Ingresa tu nombre:")
        st.caption("Esta calculadora es un modelo estadístico que estima probabilidad de riesgo cardiovascular.")

        # Video (opcional)
        try:
            with open("MODELORCV.mp4", "rb") as video_file:
                st.video(video_file.read(), start_time=3)
        except FileNotFoundError:
            st.info("Video no disponible.")

        genero = st.selectbox("Elige tu género:", ["Masculino", "Femenino"])
        sedentarismo = st.selectbox("¿Te consideras una persona sedentaria? (más de 6 horas en reposo)",["SI", "NO"])

        # Entradas numéricas con validación
        abdominal = st.number_input("Perímetro abdominal (50–200)", min_value=50, max_value=200, step=1)
        ocupacion = st.selectbox("Elige tu ocupación:", ["Profesional", "Técnico", "Bachiller"])
        sistolica = st.number_input("Tensión arterial sistólica (100–250)", min_value=100, max_value=250, step=1)
        masa_muscular = st.number_input("Masa muscular (kg)", min_value=0.0, step=1.0, format="%.1f")
        entrenos_semana = st.number_input("¿Cuántas veces a la semana entrenas?", min_value=0, max_value=14, step=1)

        submitted = st.form_submit_button("Guardar respuesta")

    # ----- Al enviar: guarda una fila en memoria -----
    if submitted:
        fila = {
            "nombre": nombre,
            "genero": genero,
            "sedentarismo": sedentarismo,
            "perimetro_abdominal": int(abdominal),
            "ocupacion": ocupacion,
            "sistolica": int(sistolica),
            "masa_muscular": float(masa_muscular),
            "entrenos_semana": int(entrenos_semana),
        }
        st.session_state.respuestas.append(fila)
        st.success(f"Datos de {nombre} guardados en la sesión.")

    # ----- Muestra DataFrame acumulado -----
    if st.session_state.respuestas:
        df_respuestas = pd.DataFrame(st.session_state.respuestas)
        st.subheader("Respuestas capturadas")
        st.dataframe(df_respuestas, use_container_width=True)

        # Botón para descargar a Excel
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df_respuestas.to_excel(writer, index=False, sheet_name="respuestas")
            # (Opcional) incluir la hoja de referencia
            df_ref.head(1000).to_excel(writer, index=False, sheet_name="referencia")
        st.download_button(
            label="⬇️ Descargar Excel",
            data=buffer.getvalue(),
            file_name="respuestas_rcv.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    else:
        st.info("Aún no hay respuestas guardadas. Completa el formulario y presiona **Guardar respuesta**.")

    # ----- Extra: visualización de tu df original -----
    st.subheader("Datos de referencia (primeras 1000 filas)")
    st.dataframe(df_ref.head(1000), use_container_width=True)

if __name__ == "__main__":
    main()






