import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="XI Congreso Prehospitalaria",
    layout="wide",
    page_icon="☕"
)

# 2. ESTILOS CSS (Tema Cafetero)
st.markdown("""
    <style>
    .main {background-color: #f5f5f4;}
    h1 {color: #78350f;}
    h3 {color: #92400e;}
    .stProgress > div > div > div > div {background-color: #d97706;}
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e7e5e4;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #d97706;
    }
    </style>
""", unsafe_allow_html=True)

# 3. DATOS DEL PROYECTO
phases = {
    "1. ANTES (Preparación)": [
        {"area": "Gestión y Alianzas", "lead": "David & Andrés", "progress": 100, "details": "Base de datos (56 contactos), Insumos, Invitaciones."},
        {"area": "Logística y Ambientación", "lead": "Santiago & Leymar", "progress": 100, "details": "Escenografía Cafetera, Técnica, Mobiliario."},
        {"area": "Comunicaciones", "lead": "Joan Sebastian", "progress": 100, "details": "Manual de Marca, Campaña, Escarapelas."}
    ],
    "2. DURANTE (Ejecución)": [
        {"area": "Gestión y Alianzas", "lead": "Equipo Gestión", "progress": 90, "details": "Supervisión Stands, Refrigerios, Registro Marcas."},
        {"area": "Logística Operativa", "lead": "Equipo Logística", "progress": 100, "details": "Audiovisuales, Protocolo Ponentes, Flujo Asistentes."},
        {"area": "Comunicaciones", "lead": "Equipo Comms", "progress": 100, "details": "Fotos en vivo, Redes Sociales, Entrevistas."}
    ],
    "3. DESPUÉS (Cierre)": [
        {"area": "Gestión y Alianzas", "lead": "Equipo Gestión", "progress": 100, "details": "Cartas agradecimiento, Devolución bienes."},
        {"area": "Logística de Cierre", "lead": "Equipo Logística", "progress": 100, "details": "Certificados, Desmontaje, Inventario."},
        {"area": "Comunicaciones", "lead": "Equipo Comms", "progress": 100, "details": "Video resumen, Memorias, Informe final."}
    ]
}

# 4. ENCABEZADO
col_logo, col_titulo = st.columns([1, 5])
with col_titulo:
    st.title("XI Congreso Nacional Medicina Prehospitalaria")
    st.markdown("### *Identidad Cafetera en la Emergencia* ☕")
    st.caption("📍 Pereira | 📅 23-25 Octubre 2025 | Aud. Jorge Roa & Edif 14")

st.divider()

# 5. PESTAÑAS DE NAVEGACIÓN
tab1, tab2, tab3 = st.tabs(["📊 Resumen & DOFA", "⏱️ Cronograma", "🤝 Aliados"])

# --- TAB 1: RESUMEN ---
with tab1:
    # Métricas
    c1, c2, c3 = st.columns(3)
    c1.metric("Asistentes Certificados", "200+", "100% Meta")
    c2.metric("Aliados Estratégicos", "17", "Confirmados")
    c3.metric("Satisfacción General", "4.8/5", "Alta")
    
    st.markdown("---")
    
    # DOFA
    st.subheader("Análisis Estratégico (DOFA)")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.success("**✅ FORTALEZAS:** Liderazgo, Identidad clara, Capacidad de adaptación.")
        st.info("**🔵 OPORTUNIDADES:** Posicionar Pereira, Nuevas alianzas académicas.")
    with col_d2:
        st.warning("**⚠️ DEBILIDADES:** Recursos técnicos limitados, Tiempos ajustados.")
        st.error("**🛑 AMENAZAS:** Imprevistos logísticos, Cancelación de ponentes.")

# --- TAB 2: CRONOGRAMA ---
with tab2:
    st.subheader("Seguimiento por Fases")
    fase_selected = st.selectbox("Selecciona la Fase:", list(phases.keys()))
    
    st.markdown(f"### 📂 Viendo: {fase_selected}")
    for tarea in phases[fase_selected]:
        with st.container():
            st.markdown(f"**{tarea['area']}** (Líderes: {tarea['lead']})")
            st.progress(tarea['progress'] / 100)
            st.caption(f"Detalles: {tarea['details']}")
            st.markdown("---")

# --- TAB 3: ALIADOS ---
with tab3:
    st.subheader("Matriz de Aliados (17 Entidades)")
    datos_aliados = pd.DataFrame({
        "Aliado": ["Universidades Pereira", "Empresas Insumos", "Cooperativas Café", "IPS y Brigadas"],
        "Gestión Realizada": ["Cartas y Visitas", "Llamadas Comerciales", "Gestión Especie", "Convenios"],
        "Estado": ["Confirmado", "Confirmado", "Confirmado", "Parcial"],
        "Aporte": ["Aval Académico", "Stands", "Refrigerios", "Simulacros"]
    })
    st.table(datos_aliados)

export default DashboardCongreso;
