import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN INICIAL (ESTO DEBE IR PRIMERO) ---
st.set_page_config(
    page_title="XI Congreso Prehospitalaria",
    layout="wide",
    page_icon="☕"
)

# --- ESTILOS CSS AVANZADOS (PARA QUE SE VEA BONITO) ---
# Aquí es donde ocurre la magia del diseño "estilo React"
st.markdown("""
    <style>
    /* Fondo General */
    .stApp {
        background-color: #f5f5f4; /* Stone-100 */
    }
    
    /* Estilo para las Tarjetas (Cards) */
    .custom-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-top: 4px solid #d97706; /* Amber-600 */
        margin-bottom: 20px;
    }
    
    /* Estilo del Header */
    .header-box {
        background: linear-gradient(to right, #1c1917, #451a03); /* Gradiente oscuro */
        padding: 30px;
        border-radius: 15px;
        color: white;
        margin-bottom: 25px;
        border-bottom: 6px solid #d97706;
    }
    
    /* Títulos */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Métricas bonitas */
    .metric-box {
        text-align: center;
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #d97706;
    }
    .metric-label {
        font-size: 14px;
        color: #57534e;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER PERSONALIZADO ---
st.markdown("""
    <div class="header-box">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>
                <span style="background-color: rgba(217, 119, 6, 0.2); color: #fbbf24; padding: 5px 10px; border-radius: 20px; font-size: 12px; font-weight: bold;">
                    ☕ EDICIÓN ESPECIAL
                </span>
                <h1 style="color: white; margin-top: 10px; margin-bottom: 5px; font-size: 40px;">XI Congreso Nacional</h1>
                <h2 style="color: #fbbf24; margin-top: 0; font-size: 30px;">Medicina Prehospitalaria</h2>
                <p style="color: #d6d3d1; font-style: italic;">"Identidad Cafetera en la Emergencia"</p>
                <div style="margin-top: 15px;">
                    <span style="background: rgba(255,255,255,0.1); padding: 5px 15px; border-radius: 5px; margin-right: 10px;">📅 23-25 Octubre 2025</span>
                    <span style="background: rgba(255,255,255,0.1); padding: 5px 15px; border-radius: 5px;">📍 Pereira (Aud. Jorge Roa)</span>
                </div>
            </div>
            <div style="text-align: right; display: none; @media (min-width: 768px) { display: block; }">
                 <div style="font-size: 80px;">🚑</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN ---
tab1, tab2, tab3 = st.tabs(["📈 RESUMEN & DOFA", "⏱️ CRONOGRAMA", "🤝 MATRIZ ALI
