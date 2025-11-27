import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="XI Congreso Prehospitalaria", layout="wide", page_icon="☕")

# --- 2. ESTILOS CSS (TRADUCCIÓN DE TAILWIND A CSS PURO) ---
# Esto hace que se vea IDÉNTICO a tu diseño original
st.markdown("""
<style>
    /* Reset básico y fuentes */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    .stApp {
        background-color: #f5f5f4; /* bg-stone-100 */
        font-family: 'Inter', sans-serif;
    }

    /* Estilos de Tarjetas (Cards) */
    .card {
        background-color: white;
        border-radius: 0.75rem; /* rounded-xl */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #e7e5e4;
        margin-bottom: 1.5rem;
        overflow: hidden;
    }

    /* Bordes superiores de colores para las comisiones */
    .border-top-blue { border-top: 4px solid #2563eb; }
    .border-top-amber { border-top: 4px solid #d97706; }
    .border-top-green { border-top: 4px solid #16a34a; }

    /* Estilos de Texto */
    .text-stone-800 { color: #292524; }
    .text-stone-500 { color: #78716c; }
    .font-bold { font-weight: 700; }
    .text-xs { font-size: 0.75rem; }
    .uppercase { text-transform: uppercase; }

    /* Header */
    .header-container {
        background: linear-gradient(to right, #1c1917, #0c0a09);
        border-bottom: 8px solid #d97706; /* border-amber-600 */
        border-radius: 1rem;
        padding: 2.5rem;
        color: white;
        margin-bottom: 2rem;
        position: relative;
    }

    /* Tablas */
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
    }
    .custom-table td {
        padding: 1rem 1.5rem;
        border-bottom: 1px solid #f5f5f4;
        color: #1c1917;
    }

    /* Badges (Etiquetas de estado) */
    .badge-green { background-color: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 9999px; font-weight: bold; font-size: 0.75rem; }
    .badge-amber { background-color: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 9999px; font-weight: bold; font-size: 0.75rem; }
</style>
""", unsafe_allow_html=True)

# --- 3. DATOS (LOS MISMOS DEL ORIGINAL) ---
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

