# Números Difusos

Aplicación web interactiva desarrollada con Streamlit para la representación, análisis y desdifusificación de datos usando lógica difusa.

---

## Descripción

Esta herramienta permite:
- Ingresar un conjunto de datos numéricos.
- Aplicar funciones de membresía difusas (L, Pi y Gamma).
- Visualizar gráficamente las funciones de membresía.
- Obtener un valor desdifuso utilizando distintos métodos, como centroide, bisector, entre otros.

Está diseñada como una aplicación educativa para estudiantes, docentes y profesionales interesados en lógica difusa aplicada a la toma de decisiones, inteligencia artificial o control difuso.

---

## Tecnologías Utilizadas

- Python
- Streamlit
- NumPy
- Matplotlib o Plotly (según configuración)

---

## Cómo Ejecutar

1. Clona el repositorio:
   git clone https://github.com/tuusuario/numeros-difusos.git
   cd numeros-difusos

2. Instala las dependencias:
   pip install -r requirements.txt

3. Ejecuta la aplicación:
   streamlit run app.py

---

## Métodos de Desdifusificación Soportados

- Centroide
- Bisector
- Media del Máximo (MOM)
- Mínimo del Máximo (SOM)
- Máximo del Máximo (LOM)

---

## Funciones de Membresía

| Tipo   | Forma                  | Uso              |
|--------|------------------------|------------------|
| L      | Trapezoidal decreciente| Valores bajos    |
| Pi     | Triangular simétrica   | Valores medios   |
| Gamma  | Trapezoidal creciente | Valores altos    |

---

## Créditos

Este proyecto fue desarrollado como parte de un aprendizaje en lógica difusa, con apoyo de materiales académicos del laboratorio de optimización y servicios de la facultad de ingeniería de la Universidad Nacional Autónoma de México.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.
