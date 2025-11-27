import streamlit as st
import plotly.graph_objects as go

# --- 1. CONFIGURACIÓN DE PÁGINA (ESTO DEBE IR PRIMERO) ---
st.set_page_config(
    page_title="XI Congreso Prehospitalaria", 
    layout="wide", 
    page_icon="🚑",
    initial_sidebar_state="collapsed"
)

# --- 2. INYECCIÓN DE ESTILOS CSS (REPLICANDO REACT PIXEL-PERFECT) ---
st.markdown("""
<style>
    /* Importar fuente Inter para que se vea moderno */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Reset total de Streamlit */
    .stApp {
        background-color: #f5f5f4; /* bg-stone-100 */
        font-family: 'Inter', sans-serif;
        color: #1c1917;
    }
    
    /* Ocultar elementos molestos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 1rem !important; 
        padding-bottom: 2rem !important; 
        padding-left: 2rem !important; 
        padding-right: 2rem !important;
        max-width: 100% !important;
    }

    /* Clases de Tarjetas idénticas a React */
    .react-card {
        background-color: white;
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border: 1px solid #e7e5e4;
        margin-bottom: 1.5rem;
        overflow: hidden;
    }

    /* Header Gradiente */
    .header-gradient {
        background: linear-gradient(to right, #1c1917, #292524); /* stone-900 */
        border-bottom: 6px solid #d97706; /* amber-600 */
        border-radius: 1rem;
        position: relative;
        overflow: hidden;
        color: white;
        padding: 2.5rem;
        margin-bottom: 2rem;
    }

    /* Tablas personalizadas (Sin usar st.dataframe) */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.875rem;
    }
    .styled-table thead tr {
        background-color: #fafaf9;
        border-bottom: 1px solid #e7e5e4;
    }
    .styled-table th {
        padding: 1rem;
        text-align: left;
        font-weight: 700;
        color: #78716c;
        text-transform: uppercase;
        font-size: 0.75rem;
    }
    .styled-table td {
        padding: 1rem;
        border-bottom: 1px solid #f5f5f4;
        color: #44403c;
    }
    .styled-table tr:last-child td {
        border-bottom: none;
    }

    /* Barras de progreso HTML */
    .prog-track {
        background-color: #f3f4f6;
        border-radius: 9999px;
        height: 8px;
        width: 100%;
        overflow: hidden;
    }
    .prog-fill {
        height: 100%;
        border-radius: 9999px;
        transition: width 0.5s ease-in-out;
    }

    /* Utilidades de Texto */
    .text-xs { font-size: 0.75rem; line-height: 1rem; }
    .font-bold { font-weight: 700; }
    .uppercase { text-transform: uppercase; }
    .tracking-wider { letter-spacing: 0.05em; }
    
</style>
""", unsafe_allow_html=True)

# --- 3. DEFINICIÓN DE ICONOS SVG (PARA QUE SE VEA IGUAL A LUCIDE-REACT) ---
ICONS = {
    "briefcase": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>""",
    "layout": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>""",
    "megaphone": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>""",
    "check": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>""",
    "users": """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>""",
    "coffee": """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/><line x1="6" x2="6" y1="2" y2="4"/><line x1="10" x2="10" y1="2" y2="4"/><line x1="14" x2="14" y1="2" y2="4"/></svg>"""
}