# --- 4. RENDERIZADO DEL HEADER ---
st.markdown("""
<div class="header-container">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span style="background: rgba(217,119,6,0.2); color: #fbbf24; padding: 4px 12px; border-radius: 9999px; font-size: 0.75rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">
                ☕ Edición Especial
            </span>
            <h1 style="font-size: 2.5rem; font-weight: 800; margin-top: 1rem; margin-bottom: 0.5rem; line-height: 1.1;">
                XI Congreso Nacional<br>
                <span style="color: #f59e0b;">Medicina Prehospitalaria</span>
            </h1>
            <p style="color: #d6d3d1; font-style: italic; font-size: 1.125rem;">"Identidad Cafetera en la Emergencia"</p>
            <div style="margin-top: 1.5rem; display: flex; gap: 1rem;">
                <span style="background: rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 0.5rem; font-size: 0.875rem;">📅 23-25 Octubre 2025</span>
                <span style="background: rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 0.5rem; font-size: 0.875rem;">📍 Aud. Jorge Roa & Edif. 14</span>
            </div>
        </div>
        <div style="text-align: center; background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 1rem; backdrop-filter: blur(4px);">
             <div style="font-size: 3rem; margin-bottom: 0.5rem;">🚑</div>
             <div style="font-weight: bold; font-size: 1.5rem;">200+</div>
             <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.8;">Asistentes</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. TABS DE NAVEGACIÓN ---
tab1, tab2, tab3 = st.tabs(["📈 Resumen & DOFA", "⏱️ Cronograma (Fases)", "🤝 Matriz Aliados"])

# --- TAB 1: RESUMEN Y DOFA ---
with tab1:
    # Métricas
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="card" style="padding: 1.5rem; border-left: 4px solid #22c55e;">
            <div class="text-xs font-bold text-stone-500 uppercase">Asistencia</div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #166534;">200+</div>
            <div class="text-xs text-stone-500">100% de la Meta</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card" style="padding: 1.5rem; border-left: 4px solid #d97706;">
            <div class="text-xs font-bold text-stone-500 uppercase">Cronograma</div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #92400e;">98%</div>
            <div class="text-xs text-stone-500">Ejecución a tiempo</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="card" style="padding: 1.5rem; border-left: 4px solid #2563eb;">
            <div class="text-xs font-bold text-stone-500 uppercase">Aliados</div>
            <div style="font-size: 1.5rem; font-weight: 800; color: #1e40af;">17</div>
            <div class="text-xs text-stone-500">Empresas Vinculadas</div>
        </div>""", unsafe_allow_html=True)

    # DOFA
    st.markdown("### 🦁 Análisis de Impacto (DOFA)")
    d1, d2 = st.columns(2)
    with d1:
        st.markdown("""
        <div class="card" style="padding: 1.5rem; background-color: #f0fdf4; border: 1px solid #bbf7d0;">
            <h4 style="color: #166534; margin: 0 0 10px 0;">✅ Fortalezas</h4>
            <ul style="color: #15803d; font-size: 0.9rem; margin: 0; padding-left: 1.2rem;">
                <li>Trabajo en equipo y liderazgo</li>
                <li>Identidad Cafetera clara</li>
                <li>17 Aliados confirmados</li>
            </ul>
        </div>
        <div class="card" style="padding: 1.5rem; background-color: #eff6ff; border: 1px solid #bfdbfe;">
            <h4 style="color: #1e40af; margin: 0 0 10px 0;">🔵 Oportunidades</h4>
            <ul style="color: #1d4ed8; font-size: 0.9rem; margin: 0; padding-left: 1.2rem;">
                <li>Posicionar a Pereira como eje académico</li>
                <li>Alianzas con nuevos emprendimientos</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with d2:
        st.markdown("""
        <div class="card" style="padding: 1.5rem; background-color: #fef2f2; border: 1px solid #fecaca;">
            <h4 style="color: #991b1b; margin: 0 0 10px 0;">⚠️ Debilidades</h4>
            <ul style="color: #b91c1c; font-size: 0.9rem; margin: 0; padding-left: 1.2rem;">
                <li>Recursos técnicos limitados</li>
                <li>Tiempos ajustados en gráficas</li>
            </ul>
        </div>
        <div class="card" style="padding: 1.5rem; background-color: #fffbeb; border: 1px solid #fde68a;">
            <h4 style="color: #92400e; margin: 0 0 10px 0;">🛑 Amenazas</h4>
            <ul style="color: #b45309; font-size: 0.9rem; margin: 0; padding-left: 1.2rem;">
                <li>Imprevistos logísticos</li>
                <li>Ausencia de ponentes (riesgo latente)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: CRONOGRAMA ---
with tab2:
    selected_phase = st.selectbox("Seleccionar Fase:", ["antes", "durante", "despues"], format_func=lambda x: x.upper())
    
    # Grid de 3 columnas para las comisiones
    cols = st.columns(3)
    
    for idx, commission in enumerate(phases[selected_phase]):
        with cols[idx]:
            # HTML Dinámico para cada tarjeta
            html_tasks = ""
            for t in commission['tasks']:
                color_bar = "#22c55e" if t['progress'] == 100 else "#fbbf24"
                html_tasks += f"""
                <div style="margin-bottom: 12px; padding-left: 12px; border-left: 2px solid #e7e5e4; position: relative;">
                    <div style="position: absolute; left: -5px; top: 4px; width: 8px; height: 8px; border-radius: 50%; background-color: {color_bar};"></div>
                    <div style="display: flex; justify-content: space-between; font-size: 0.875rem; font-weight: 600; color: #44403c;">
                        <span>{t['activity']}</span>
                        <span style="color: {color_bar};">{t['progress']}%</span>
                    </div>
                    <div style="font-size: 0.75rem; color: #78716c; margin-top: 2px;">{t['details']}</div>
                </div>
                """
            
            # Renderizar la tarjeta completa
            st.markdown(f"""
            <div class="card border-top-{commission['color']}">
                <div style="padding: 1.5rem; background-color: #fafaf9; border-bottom: 1px solid #e7e5e4;">
                    <div style="display: flex; justify-content: space-between;">
                        <div style="font-size: 1.5rem;">{commission['icon']}</div>
                        <span style="font-size: 0.65rem; font-weight: bold; text-transform: uppercase; background: white; padding: 4px 8px; border-radius: 999px; border: 1px solid #e7e5e4; color: #78716c;">Comisión</span>
                    </div>
                    <h3 style="margin-top: 0.5rem; font-size: 1.125rem; color: #1c1917; margin-bottom: 0;">{commission['name']}</h3>
                    <div style="font-size: 0.75rem; color: #78716c; display: flex; align-items: center; margin-top: 4px;">
                        👤 {commission['lead']}
                    </div>
                </div>
                <div style="padding: 1.5rem;">
                    {html_tasks}
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 3: ALIADOS ---
with tab3:
    st.markdown("""
    <div class="card">
        <div style="padding: 1.5rem; background: linear-gradient(to right, #eff6ff, white); border-bottom: 1px solid #e7e5e4;">
            <h3 style="color: #1e40af; margin: 0; display: flex; align-items: center;">🤝 Matriz de Gestión de Alianzas</h3>
            <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.875rem;">Resumen de los 17 aliados estratégicos gestionados.</p>
        </div>
        <table class="custom-table">
            <thead>
                <tr>
                    <th>Tipo de Aliado</th>
                    <th>Gestión</th>
                    <th style="text-align: center;">Estado</th>
                    <th style="text-align: right;">Aporte Principal</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><span style="font-weight: 600;">Universidades (Pereira)</span></td>
                    <td>Cartas y visitas</td>
                    <td style="text-align: center;"><span class="badge-green">Confirmado</span></td>
                    <td style="text-align: right;">Difusión y Aval Académico</td>
                </tr>
                <tr>
                    <td><span style="font-weight: 600;">Empresas de Insumos</span></td>
                    <td>Llamadas y Propuestas</td>
                    <td style="text-align: center;"><span class="badge-green">Confirmado</span></td>
                    <td style="text-align: right;">Stands y Muestras</td>
                </tr>
                <tr>
                    <td><span style="font-weight: 600;">Cooperativas de Café</span></td>
                    <td>Gestión en especie</td>
                    <td style="text-align: center;"><span class="badge-green">Confirmado</span></td>
                    <td style="text-align: right;">Decoración y Refrigerios</td>
                </tr>
                <tr>
                    <td><span style="font-weight: 600;">IPS y Brigadas</span></td>
                    <td>Convenios</td>
                    <td style="text-align: center;"><span class="badge-amber">Parcial</span></td>
                    <td style="text-align: right;">Apoyo en Simulacros</td>
                </tr>
                <tr style="background-color: #fafaf9; font-weight: bold;">
                    <td colspan="3" style="text-align: right; padding-right: 2rem;">TOTAL ALIADOS:</td>
                    <td style="text-align: right; color: #1d4ed8;">17 ENTIDADES</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
