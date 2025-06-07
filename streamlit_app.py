import streamlit as st
from PIL import Image
from base import fuzificar_datos, desdifuzificar

logo = Image.open("UNAM_logo.png")
col1, col2 = st.columns([1, 5])
with col1:
    st.image(logo, width=80)
with col2:
    st.title("Números Difusos")

# Seleccionamos el método
metodo = st.selectbox(
    "Selecciona el método de desdifusificación:",
    options=['centroid', 'bisector', 'mom', 'som', 'lom'],
    format_func=lambda x: {
        'centroid': 'Centroide',
        'bisector': 'Bisector',
        'mom': 'Media del Máximo',
        'som': 'Mínimo del Máximo',
        'lom': 'Máximo del Máximo'
    }[x]
)

# Pedimos los datos
num_datos = st.number_input("¿Cuántos datos deseas ingresar?", min_value=4, step=1)

# Ingresamos los datos y usamos las funciones de lógica difusa
st.subheader("Ingresa los valores:")
valores = []
cols = st.columns(2)

for i in range(int(num_datos)):
    with cols[i % 2]:
        val = st.number_input(f"Dato #{i+1}", key=f"dato_{i}")
        valores.append(val)

if st.button("Continuar"):
    if len(valores) < 4:
        st.error("Por favor, ingresa al menos 4 valores.")
    else:
        fig, x, membresia_combinada = fuzificar_datos(valores)
        st.plotly_chart(fig, use_container_width=True)

        resultado = desdifuzificar(x, membresia_combinada, metodo)

        st.metric(label=f"Resultado con {metodo}", value=f"{resultado:.2f}")
