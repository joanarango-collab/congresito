import streamlit as st
import plotly.graph_objects as go

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="XI Congreso Prehospitalaria", 
    layout="wide", 
    page_icon="☕"
)

# --- 2. ESTILOS CSS (REPLICANDO EL DISEÑO REACT/TAILWIND) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .stApp {
        background-color: #f5f5f4; /* bg-stone-100 */
        font-family: 'Inter', sans-serif;
        color: #292524;
    }

    /* Ocultar elementos nativos de Streamlit que estorban */
    header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 5rem;}

    /* Clases de Utilidad estilo Tailwind */
    .card {
        background-color: white;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid #e7e5e4;
        margin-bottom: 1.5rem;
        overflow: hidden;
    }
    
    .shadow-lg { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }
    
    /* Bordes de colores */
    .border-t-blue { border-top: 4px solid #2563eb; }
    .border-t-amber { border-top: 4px solid #d97706; }
    .border-t-green { border-top: 4px solid #16a34a; }
    .border-l-blue { border-left: 8px solid #3b82f6; }
    .border-l-amber { border-left: 8px solid #d97706; }
    .border-l-green { border-left: 8px solid #22c55e; }
    .border-l-purple { border-left: 8px solid #7e22ce; }

    /* Header */
    .header-bg {
        background: linear-gradient(to right, #1c1917, #292524);
        border-bottom: 8px solid #d97706;
        border-radius: 1rem;
        color: white;
        padding: 2rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    /* Tablas Personalizadas */
    .custom-table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
    .custom-table th {
        background-color: #fafaf9;
        color: #78716c;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 0.75rem;
        padding: 1rem;
        text-align: left;
        border-bottom: 1px solid #e7e5e4;
    }
    .custom-table td {
        padding: 1rem;
        border-bottom: 1px solid #f5f5f4;
        color: #44403c;
        vertical-align: middle;
    }
    .custom-table tr:hover { background-color: #fafaf9; }

    /* Progress Bars Custom */
    .progress-track { background-color: #f3f4f6; border-radius: 99px; height: 8px; width: 100%; overflow: hidden; }
    .progress-fill-green { background-color: #16a34a; height: 100%; }
    .progress-fill-amber { background-color: #d97706; height: 100%; }
    .progress-fill-blue { background-color: #2563eb; height: 100%; }

    /* Badges */
    .badge { padding: 4px 10px; border-radius: 6px; font-weight: 700; font-size: 0.7rem; text-transform: uppercase; display: inline-block; }
    .badge-blue { background: #eff6ff; color: #1e40af; }
    .badge-amber { background: #fffbeb; color: #92400e; }
    .badge-green { background: #f0fdf4; color: #166534; }
    
</style>
""", unsafe_allow_html=True)

# --- 3. DATOS Y LÓGICA ---

# Datos de Gráficos (Tab 1)
aliados_data = {"labels": ["Insumos Médicos", "Universidades", "Café/Alimentos"], "values": [10, 4, 3], "colors": ['#1e40af', '#3b82f6', '#93c5fd']}
asistentes_data = {"labels": ["Estudiantes UTP", "Externos", "Staff/Ponentes"], "values": [140, 40, 20], "colors": ['#b45309', '#f59e0b', '#fcd34d']}
cumplimiento_data = [
    {"label": "Gestión Financiera", "value": 91},
    {"label": "Logística (Montaje)", "value": 98},
    {"label": "Comunicaciones", "value": 100},
    {"label": "Asistencia (Aforo)", "value": 100}
]

# Datos de Fases (Tabs 2, 3, 4)
phases = {
    "antes": [
        {
            "name": "Gestión y Alianzas", "lead": "David Muñoz & Andrés Álvarez", "icon": "💼", "color": "text-blue-700", "bg": "bg-blue-50", "border": "border-l-blue",
            "indicators": [
                {"item": "Base de Datos Aliados", "meta": "1 BD", "ejec": "1 BD", "perc": 100},
                {"item": "Contactar Empresas Insumos", "meta": "11", "ejec": "10", "perc": 91},
                {"item": "Contactar IPS/Brigadas", "meta": "12", "ejec": "7", "perc": 58},
                {"item": "Gestión Universidades", "meta": "5", "ejec": "5", "perc": 100}
            ]
        },
        {
            "name": "Logística", "lead": "Santiago Rendón & Leymar Portilla", "icon": "🛠️", "color": "text-amber-700", "bg": "bg-amber-50", "border": "border-l-amber",
            "indicators": [
                {"item": "Contactar Ponentes", "meta": "20", "ejec": "20", "perc": 100},
                {"item": "Diseño Certificados", "meta": "1", "ejec": "1", "perc": 100},
                {"item": "Gestión Mobiliario", "meta": "100%", "ejec": "100%", "perc": 100},
                {"item": "Decoración Cafetera", "meta": "50 ítems", "ejec": "50", "perc": 100}
            ]
        },
        {
            "name": "Comunicaciones", "lead": "Joan Sebastian Arango", "icon": "📢", "color": "text-green-700", "bg": "bg-green-50", "border": "border-l-green",
            "indicators": [
                {"item": "Manual de Marca", "meta": "1", "ejec": "1", "perc": 100},
                {"item": "Campaña Expectativa", "meta": "3 Olas", "ejec": "3 Olas", "perc": 100},
                {"item": "Video Teaser", "meta": "1", "ejec": "1", "perc": 100},
                {"item": "Diseño Escarapelas", "meta": "3 Tipos", "ejec": "3 Tipos", "perc": 100}
            ]
        }
    ],
    "durante": [
        {
            "name": "Gestión y Alianzas", "lead": "Equipo Gestión", "icon": "💼", "color": "text-blue-700", "bg": "bg-blue-50", "border": "border-l-blue",
            "indicators": [
                {"item": "Supervisión Stands", "meta": "15", "ejec": "15", "perc": 100},
                {"item": "Entrega Refrigerios", "meta": "200", "ejec": "200", "perc": 100},
                {"item": "Registro Aliados", "meta": "17", "ejec": "15", "perc": 88}
            ]
        },
        {
            "name": "Logística", "lead": "Equipo Logística", "icon": "🛠️", "color": "text-amber-700", "bg": "bg-amber-50", "border": "border-l-amber",
            "indicators": [
                {"item": "Soporte Auditorio", "meta": "100%", "ejec": "100%", "perc": 100},
                {"item": "Control Asistencia", "meta": "200", "ejec": "200", "perc": 100},
                {"item": "Talleres Edif. 14", "meta": "6", "ejec": "6", "perc": 100}
            ]
        },
        {
            "name": "Comunicaciones", "lead": "Equipo Comunicaciones", "icon": "📢", "color": "text-green-700", "bg": "bg-green-50", "border": "border-l-green",
            "indicators": [
                {"item": "Cobertura Ponencias", "meta": "12", "ejec": "12", "perc": 100},
                {"item": "Entrevistas", "meta": "10", "ejec": "8", "perc": 80},
                {"item": "Stories en Vivo", "meta": "50", "ejec": "50+", "perc": 100}
            ]
        }
    ],
    "despues": [
        {
            "name": "Cierre General", "lead": "Todas las Comisiones", "icon": "✅", "color": "text-purple-700", "bg": "bg-purple-50", "border": "border-l-purple",
            "indicators": [
                {"item": "Cartas Agradecimiento", "meta": "17", "ejec": "17", "perc": 100},
                {"item": "Certificados Enviados", "meta": "200", "ejec": "200", "perc": 100},
                {"item": "Memorias Digitales", "meta": "1 Pack", "ejec": "1 Pack", "perc": 100},
                {"item": "Informe Final", "meta": "1", "ejec": "1", "perc": 100}
            ]
        }
    ]
}

# --- FUNCIONES DE GRÁFICOS ---
def crear_dona(labels, values, colors, title):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7, 
                                 marker=dict(colors=colors), textinfo='value', hoverinfo='label+value')])
    fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=160,
                      annotations=[dict(text=title, x=0.5, y=0.5, font_size=12, showarrow=False)])
    return fig

# --- 4. ESTRUCTURA DE LA PÁGINA ---

# HEADER
st.markdown("""
<div class="header-bg">
    <div style="display: flex; gap: 2rem; align-items: center; flex-wrap: wrap;">
        <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 50%; border: 2px solid rgba(245, 158, 11, 0.5); width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; font-size: 3rem;">
            🚑
        </div>
        <div style="flex: 1;">
            <div style="display: inline-block; background: rgba(217, 119, 6, 0.3); border: 1px solid #d97706; color: #fbbf24; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 99px; text-transform: uppercase; margin-bottom: 0.5rem;">
                ☕ Edición Especial: Identidad Cafetera
            </div>
            <h1 style="margin: 0; font-size: 2.5rem; font-weight: 800; line-height: 1.1;">
                XI Congreso Nacional<br>
                <span style="color: #f59e0b;">Medicina Prehospitalaria</span>
            </h1>
            <div style="display: flex; gap: 1rem; margin-top: 1rem;">
                <span style="background: rgba(255,255,255,0.1); padding: 5px 10px; border-radius: 6px; font-size: 0.85rem;">📅 23-25 Octubre 2025</span>
                <span style="background: rgba(255,255,255,0.1); padding: 5px 10px; border-radius: 6px; font-size: 0.85rem;">📍 Aud. Jorge Roa & Edif. 14</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# TABS DE NAVEGACIÓN
tab1, tab2, tab3, tab4 = st.tabs(["📊 Visión General", "1️⃣ Pre-Evento", "2️⃣ Durante", "3️⃣ Post-Evento"])

# --- TAB 1: VISIÓN GENERAL ---
with tab1:
    col_g1, col_g2, col_g3 = st.columns(3)
    
    with col_g1:
        st.markdown('<div class="card shadow-lg border-t-blue" style="text-align: center; padding: 1rem;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #1e40af; font-size: 1.1rem; margin: 0;">Aliados Estratégicos</h3>', unsafe_allow_html=True)
        st.markdown('<p style="color: #6b7280; font-size: 0.8rem; margin-bottom: 1rem;">Total: 17 Entidades</p>', unsafe_allow_html=True)
        st.plotly_chart(crear_dona(aliados_data['labels'], aliados_data['values'], aliados_data['colors'], "Gestión"), use_container_width=True)
        # Leyenda manual
        st.markdown("""<div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; font-size: 0.7rem;">
            <span style="color: #1e40af">● Insumos (10)</span>
            <span style="color: #3b82f6">● Unis (4)</span>
            <span style="color: #93c5fd">● Café (3)</span>
        </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_g2:
        st.markdown('<div class="card shadow-lg border-t-amber" style="text-align: center; padding: 1rem;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #92400e; font-size: 1.1rem; margin: 0;">Asistencia</h3>', unsafe_allow_html=True)
        st.markdown('<p style="color: #6b7280; font-size: 0.8rem; margin-bottom: 1rem;">Total: ~200 Pax</p>', unsafe_allow_html=True)
        st.plotly_chart(crear_dona(asistentes_data['labels'], asistentes_data['values'], asistentes_data['colors'], "Aforo"), use_container_width=True)
        st.markdown("""<div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; font-size: 0.7rem;">
            <span style="color: #b45309">● UTP (140)</span>
            <span style="color: #f59e0b">● Ext (40)</span>
            <span style="color: #fcd34d">● Staff (20)</span>
        </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_g3:
        st.markdown('<div class="card shadow-lg border-t-green" style="padding: 1rem;">', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center;"><h3 style="color: #166534; font-size: 1.1rem; margin: 0;">Cumplimiento Global</h3><p style="color: #6b7280; font-size: 0.8rem; margin-bottom: 1rem;">Por áreas</p></div>', unsafe_allow_html=True)
        
        # Barras HTML
        for item in cumplimiento_data:
            st.markdown(f"""
            <div style="margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: 600; color: #374151;">
                    <span>{item['label']}</span>
                    <span>{item['value']}%</span>
                </div>
                <div class="progress-track">
                    <div class="progress-fill-green" style="width: {item['value']}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # DOFA
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("""
        <div class="card" style="padding: 1.5rem; background: #f0fdf4; border: 1px solid #bbf7d0;">
            <h4 style="color: #166534; margin: 0 0 10px 0; display: flex; align-items: center;">🏆 Fortalezas</h4>
            <ul style="color: #14532d; font-size: 0.85rem; padding-left: 1.2rem; margin: 0;">
                <li>Identidad Cafetera clara y transversal.</li>
                <li>Capacidad de gestión (17 aliados).</li>
                <li>Trabajo articulado entre comisiones.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_d2:
        st.markdown("""
        <div class="card" style="padding: 1.5rem; background: #fef2f2; border: 1px solid #fecaca;">
            <h4 style="color: #991b1b; margin: 0 0 10px 0; display: flex; align-items: center;">⚠️ Oportunidades de Mejora</h4>
            <ul style="color: #7f1d1d; font-size: 0.85rem; padding-left: 1.2rem; margin: 0;">
                <li>Mayor anticipación en piezas gráficas.</li>
                <li>Recursos técnicos propios limitados.</li>
                <li>Dependencia alta de gestión externa.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- FUNCION GENERADORA DE TABS DE FASE ---
def render_phase_tab(phase_key):
    for commission in phases[phase_key]:
        # Estilos dinámicos según el color de la comisión en los datos
        color_class = commission['color'] # ej: text-blue-700
        bg_class = commission['bg'] # ej: bg-blue-50
        border_class = commission['border'] # ej: border-l-blue
        
        # Mapa de colores para las barras internas
        bar_color = "progress-fill-green"
        if "blue" in color_class: bar_color = "progress-fill-blue"
        if "amber" in color_class: bar_color = "progress-fill-amber"
        if "purple" in color_class: bar_color = "progress-fill-green" # Purple usa verde por defecto

        # Generar filas de la tabla
        rows_html = ""
        for ind in commission['indicators']:
            # Lógica de color de porcentaje
            perc_color = "#16a34a" # verde
            if ind['perc'] < 100: perc_color = "#d97706" # ambar
            if ind['perc'] < 60: perc_color = "#dc2626" # rojo

            rows_html += f"""
            <tr>
                <td style="font-weight: 500;">{ind['item']}</td>
                <td style="text-align: center; color: #78716c;">{ind['meta']}</td>
                <td style="text-align: center; font-weight: 700;">{ind['ejec']}</td>
                <td style="width: 150px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <div class="progress-track" style="flex: 1;">
                            <div class="{bar_color}" style="width: {ind['perc']}%; background-color: {perc_color};"></div>
                        </div>
                        <span style="font-size: 0.75rem; font-weight: 700; color: {perc_color};">{ind['perc']}%</span>
                    </div>
                </td>
            </tr>
            """

        st.markdown(f"""
        <div class="card shadow-lg {border_class}" style="overflow: hidden;">
            <div class="{bg_class}" style="padding: 1rem; border-bottom: 1px solid #e7e5e4; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="background: white; padding: 8px; border-radius: 50%; font-size: 1.2rem; box-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                        {commission['icon']}
                    </div>
                    <div>
                        <h3 style="margin: 0; font-size: 1.25rem;" class="{color_class.replace('text-', 'text-color-')}">{commission['name']}</h3>
                        <div style="font-size: 0.8rem; color: #57534e;">👤 Líderes: {commission['lead']}</div>
                    </div>
                </div>
                <div style="background: white; padding: 5px 10px; border-radius: 6px; border: 1px solid #e7e5e4; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                    <span style="font-size: 0.65rem; font-weight: 700; color: #a8a29e; text-transform: uppercase;">Estado Fase</span>
                    <div style="color: #16a34a; font-weight: 700; font-size: 0.85rem; display: flex; align-items: center;">
                        ✅ Completado 100%
                    </div>
                </div>
            </div>
            <div style="overflow-x: auto;">
                <table class="custom-table">
                    <thead>
                        <tr>
                            <th>Indicador / Actividad</th>
                            <th style="text-align: center;">Meta</th>
                            <th style="text-align: center;">Ejecutado</th>
                            <th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows_html}
                    </tbody>
                </table>
            </div>
            <div style="background: #fafaf9; padding: 8px; text-align: center; font-size: 0.7rem; color: #a8a29e; border-top: 1px solid #e7e5e4;">
                ℹ️ Datos extraídos del informe final de {commission['name']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- RENDERIZADO DE TABS DE FASE ---
with tab2:
    render_phase_tab("antes")
with tab3:
    render_phase_tab("durante")
with tab4:
    render_phase_tab("despues")

# --- FOOTER: MATRIZ ALIADOS ---
st.markdown("""
<div class="card shadow-lg" style="background: #292524; color: white; border-top: 4px solid #d97706; margin-top: 2rem;">
    <div style="padding: 1.5rem; border-bottom: 1px solid #44403c;">
        <h3 style="margin: 0; display: flex; align-items: center; font-size: 1.2rem;">
            🤝 Resumen de Alianzas (Matriz)
        </h3>
    </div>
    <div style="padding: 1.5rem;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; text-align: center;">
            <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="font-size: 1.5rem; font-weight: 800; color: #fbbf24;">17</div>
                <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Aliados Totales</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="font-size: 1.5rem; font-weight: 800; color: #60a5fa;">5</div>
                <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Universidades</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="font-size: 1.5rem; font-weight: 800; color: #4ade80;">10</div>
                <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Empresas Privadas</div>
            </div>
            <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="font-size: 1.5rem; font-weight: 800; color: #c084fc;">2</div>
                <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Cooperativas</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
