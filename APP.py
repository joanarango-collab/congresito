import streamlit as st
import pandas as pd

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="XI Congreso Prehospitalaria",
    layout="wide",
    page_icon="☕"
)

# --- 2. ESTILOS (CSS) ---
st.markdown("""
    <style>
    .main {background-color: #f5f5f4;}
    h1 {color: #78350f;}
    h3 {color: #92400e;}
    .stProgress > div > div > div > div {background-color: #d97706;}
    </style>
""", unsafe_allow_html=True)

# --- 3. TÍTULO Y LOGO ---
col_logo, col_texto = st.columns([1, 5])
with col_texto:
    st.title("XI Congreso Nacional Medicina Prehospitalaria")
    st.markdown("### *Identidad Cafetera en la Emergencia* ☕")
    st.caption("📍 Pereira | 📅 23-25 Octubre 2025 | Aud. Jorge Roa & Edif 14")

st.divider()

# --- 4. DATOS ---
phases = {
    "1. ANTES (Preparación)": [
        {"area": "Gestión y Alianzas", "lead": "David & Andrés", "progress": 100, "status": "Completado"},
        {"area": "Logística y Ambientación", "lead": "Santiago & Leymar", "progress": 100, "status": "Completado"},
        {"area": "Comunicaciones", "lead": "Joan Sebastian", "progress": 100, "status": "Completado"}
    ],
    "2. DURANTE (Ejecución)": [
        {"area": "Gestión y Alianzas", "lead": "Equipo Gestión", "progress": 90, "status": "En Progreso"},
        {"area": "Logística Operativa", "lead": "Equipo Logística", "progress": 100, "status": "Completado"},
        {"area": "Comunicaciones", "lead": "Equipo Comms", "progress": 100, "status": "Completado"}
    ],
    "3. DESPUÉS (Cierre)": [
        {"area": "Gestión y Alianzas", "lead": "Equipo Gestión", "progress": 100, "status": "Pendiente"},
        {"area": "Logística de Cierre", "lead": "Equipo Logística", "progress": 100, "status": "Pendiente"},
        {"area": "Comunicaciones", "lead": "Equipo Comms", "progress": 100, "status": "Pendiente"}
    ]
}

# --- 5. PESTAÑAS (TABS) ---
tab1, tab2, tab3 = st.tabs(["📊 Resumen", "⏱️ Cronograma", "🤝 Aliados"])

# TAB 1: RESUMEN
with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Asistentes", "200+", "100% Meta")
    c2.metric("Aliados", "17", "Confirmados")
    c3.metric("Satisfacción", "4.8/5", "Alta")
    
    st.success("**✅ FORTALEZAS:** Trabajo en equipo, Identidad clara.")
    st.warning("**⚠️ DEBILIDADES:** Recursos limitados, Tiempos ajustados.")

# TAB 2: CRONOGRAMA
with tab2:
    fase = st.selectbox("Selecciona Fase:", list(phases.keys()))
    st.markdown(f"### Viendo: {fase}")
    for item in phases[fase]:
        st.write(f"**{item['area']}** (Líderes: {item['lead']})")
        st.progress(item['progress'] / 100)
        st.caption(f"Estado: {item['status']}")
        st.divider()

# TAB 3: ALIADOS
with tab3:
    st.subheader("Matriz de Aliados")
    df = pd.DataFrame({
        "Aliado": ["Universidades", "Empresas Insumos", "Cooperativas Café", "IPS y Brigadas"],
        "Gestión": ["Cartas y Visitas", "Llamadas", "Gestión Especie", "Convenios"],
        "Estado": ["Confirmado", "Confirmado", "Confirmado", "Parcial"]
    })
    st.table(df)
