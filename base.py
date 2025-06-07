import numpy as np
import skfuzzy as fuzz
import plotly.graph_objs as go
import plotly.subplots as sp

def fuzificar_datos(lista):
    lista_ordenada = sorted(lista)
    Q1, Q2, Q3 = np.percentile(lista_ordenada, [25, 50, 75])
    min_val = min(lista)
    max_val = max(lista)

    x = np.linspace(min_val, max_val, 1000)

    membresia_L = fuzz.trapmf(x, [min_val, min_val, min_val, Q1])
    membresia_Pi = fuzz.trapmf(x, [Q1, Q2, Q2, Q3])
    membresia_Gamma = fuzz.trapmf(x, [Q3, max_val, max_val, max_val])

    membresia_combinada = np.fmax(membresia_L, np.fmax(membresia_Pi, membresia_Gamma))

    fig = sp.make_subplots(rows=3, cols=1, shared_xaxes=True, subplot_titles=(
        "Función L (Bajo)", "Función Pi (Intermedio)", "Función Gamma (Alto)"))

    fig.add_trace(go.Scatter(x=x, y=membresia_L, mode='lines', name='L (Bajo)', line=dict(color='blue')),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=membresia_Pi, mode='lines', name='Pi (Intermedio)', line=dict(color='green')),
                  row=2, col=1)
    fig.add_trace(go.Scatter(x=x, y=membresia_Gamma, mode='lines', name='Gamma (Alto)', line=dict(color='red')),
                  row=3, col=1)

    fig.update_layout(
        height=700,
        title_text="Funciones de Membresía Difusas",
        xaxis_title="Valores",
        yaxis_title="Membresía",
        template="plotly_dark",
        showlegend=False
    )

    return fig, x, membresia_combinada

def desdifuzificar(x, membresia, metodo='centroid'):
    if metodo not in ['centroid', 'bisector', 'mom', 'som', 'lom']:
        raise ValueError("Método de desdifusificación no válido.")
    return fuzz.defuzz(x, membresia, metodo)
