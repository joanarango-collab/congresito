import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="XI Congreso Prehospitalaria",
    layout="wide",
    page_icon="☕"
)

# --- ESTILOS CSS AVANZADOS (DISEÑO REACT) ---
st.markdown("""
    <style>
    /* Fondo General */
    .stApp {
        background-color: #f5f5f4;
    }
    
    /* Estilo para las Tarjetas (Cards) */
    .custom-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-top: 4px solid #d97706;
        margin-bottom: 20px;
    }
    
    /* Estilo del Header */
    .header-box {
        background: linear-gradient(to right, #1c1917, #451a03);
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

# --- NAVEGACIÓN (AQUÍ ESTABA EL ERROR ANTES) ---
tab1, tab2, tab3 = st.tabs(["📈 RESUMEN & DOFA", "⏱️ CRONOGRAMA", "🤝 MATRIZ ALIADOS"])

# --- TAB 1: RESUMEN (TARJETAS BONITAS) ---
with tab1:
    # Fila de Métricas
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="custom-card" style="border-color: #22c55e;">
            <div class="metric-label">Asistentes Certificados</div>
            <div class="metric-value">200+</div>
            <div style="color: #22c55e; font-size: 12px; margin-top: 5px;">▲ 100% de la Meta</div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="custom-card" style="border-color: #3b82f6;">
            <div class="metric-label">Aliados Estratégicos</div>
            <div class="metric-value">17</div>
            <div style="color: #3b82f6; font-size: 12px; margin-top: 5px;">Empresas Confirmadas</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="custom-card" style="border-color: #d97706;">
            <div class="metric-label">Satisfacción</div>
            <div class="metric-value">4.9/5</div>
            <div style="color: #d97706; font-size: 12px; margin-top: 5px;">Feedback Post-Evento</div>
        </div>
        """, unsafe_allow_html=True)

    # DOFA
    st.markdown("### 🦁 Análisis Estratégico (DOFA)")
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        st.markdown("""
        <div class="custom-card" style="border-left: 5px solid #22c55e;">
            <h4 style="color: #15803d; margin-top:0;">✅ FORTALEZAS</h4>
            <ul style="color: #44403c;">
                <li>Trabajo en equipo y liderazgo consolidado.</li>
                <li>Identidad Cafetera clara y diferenciadora.</li>
                <li>Capacidad de adaptación ante cambios.</li>
            </ul>
        </div>
        <div class="custom-card" style="border-left: 5px solid #3b82f6;">
            <h4 style="color: #1d4ed8; margin-top:0;">🔵 OPORTUNIDADES</h4>
            <ul style="color: #44403c;">
                <li>Posicionar a Pereira como eje académico nacional.</li>
                <li>Alianzas con nuevos emprendimientos locales.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_d2:
        st.markdown("""
        <div class="custom-card" style="border-left: 5px solid #f59e0b;">
            <h4 style="color: #b45309; margin-top:0;">⚠️ DEBILIDADES</h4>
            <ul style="color: #44403c;">
                <li>Recursos técnicos limitados en la U.</li>
                <li>Tiempos ajustados para piezas gráficas.</li>
            </ul>
        </div>
        <div class="custom-card" style="border-left: 5px solid #ef4444;">
            <h4 style="color: #b91c1c; margin-top:0;">🛑 AMENAZAS</h4>
            <ul style="color: #44403c;">
                <li>Imprevistos logísticos de última hora.</li>
                <li>Riesgo latente de cancelación de ponentes.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: CRONOGRAMA (ESTILO TIMELINE) ---
with tab2:
    st.markdown("### 📅 Seguimiento de Fases")
    
    # Selector de fase estilizado
    fase_seleccionada = st.selectbox("Seleccionar Fase:", 
        ["1. PRE (Preparación)", "2. PRO (Ejecución)", "3. POST (Cierre)"])
    
    # Datos simulados para visualización
    tasks = {
        "1. PRE (Preparación)": [
            {"title": "Gestión y Alianzas", "lead": "David & Andrés", "prog": 100, "color": "#3b82f6", "icon": "💼", "desc": "Base de datos, Insumos, Cartas oficiales."},
            {"title": "Logística y Ambientación", "lead": "Santiago & Leymar", "prog": 100, "color": "#d97706", "icon": "🛠️", "desc": "Escenografía cafetera, Mobiliario stands."},
            {"title": "Comunicaciones", "lead": "Joan Sebastian", "prog": 100, "color": "#22c55e", "icon": "📢", "desc": "Manual de marca, Campaña expectativa."}
        ],
        "2. PRO (Ejecución)": [
            {"title": "Gestión (Durante)", "lead": "Equipo Gestión", "prog": 90, "color": "#3b82f6", "icon": "🤝", "desc": "Supervisión stands y refrigerios."},
            {"title": "Logística Operativa", "lead": "Equipo Logística", "prog": 100, "color": "#d97706", "icon": "🎧", "desc": "Soporte audiovisual y flujo asistentes."},
            {"title": "Comunicaciones Live", "lead": "Equipo Comms", "prog": 100, "color": "#22c55e", "icon": "📸", "desc": "Cobertura en vivo, stories y entrevistas."}
        ],
        "3. POST (Cierre)": [
            {"title": "Cierre Gestión", "lead": "Equipo Gestión", "prog": 100, "color": "#3b82f6", "icon": "📩", "desc": "Cartas de agradecimiento enviadas."},
            {"title": "Logística Salida", "lead": "Equipo Logística", "prog": 100, "color": "#d97706", "icon": "📦", "desc": "Desmontaje y limpieza total."},
            {"title": "Memorias", "lead": "Equipo Comms", "prog": 100, "color": "#22c55e", "icon": "💾", "desc": "Edición aftermovie y certificados."}
        ]
    }

    # Renderizar tarjetas de tareas
    current_tasks = tasks[fase_seleccionada]
    
    col_t1, col_t2, col_t3 = st.columns(3)
    
    for i, task in enumerate(current_tasks):
        with [col_t1, col_t2, col_t3][i]:
            st.markdown(f"""
            <div class="custom-card" style="border-top: 4px solid {task['color']}; min-height: 250px;">
                <div style="font-size: 30px; margin-bottom: 10px;">{task['icon']}</div>
                <h3 style="margin: 0; color: #44403c; font-size: 18px;">{task['title']}</h3>
                <p style="color: #78716c; font-size: 12px; font-weight: bold; margin-bottom: 15px;">Líderes: {task['lead']}</p>
                
                <div style="background-color: #e5e7eb; border-radius: 10px; height: 8px; width: 100%; margin-bottom: 5px;">
                    <div style="background-color: {task['color']}; width: {task['prog']}%; height: 8px; border-radius: 10px;"></div>
                </div>
                <div style="text-align: right; font-size: 12px; font-weight: bold; color: {task['color']};">{task['prog']}% Completado</div>
                
                <p style="margin-top: 15px; font-size: 13px; color: #57534e; line-height: 1.4;">
                    {task['desc']}
                </p>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 3: ALIADOS ---
with tab3:
    st.markdown("### 🤝 Matriz de Aliados Estratégicos")
    st.markdown("""
    <div class="custom-card">
        <p>Resumen de las 17 entidades gestionadas para el congreso.</p>
    </div>
    """, unsafe_allow_html=True)
    
    df_aliados = pd.DataFrame([
        ["Universidades (Pereira)", "Cartas y visitas", "✅ Confirmado", "Difusión y Aval"],
        ["Empresas de Insumos", "Llamadas", "✅ Confirmado", "Stands y Muestras"],
        ["Cooperativas de Café", "Gestión Especie", "✅ Confirmado", "Decoración y Café"],
        ["IPS y Brigadas", "Convenios", "⚠️ Parcial", "Apoyo Simulacros"],
        ["Marcas Locales", "Redes Sociales", "✅ Confirmado", "Premios Sorpresa"]
    ], columns=["Tipo de Aliado", "Gestión", "Estado", "Aporte Principal"])

    st.dataframe(
        df_aliados, 
        use_container_width=True,
        hide_index=True,
        column_config={
            "Estado": st.column_config.TextColumn(
                "Estado",
                help="Estado actual del convenio",
                width="medium"
            )
        }
    )

# --- FIN DEL DASHBOARD ---