# --- 4. DATOS ---
phases = {
    "antes": [
        {
            "name": "Gestión y Alianzas", "lead": "David Muñoz & Andrés Álvarez", "icon": "briefcase", "color": "text-blue-700", "bg_icon": "bg-blue-50", "border": "border-blue-500", "bg_header": "bg-blue-50",
            "indicators": [
                {"item": "Base de Datos Aliados", "meta": "1 BD", "ejec": "1 BD", "perc": 100},
                {"item": "Contactar Insumos", "meta": "11", "ejec": "10", "perc": 91},
                {"item": "Contactar IPS/Brigadas", "meta": "12", "ejec": "7", "perc": 58},
                {"item": "Gestión Universidades", "meta": "5", "ejec": "5", "perc": 100}
            ]
        },
        {
            "name": "Logística", "lead": "Santiago Rendón & Leymar Portilla", "icon": "layout", "color": "text-amber-700", "bg_icon": "bg-amber-50", "border": "border-amber-500", "bg_header": "bg-amber-50",
            "indicators": [
                {"item": "Contactar Ponentes", "meta": "20", "ejec": "20", "perc": 100},
                {"item": "Diseño Certificados", "meta": "1", "ejec": "1", "perc": 100},
                {"item": "Gestión Mobiliario", "meta": "100%", "ejec": "100%", "perc": 100},
                {"item": "Decoración Cafetera", "meta": "50", "ejec": "50", "perc": 100}
            ]
        },
        {
            "name": "Comunicaciones", "lead": "Joan Sebastian Arango", "icon": "megaphone", "color": "text-green-700", "bg_icon": "bg-green-50", "border": "border-green-500", "bg_header": "bg-green-50",
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
            "name": "Gestión y Alianzas", "lead": "Equipo Gestión", "icon": "briefcase", "color": "text-blue-700", "bg_icon": "bg-blue-50", "border": "border-blue-500", "bg_header": "bg-blue-50",
            "indicators": [
                {"item": "Supervisión Stands", "meta": "15", "ejec": "15", "perc": 100},
                {"item": "Entrega Refrigerios", "meta": "200", "ejec": "200", "perc": 100},
                {"item": "Registro Aliados", "meta": "17", "ejec": "15", "perc": 88}
            ]
        },
        {
            "name": "Logística", "lead": "Equipo Logística", "icon": "layout", "color": "text-amber-700", "bg_icon": "bg-amber-50", "border": "border-amber-500", "bg_header": "bg-amber-50",
            "indicators": [
                {"item": "Soporte Auditorio", "meta": "100%", "ejec": "100%", "perc": 100},
                {"item": "Control Asistencia", "meta": "200", "ejec": "200", "perc": 100},
                {"item": "Talleres Edif. 14", "meta": "6", "ejec": "6", "perc": 100}
            ]
        },
        {
            "name": "Comunicaciones", "lead": "Equipo Comunicaciones", "icon": "megaphone", "color": "text-green-700", "bg_icon": "bg-green-50", "border": "border-green-500", "bg_header": "bg-green-50",
            "indicators": [
                {"item": "Cobertura Ponencias", "meta": "12", "ejec": "12", "perc": 100},
                {"item": "Entrevistas", "meta": "10", "ejec": "8", "perc": 80},
                {"item": "Stories en Vivo", "meta": "50", "ejec": "50+", "perc": 100}
            ]
        }
    ],
    "despues": [
        {
            "name": "Cierre General", "lead": "Todas las Comisiones", "icon": "check", "color": "text-purple-700", "bg_icon": "bg-purple-50", "border": "border-purple-500", "bg_header": "bg-purple-50",
            "indicators": [
                {"item": "Cartas Agradecimiento", "meta": "17", "ejec": "17", "perc": 100},
                {"item": "Certificados Enviados", "meta": "200", "ejec": "200", "perc": 100},
                {"item": "Memorias Digitales", "meta": "1 Pack", "ejec": "1 Pack", "perc": 100},
                {"item": "Informe Final", "meta": "1", "ejec": "1", "perc": 100}
            ]
        }
    ]
}

