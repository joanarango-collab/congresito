import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="XI Congreso Prehospitalaria", layout="wide", page_icon="☕")

# --- 2. ESTILOS CSS (IDÉNTICO AL DISEÑO ORIGINAL) ---
st.markdown("""
<style>
    /* Fuentes e importaciones */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    .stApp {
        background-color: #f5f5f4; /* bg-stone-100 */
        font-family: 'Inter', sans-serif;
        color: #292524; /* text-stone-800 */
    }

    /* Estilos de Tarjetas (Cards) */
    .card {
        background-color: white;
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid #e7e5e4;
        margin-bottom: 1.5rem;
        overflow: hidden;
    }

    /* Bordes superiores de colores */
    .border-top-blue { border-top: 4px solid #2563eb; }
    .border-top-amber { border-top: 4px solid #d97706; }
    .border-top-green { border-top: 4px solid #16a34a; }

    /* Utilidades de Texto */
    .font-bold { font-weight: 700; }
    .text-xs { font-size: 0.75rem; }
    .text-sm { font-size: 0.875rem; }
    .uppercase { text-transform: uppercase; }
    .text-stone-500 { color: #78716c; }
    .text-stone-700 { color: #44403c; }

    /* Header Principal */
    .header-container {
        background: linear-gradient(to right, #1c1917, #0c0a09); /* stone-900 gradients */
        border-bottom: 8px solid #d97706; /* border-amber-600 */
        border-radius: 1rem;
        padding: 2.5rem;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }

    /* Estilos para Tablas */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.875rem;
    }
    .custom-table th {
        text-align: left;
        padding: 0.75rem 1.5rem;
        background-color: #fafaf9;
        color: #78716c;
        text-transform: uppercase;
        font-size: 0.75rem;
        border-bottom: 1px solid #e7e5e4;
        font-weight: 700;
    }
    .custom-table td {
        padding: 1rem 1.5rem;
        border-bottom: 1px solid #f5f5f4;
        vertical-align: middle;
    }

    /* Badges (Etiquetas) */
    .badge { padding: 2px 10px; border-radius: 9999px; font-weight: 700; font-size: 0.7rem; text-transform: uppercase; }
    .badge-green { background-color: #dcfce7; color: #166534; }
    .badge-amber { background-color: #fef3c7; color: #92400e; }

    /* Ajustes de Streamlit */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: #e7e5e4; padding: 5px; border-radius: 999px; display: inline-flex; }
    .stTabs [data-baseweb="tab"] { border-radius: 999px; padding: 8px 16px; border: none; background-color: transparent; }
    .stTabs [aria-selected="true"] { background-color: #d97706 !important; color: white !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATOS DEL EVENTO ---
phases = {
    "antes": [
        {
            "name": "Gestión y Alianzas", "lead": "David Muñoz & Andrés Álvarez", "icon": "💼", "color": "blue",
            "stats": [("Base de Datos", "56 Contactos"), ("Aliados", "17 Empresas"), ("Meta", "90% Logrado")],
            "tasks": [
                {"activity": "Base de Datos Aliados", "progress": 100, "details": "Mapeo de 56 entidades (IPS, UTP)."},
                {"activity": "Solicitud de Insumos", "progress": 95, "details": "Gestión de café, refrigerios."},
                {"activity": "Invitaciones Oficiales", "progress": 100, "details": "Cartas a universidades."}
            ]
        },
        {
            "name": "Logística y Ambientación", "lead": "Santiago Rendón & Leymar Portilla", "icon": "🛠️", "color": "amber",
            "stats": [("Decoración", "Identidad Cafetera"), ("Certificados", "Diseño Listo"), ("Insumos", "100% Gestionados")],
            "tasks": [
                {"activity": "Escenografía Cafetera", "progress": 100, "details": "Elementos en cartón y pintura."},
                {"activity": "Requerimientos Técnicos", "progress": 100, "details": "Recolección presentaciones."},
                {"activity": "Mobiliario Stands", "progress": 100, "details": "Mesas y sillas aseguradas."}
            ]
        },
        {
            "name": "Comunicaciones", "lead": "Joan Sebastian Arango", "icon": "📢", "color": "green",
            "stats": [("Línea Gráfica", "Definida"), ("Campaña", "Lanzada"), ("Redes", "Activas")],
            "tasks": [
                {"activity": "Manual de Marca", "progress": 100, "details": "Paleta visual cafetera."},
                {"activity": "Campaña Expectativa", "progress": 100, "details": "Teaser y flyers."},
                {"activity": "Diseño Escarapelas", "progress": 100, "details": "Identificación staff."}
            ]
        }
    ],
    "durante": [
        {
            "name": "Gestión y Alianzas", "lead": "Equipo Gestión", "icon": "💼", "color": "blue",
            "stats": [("Stands Activos", "17 Stands"), ("Refrigerios", "Distribuidos"), ("Satisfacción", "Alta")],
            "tasks": [
                {"activity": "Supervisión de Stands", "progress": 100, "details": "Verificación montaje."},
                {"activity": "Logística Alimentación", "progress": 100, "details": "Entrega refrigerios."},
                {"activity": "Registro de Marcas", "progress": 90, "details": "Evidencia visual."}
            ]
        },
        {
            "name": "Logística Operativa", "lead": "Equipo Logística", "icon": "🎧", "color": "amber",
            "stats": [("Sedes", "Auditorio + Edif 14"), ("Incidencias", "Mínimas"), ("Tiempos", "Cumplidos")],
            "tasks": [
                {"activity": "Soporte Audiovisual", "progress": 100, "details": "Pruebas sonido."},
                {"activity": "Protocolo Ponentes", "progress": 100, "details": "Acompañamiento tarima."},
                {"activity": "Flujo de Asistentes", "progress": 100, "details": "Control acceso."}
            ]
        },
        {
            "name": "Comunicaciones", "lead": "Equipo Comms", "icon": "📸", "color": "green",
            "stats": [("Cobertura", "En Vivo"), ("Entrevistas", "Realizadas"), ("Stories", "+50 Publicadas")],
            "tasks": [
                {"activity": "Registro Fotográfico", "progress": 100, "details": "Cobertura completa."},
                {"activity": "Gestión Redes", "progress": 100, "details": "Minuto a minuto."},
                {"activity": "Entrevistas", "progress": 100, "details": "Testimonios."}
            ]
        }
    ],
    "despues": [
        {
            "name": "Gestión y Alianzas", "lead": "Equipo Gestión", "icon": "💼", "color": "blue",
            "stats": [("Agradecimientos", "Enviados"), ("Informe", "Entregado"), ("Relaciones", "Consolidadas")],
            "tasks": [
                {"activity": "Cartas Agradecimiento", "progress": 100, "details": "Envío a 17 aliados."},
                {"activity": "Informe Gestión", "progress": 100, "details": "Balance impacto."},
                {"activity": "Devolución Bienes", "progress": 100, "details": "Retorno mobiliario."}
            ]
        },
        {
            "name": "Logística de Cierre", "lead": "Equipo Logística", "icon": "📦", "color": "amber",
            "stats": [("Certificados", "Distribuidos"), ("Inventario", "Paz y Salvo"), ("Desmontaje", "Total")],
            "tasks": [
                {"activity": "Certificación Digital", "progress": 100, "details": "Envío masivo."},
                {"activity": "Desmontaje", "progress": 100, "details": "Retiro decoración."},
                {"activity": "Informe Final", "progress": 100, "details": "Evaluación operativa."}
            ]
        },
        {
            "name": "Comunicaciones", "lead": "Equipo Comms", "icon": "💾", "color": "green",
            "stats": [("Memorias", "Publicadas"), ("Aftermovie", "Editado"), ("Álbum", "Online")],
            "tasks": [
                {"activity": "Post-Producción", "progress": 100, "details": "Video resumen."},
                {"activity": "Memorias Académicas", "progress": 100, "details": "Compilación PDF."},
                {"activity": "Informe Métricas", "progress": 100, "details": "Análisis alcance."}
            ]
        }
    ]
}

# --- 4. HEADER PRINCIPAL ---
st.markdown("""
<div class="header-container">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <div style="display: inline-flex; align-items: center; background: rgba(217,119,6,0.2); color: #fbbf24; padding: 4px 12px; border-radius: 9999px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; border: 1px solid rgba(251, 191, 36, 0.5); margin-bottom: 1rem;">
                <span style="margin-right: 6px;">☕</span> Edición Especial
            </div>
            <h1 style="font-size: 3rem; font-weight: 800; margin: 0; line-height: 1; text-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                XI Congreso Nacional<br>
                <span style="color: #f59e0b;">Medicina Prehospitalaria</span>
            </h1>
            <p style="color: #d6d3d1; font-style: italic; font-size: 1.25rem; margin-top: 1rem; font-weight: 500;">"Identidad Cafetera en la Emergencia"</p>
            <div style="margin-top: 2rem; display: flex; gap: 1rem;">
                <span style="display: flex; align-items: center; background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 0.75rem; font-size: 0.875rem; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
                    📅 23-25 Octubre 2025
                </span>
                <span style="display: flex; align-items: center; background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 0.75rem; font-size: 0.875rem; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
                    📍 Aud. Jorge Roa & Edif. 14
                </span>
            </div>
        </div>
        <div style="display: flex; gap: 1rem;">
             <div style="text-align: center; background: rgba(217, 119, 6, 0.9); padding: 1.5rem; border-radius: 1rem; backdrop-filter: blur(8px); border: 1px solid rgba(217, 119, 6, 0.5); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);">
                 <div style="font-size: 2.5rem; margin-bottom: 0.25rem; opacity: 0.9;">👥</div>
                 <div style="font-weight: 800; font-size: 1.875rem; line-height: 1;">200+</div>
                 <div style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; font-weight: 700; margin-top: 0.25rem;">Asistentes</div>
             </div>
             <div style="text-align: center; background: rgba(41, 37, 36, 0.9); padding: 1.5rem; border-radius: 1rem; backdrop-filter: blur(8px); border: 1px solid rgba(68, 64, 60, 0.5); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);">
                 <div style="font-size: 2.5rem; margin-bottom: 0.25rem; opacity: 0.9; color: #4ade80;">🤝</div>
                 <div style="font-weight: 800; font-size: 1.875rem; line-height: 1;">17</div>
                 <div style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; font-weight: 700; margin-top: 0.25rem;">Aliados</div>
             </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. NAVEGACIÓN PRINCIPAL ---
tab1, tab2, tab3 = st.tabs(["📈 Resumen & DOFA", "⏱️ Cronograma (Fases)", "🤝 Matriz Aliados"])

# --- TAB 1: RESUMEN ---
with tab1:
    # Tarjetas de KPIs
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="card" style="padding: 1.5rem; border-left: 4px solid #22c55e;">
            <div class="text-xs font-bold text-stone-500 uppercase">Asistencia vs Meta</div>
            <div style="font-size: 1.875rem; font-weight: 800; color: #166534; margin: 0.5rem 0;">100%</div>
            <div style="height: 8px; background: #dcfce7; border-radius: 99px; overflow: hidden;"><div style="width: 100%; height: 100%; background: #22c55e;"></div></div>
            <div class="text-xs text-stone-500" style="margin-top: 0.5rem;">200 participantes certificados</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card" style="padding: 1.5rem; border-left: 4px solid #d97706;">
            <div class="text-xs font-bold text-stone-500 uppercase">Cumplimiento Cronograma</div>
            <div style="font-size: 1.875rem; font-weight: 800; color: #92400e; margin: 0.5rem 0;">98%</div>
            <div style="height: 8px; background: #fef3c7; border-radius: 99px; overflow: hidden;"><div style="width: 98%; height: 100%; background: #d97706;"></div></div>
            <div class="text-xs text-stone-500" style="margin-top: 0.5rem;">Actividades ejecutadas a tiempo</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="card" style="padding: 1.5rem; border-left: 4px solid #2563eb;">
            <div class="text-xs font-bold text-stone-500 uppercase">Satisfacción Aliados</div>
            <div style="font-size: 1.875rem; font-weight: 800; color: #1e40af; margin: 0.5rem 0;">90%</div>
            <div style="height: 8px; background: #dbeafe; border-radius: 99px; overflow: hidden;"><div style="width: 90%; height: 100%; background: #2563eb;"></div></div>
            <div class="text-xs text-stone-500" style="margin-top: 0.5rem;">17 Empresas vinculadas</div>
        </div>""", unsafe_allow_html=True)

    # DOFA (Layout 2x2)
    st.markdown("<h3 style='font-weight: 800; color: #78350f; margin-top: 2rem; margin-bottom: 1.5rem;'>🦁 Análisis de Impacto (DOFA)</h3>", unsafe_allow_html=True)
    
    d_col1, d_col2 = st.columns(2)
    with d_col1:
        st.markdown("""
        <div class="card" style="padding: 1.5rem; background-color: #f0fdf4; border: 1px solid #bbf7d0; display: flex; gap: 1rem;">
            <div style="font-size: 1.5rem;">🏆</div>
            <div>
                <h4 style="color: #166534; margin: 0 0 0.5rem 0; font-weight: 700;">Fortalezas</h4>
                <ul style="color: #15803d; font-size: 0.875rem; margin: 0; padding-left: 1.2rem; line-height: 1.5;">
                    <li>Trabajo en equipo y liderazgo</li>
                    <li>Identidad Cafetera clara</li>
                    <li>Capacidad de adaptación</li>
                    <li>17 Aliados confirmados</li>
                </ul>
            </div>
        </div>
        <div class="card" style="padding: 1.5rem; background-color: #eff6ff; border: 1px solid #bfdbfe; display: flex; gap: 1rem;">
            <div style="font-size: 1.5rem;">🚀</div>
            <div>
                <h4 style="color: #1e40af; margin: 0 0 0.5rem 0; font-weight: 700;">Oportunidades</h4>
                <ul style="color: #1d4ed8; font-size: 0.875rem; margin: 0; padding-left: 1.2rem; line-height: 1.5;">
                    <li>Posicionar a Pereira como eje académico</li>
                    <li>Alianzas con nuevos emprendimientos</li>
                    <li>Expandir cobertura digital</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with d_col2:
        st.markdown("""
        <div class="card" style="padding: 1.5rem; background-color: #fef2f2; border: 1px solid #fecaca; display: flex; gap: 1rem;">
            <div style="font-size: 1.5rem;">⚠️</div>
            <div>
                <h4 style="color: #991b1b; margin: 0 0 0.5rem 0; font-weight: 700;">Debilidades</h4>
                <ul style="color: #b91c1c; font-size: 0.875rem; margin: 0; padding-left: 1.2rem; line-height: 1.5;">
                    <li>Recursos técnicos limitados</li>
                    <li>Tiempos ajustados en piezas gráficas</li>
                    <li>Presupuesto dependiente de gestión</li>
                </ul>
            </div>
        </div>
        <div class="card" style="padding: 1.5rem; background-color: #fffbeb; border: 1px solid #fde68a; display: flex; gap: 1rem;">
            <div style="font-size: 1.5rem;">🎯</div>
            <div>
                <h4 style="color: #92400e; margin: 0 0 0.5rem 0; font-weight: 700;">Amenazas</h4>
                <ul style="color: #b45309; font-size: 0.875rem; margin: 0; padding-left: 1.2rem; line-height: 1.5;">
                    <li>Imprevistos logísticos de última hora</li>
                    <li>Ausencia de ponentes (riesgo latente)</li>
                    <li>Fallas técnicas en auditorio</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: CRONOGRAMA (CORREGIDO) ---
with tab2:
    # Selector centrado
    c_spacer1, c_select, c_spacer2 = st.columns([1, 2, 1])
    with c_select:
        selected_phase_key = st.selectbox("Seleccionar Fase", ["antes", "durante", "despues"], format_func=lambda x: {"antes": "1. PRE (Antes)", "durante": "2. PRO (Durante)", "despues": "3. POST (Después)"}[x], label_visibility="collapsed")
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # Grid de Comisiones
    cols_cronograma = st.columns(3)
    for idx, commission in enumerate(phases[selected_phase_key]):
        with cols_cronograma[idx]:
            # Construcción del HTML de tareas (SIN SANGRÍA PARA EVITAR ERROR)
            tasks_html = ""
            for t in commission['tasks']:
                color_bar = "#22c55e" if t['progress'] == 100 else "#fbbf24"
                tasks_html += f"""<div style="margin-bottom: 16px; padding-left: 16px; border-left: 2px solid #e7e5e4; position: relative;"><div style="position: absolute; left: -5px; top: 6px; width: 8px; height: 8px; border-radius: 50%; background-color: {color_bar};"></div><div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;"><span style="font-weight: 600; color: #44403c; font-size: 0.875rem;">{t['activity']}</span><span style="font-size: 0.75rem; font-weight: 700; color: {color_bar};">{t['progress']}%</span></div><p style="margin: 0; font-size: 0.75rem; color: #78716c; line-height: 1.4;">{t['details']}</p></div>"""

            # Renderizado de la Tarjeta (SIN SANGRÍA EN EL HTML INTERNO)
            st.markdown(f"""<div class="card border-top-{commission['color']}"><div style="padding: 1.5rem; background-color: #fafaf9; border-bottom: 1px solid #e7e5e4;"><div style="display: flex; justify-content: space-between; align-items: flex-start;"><div style="background: white; padding: 8px; border-radius: 10px; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); font-size: 1.5rem; color: {commission['color']};">{commission['icon']}</div><span style="font-size: 0.65rem; font-weight: 700; text-transform: uppercase; background: white; padding: 4px 10px; border-radius: 999px; border: 1px solid #e7e5e4; color: #78716c; letter-spacing: 0.05em;">Comisión</span></div><h3 style="margin-top: 1rem; font-size: 1.125rem; font-weight: 700; color: #1c1917; margin-bottom: 0.25rem;">{commission['name']}</h3><div style="font-size: 0.75rem; font-weight: 500; color: #78716c; display: flex; align-items: center;"><span style="margin-right: 4px;">👤</span> {commission['lead']}</div></div><div style="padding: 1.5rem 1.5rem 0.5rem 1.5rem;"><div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 1.5rem;">{ "".join([f"<div style='text-align: center; padding: 8px; background: #fafaf9; border-radius: 8px; border: 1px solid #e7e5e4;'><p style='margin: 0; font-size: 0.6rem; font-weight: 700; text-transform: uppercase; color: #a8a29e; letter-spacing: 0.05em;'>{s[0]}</p><p style='margin: 4px 0 0 0; font-size: 0.8rem; font-weight: 700; color: #44403c;'>{s[1]}</p></div>" for s in commission['stats']]) }</div>{tasks_html}</div></div>""", unsafe_allow_html=True)

# --- TAB 3: ALIADOS ---
with tab3:
    st.markdown("""
    <div class="card">
        <div style="padding: 1.5rem; background: linear-gradient(to right, #eff6ff, white); border-bottom: 1px solid #e7e5e4;">
            <h3 style="color: #1e40af; margin: 0; display: flex; align-items: center; font-weight: 700;">
                <span style="margin-right: 8px; font-size: 1.5rem;">🤝</span> Matriz de Gestión de Alianzas
            </h3>
            <p style="margin: 8px 0 0 0; color: #64748b; font-size: 0.875rem;">Resumen de los 17 aliados estratégicos gestionados.</p>
        </div>
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="padding-left: 2rem;">Tipo de Aliado</th>
                    <th>Gestión</th>
                    <th style="text-align: center;">Estado</th>
                    <th style="text-align: right; padding-right: 2rem;">Aporte Principal</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding-left: 2rem; font-weight: 600; color: #1c1917;">Universidades (Pereira)</td>
                    <td>Cartas y visitas</td>
                    <td style="text-align: center;"><span class="badge badge-green">Confirmado</span></td>
                    <td style="text-align: right; padding-right: 2rem;">Difusión y Aval Académico</td>
                </tr>
                <tr>
                    <td style="padding-left: 2rem; font-weight: 600; color: #1c1917;">Empresas de Insumos</td>
                    <td>Llamadas y Propuestas</td>
                    <td style="text-align: center;"><span class="badge badge-green">Confirmado</span></td>
                    <td style="text-align: right; padding-right: 2rem;">Stands y Muestras</td>
                </tr>
                <tr>
                    <td style="padding-left: 2rem; font-weight: 600; color: #1c1917;">Cooperativas de Café</td>
                    <td>Gestión en especie</td>
                    <td style="text-align: center;"><span class="badge badge-green">Confirmado</span></td>
                    <td style="text-align: right; padding-right: 2rem;">Decoración y Refrigerios</td>
                </tr>
                <tr>
                    <td style="padding-left: 2rem; font-weight: 600; color: #1c1917;">IPS y Brigadas</td>
                    <td>Convenios</td>
                    <td style="text-align: center;"><span class="badge badge-amber">Parcial</span></td>
                    <td style="text-align: right; padding-right: 2rem;">Apoyo en Simulacros</td>
                </tr>
                <tr style="background-color: #fafaf9;">
                    <td colspan="3" style="text-align: right; padding-right: 1rem; font-weight: 700; font-size: 0.875rem;">TOTAL ALIADOS ACTIVOS:</td>
                    <td style="text-align: right; padding-right: 2rem; color: #1d4ed8; font-weight: 800; font-size: 0.875rem;">17 ENTIDADES</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