# --- 5. RENDERIZADO DEL HEADER ---
st.markdown(f"""
<div class="header-gradient">
    <div style="position: relative; z-index: 10; display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;">
        <div style="background: rgba(255,255,255,0.1); width: 120px; height: 120px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid rgba(245, 158, 11, 0.5); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);">
            <div style="font-size: 3.5rem;">🚑</div>
        </div>
        
        <div style="flex: 1;">
            <div style="display: inline-flex; align-items: center; background: rgba(217, 119, 6, 0.2); border: 1px solid #d97706; color: #fbbf24; padding: 4px 12px; border-radius: 99px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 0.75rem;">
                <span style="margin-right: 6px;">{ICONS['coffee']}</span> Edición Especial: Identidad Cafetera
            </div>
            <h1 style="margin: 0; font-size: 2.5rem; font-weight: 800; line-height: 1.1; margin-bottom: 0.5rem;">
                XI Congreso Nacional <br>
                <span style="color: #f59e0b;">Medicina Prehospitalaria</span>
            </h1>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                <span style="background: rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 8px; font-size: 0.875rem; border: 1px solid rgba(255,255,255,0.1);">📅 23-25 Octubre 2025</span>
                <span style="background: rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 8px; font-size: 0.875rem; border: 1px solid rgba(255,255,255,0.1);">📍 Aud. Jorge Roa & Edif. 14</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 6. NAVEGACIÓN (TABS) ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Visión General", "1️⃣ Pre-Evento", "2️⃣ Durante", "3️⃣ Post-Evento"])

# --- TAB 1: VISIÓN GENERAL (GRÁFICOS) ---
with tab1:
    # FILA DE GRÁFICOS
    c1, c2, c3 = st.columns(3)
    
    # Gráfico 1: Aliados
    with c1:
        fig1 = go.Figure(data=[go.Pie(labels=["Insumos", "Unis", "Café"], values=[10, 4, 3], hole=.7, marker=dict(colors=['#1e40af', '#3b82f6', '#93c5fd']))])
        fig1.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=180, annotations=[dict(text="Gestión", x=0.5, y=0.5, font_size=12, showarrow=False)])
        
        st.markdown("""
        <div class="react-card" style="border-top: 4px solid #2563eb; padding: 1.5rem; text-align: center;">
            <h3 style="color: #1e3a8a; margin: 0; font-size: 1.1rem;">Aliados Estratégicos</h3>
            <p style="color: #6b7280; font-size: 0.8rem; margin-bottom: 1rem;">Total: 17 Entidades</p>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Gráfico 2: Asistencia
    with c2:
        fig2 = go.Figure(data=[go.Pie(labels=["UTP", "Externos", "Staff"], values=[140, 40, 20], hole=.7, marker=dict(colors=['#b45309', '#f59e0b', '#fcd34d']))])
        fig2.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=180, annotations=[dict(text="Aforo", x=0.5, y=0.5, font_size=12, showarrow=False)])
        
        st.markdown("""
        <div class="react-card" style="border-top: 4px solid #d97706; padding: 1.5rem; text-align: center;">
            <h3 style="color: #78350f; margin: 0; font-size: 1.1rem;">Asistencia</h3>
            <p style="color: #6b7280; font-size: 0.8rem; margin-bottom: 1rem;">Total: ~200 Pax</p>
        """, unsafe_allow_html=True)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Gráfico 3: Barras
    with c3:
        st.markdown("""
        <div class="react-card" style="border-top: 4px solid #16a34a; padding: 1.5rem;">
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <h3 style="color: #14532d; margin: 0; font-size: 1.1rem;">Cumplimiento Global</h3>
                <p style="color: #6b7280; font-size: 0.8rem;">Por áreas</p>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: 600; color: #374151; margin-bottom: 4px;"><span>Gestión</span><span>91%</span></div>
                <div class="prog-track"><div class="prog-fill" style="width: 91%; background-color: #16a34a;"></div></div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: 600; color: #374151; margin-bottom: 4px;"><span>Logística</span><span>98%</span></div>
                <div class="prog-track"><div class="prog-fill" style="width: 98%; background-color: #16a34a;"></div></div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; font-weight: 600; color: #374151; margin-bottom: 4px;"><span>Comunicaciones</span><span>100%</span></div>
                <div class="prog-track"><div class="prog-fill" style="width: 100%; background-color: #16a34a;"></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # DOFA
    d1, d2 = st.columns(2)
    with d1:
        st.markdown("""
        <div class="react-card" style="padding: 1.5rem; background: linear-gradient(to bottom right, #ffffff, #f0fdf4); border: 1px solid #bbf7d0;">
            <h4 style="color: #166534; margin: 0 0 12px 0; font-weight: 700; display: flex; align-items: center;">🏆 Fortalezas</h4>
            <ul style="margin: 0; padding-left: 1.2rem; color: #14532d; font-size: 0.9rem; line-height: 1.6;">
                <li>Identidad Cafetera clara y transversal.</li>
                <li>Capacidad de gestión (17 aliados sin presupuesto).</li>
                <li>Trabajo articulado entre comisiones.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with d2:
        st.markdown("""
        <div class="react-card" style="padding: 1.5rem; background: linear-gradient(to bottom right, #ffffff, #fef2f2); border: 1px solid #fecaca;">
            <h4 style="color: #991b1b; margin: 0 0 12px 0; font-weight: 700; display: flex; align-items: center;">⚠️ Oportunidades</h4>
            <ul style="margin: 0; padding-left: 1.2rem; color: #7f1d1d; font-size: 0.9rem; line-height: 1.6;">
                <li>Mayor anticipación en piezas gráficas.</li>
                <li>Recursos técnicos propios limitados.</li>
                <li>Dependencia alta de gestión externa.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- FUNCIÓN PARA RENDERIZAR TABLAS DETALLADAS ---
def render_detailed_tab(phase_name):
    for commission in phases[phase_name]:
        # Configurar colores para HTML
        text_color = "#1d4ed8" if "blue" in commission['color'] else "#b45309" if "amber" in commission['color'] else "#15803d" if "green" in commission['color'] else "#7e22ce"
        bg_bar = "#2563eb" if "blue" in commission['color'] else "#d97706" if "amber" in commission['color'] else "#16a34a" if "green" in commission['color'] else "#a855f7"
        border_class = f"border-l-8 {commission['border'].replace('border-l-', 'border-l-color-')}" # mapeo simple
        
        # HTML de filas
        rows_html = ""
        for ind in commission['indicators']:
            perc_color = "#16a34a" # Green default
            if ind['perc'] < 100: perc_color = "#d97706"
            if ind['perc'] < 60: perc_color = "#dc2626"
            
            rows_html += f"""
            <tr>
                <td style="font-weight: 500;">{ind['item']}</td>
                <td style="text-align: center; color: #78716c;">{ind['meta']}</td>
                <td style="text-align: center; font-weight: 700;">{ind['ejec']}</td>
                <td style="width: 140px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <div class="prog-track">
                            <div class="prog-fill" style="width: {ind['perc']}%; background-color: {perc_color};"></div>
                        </div>
                        <span style="font-size: 0.75rem; font-weight: 700; color: {perc_color};">{ind['perc']}%</span>
                    </div>
                </td>
            </tr>
            """
            
        st.markdown(f"""
        <div class="react-card" style="border-left: 6px solid {bg_bar};">
            <div class="{commission['bg_header']}" style="padding: 1rem 1.5rem; border-bottom: 1px solid #e7e5e4; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="color: {text_color}; background: white; padding: 8px; border-radius: 50%; box-shadow: 0 1px 2px rgba(0,0,0,0.1);">
                        {ICONS[commission['icon']]}
                    </div>
                    <div>
                        <h3 style="margin: 0; color: {text_color}; font-size: 1.25rem;">{commission['name']}</h3>
                        <div style="font-size: 0.8rem; color: #57534e; display: flex; align-items: center; gap: 4px;">
                             {ICONS['users']} Líderes: {commission['lead']}
                        </div>
                    </div>
                </div>
                <div style="background: white; padding: 6px 12px; border-radius: 8px; border: 1px solid #e7e5e4; text-align: right;">
                    <div style="text-transform: uppercase; font-size: 0.65rem; font-weight: 700; color: #a8a29e;">Estado</div>
                    <div style="color: #16a34a; font-weight: 700; font-size: 0.85rem;">Completo 100%</div>
                </div>
            </div>
            <div style="overflow-x: auto;">
                <table class="styled-table">
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
            <div style="background: #fafaf9; padding: 8px 1.5rem; border-top: 1px solid #e7e5e4; font-size: 0.75rem; color: #a8a29e; font-style: italic;">
                Datos extraídos del informe final de {commission['name']}
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    render_detailed_tab("antes")
with tab3:
    render_detailed_tab("durante")
with tab4:
    render_detailed_tab("despues")

# --- FOOTER FINAL ---
st.markdown("""
<div class="react-card" style="background-color: #1c1917; color: white; border-top: 4px solid #d97706; margin-top: 3rem;">
    <div style="padding: 1.5rem; display: flex; align-items: center; gap: 1rem; border-bottom: 1px solid #44403c;">
        <div style="color: #f59e0b;">""" + ICONS['briefcase'] + """</div>
        <h3 style="margin: 0; font-size: 1.2rem;">Resumen de Alianzas (Matriz)</h3>
    </div>
    <div style="padding: 1.5rem; display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; text-align: center;">
        <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #fbbf24;">17</div>
            <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Total Aliados</div>
        </div>
        <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #60a5fa;">5</div>
            <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Universidades</div>
        </div>
        <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #4ade80;">10</div>
            <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Privados</div>
        </div>
        <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #c084fc;">2</div>
            <div style="font-size: 0.7rem; text-transform: uppercase; opacity: 0.7;">Cooperativas</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
