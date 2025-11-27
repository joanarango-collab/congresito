import React, { useState } from 'react';
import { 
  Calendar, 
  Users, 
  Megaphone, 
  Briefcase, 
  CheckCircle, 
  Clock, 
  Award, 
  Layout, 
  TrendingUp,
  FileText,
  DollarSign,
  Coffee,
  PieChart,
  BarChart as BarChartIcon,
  AlertTriangle,
  Target,
  Handshake,
  MapPin
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Progress } from "@/components/ui/progress";

// --- Tipos de Datos ---
type Task = {
  id: string;
  activity: string;
  status: 'Completado' | 'En Progreso' | 'Pendiente';
  progress: number;
  details: string;
};

type CommissionData = {
  name: string;
  lead: string;
  icon: React.ElementType;
  color: string;
  borderColor: string;
  bgLight: string;
  tasks: Task[];
  stats: { label: string; value: string }[];
};

type PhaseData = {
  [key: string]: CommissionData[];
};

const DashboardCongreso = () => {
  const [activeTab, setActiveTab] = useState('resumen');

  // --- Datos del Evento (Extraídos de Informes y Matriz) ---
  
  // 2. Datos de Fases (Antes, Durante, Después)
  const phases: PhaseData = {
    antes: [
      {
        name: "Gestión y Alianzas",
        lead: "David Muñoz & Andrés Álvarez",
        icon: Briefcase,
        color: "text-blue-800",
        borderColor: "border-blue-600",
        bgLight: "bg-blue-50",
        stats: [
          { label: "Base de Datos", value: "56 Contactos" },
          { label: "Aliados Confirmados", value: "17 Empresas" },
          { label: "Meta Patrocinios", value: "90% Logrado" }
        ],
        tasks: [
          { id: "g1", activity: "Base de Datos Aliados", status: "Completado", progress: 100, details: "Mapeo de 56 entidades (IPS, UTP, Privados)." },
          { id: "g2", activity: "Solicitud de Insumos", status: "Completado", progress: 95, details: "Gestión de café, refrigerios y decoración." },
          { id: "g3", activity: "Invitaciones Oficiales", status: "Completado", progress: 100, details: "Cartas a universidades y programas de salud." }
        ]
      },
      {
        name: "Logística y Ambientación",
        lead: "Santiago Rendón & Leymar Portilla",
        icon: Layout,
        color: "text-amber-800",
        borderColor: "border-amber-600",
        bgLight: "bg-amber-50",
        stats: [
          { label: "Decoración", value: "Identidad Cafetera" },
          { label: "Certificados", value: "Diseño Listo" },
          { label: "Insumos", value: "100% Gestionados" }
        ],
        tasks: [
          { id: "l1", activity: "Escenografía Cafetera", status: "Completado", progress: 100, details: "Creación manual de elementos en cartón y pintura." },
          { id: "l2", activity: "Requerimientos Técnicos", status: "Completado", progress: 100, details: "Recolección de presentaciones de ponentes." },
          { id: "l3", activity: "Mobiliario Stands", status: "Completado", progress: 100, details: "Mesas, sillas y manteles asegurados." }
        ]
      },
      {
        name: "Comunicaciones",
        lead: "Joan Sebastian Arango",
        icon: Megaphone,
        color: "text-green-800",
        borderColor: "border-green-600",
        bgLight: "bg-green-50",
        stats: [
          { label: "Línea Gráfica", value: "Definida" },
          { label: "Campaña", value: "Lanzada" },
          { label: "Redes", value: "Activas" }
        ],
        tasks: [
          { id: "c1", activity: "Manual de Marca", status: "Completado", progress: 100, details: "Definición de paleta visual cafetera." },
          { id: "c2", activity: "Campaña Expectativa", status: "Completado", progress: 100, details: "Teaser, flyers y perfiles de ponentes." },
          { id: "c3", activity: "Diseño Escarapelas", status: "Completado", progress: 100, details: "Identificación para staff y asistentes." }
        ]
      }
    ],
    durante: [
      {
        name: "Gestión y Alianzas",
        lead: "Equipo Gestión",
        icon: Briefcase,
        color: "text-blue-800",
        borderColor: "border-blue-600",
        bgLight: "bg-blue-50",
        stats: [
          { label: "Stands Activos", value: "17 Stands" },
          { label: "Refrigerios", value: "Distribuidos" },
          { label: "Satisfacción", value: "Alta" }
        ],
        tasks: [
          { id: "g4", activity: "Supervisión de Stands", status: "Completado", progress: 100, details: "Verificación de montaje de aliados." },
          { id: "g5", activity: "Logística Alimentación", status: "Completado", progress: 100, details: "Entrega de refrigerios a staff y ponentes." },
          { id: "g6", activity: "Registro de Marcas", status: "En Progreso", progress: 90, details: "Evidencia visual de patrocinadores." }
        ]
      },
      {
        name: "Logística Operativa",
        lead: "Equipo Logística",
        icon: Layout,
        color: "text-amber-800",
        borderColor: "border-amber-600",
        bgLight: "bg-amber-50",
        stats: [
          { label: "Sedes", value: "Auditorio + Edif. 14" },
          { label: "Incidencias", value: "Mínimas" },
          { label: "Tiempos", value: "Cumplidos" }
        ],
        tasks: [
          { id: "l4", activity: "Soporte Audiovisual", status: "Completado", progress: 100, details: "Pruebas de sonido y proyección previas." },
          { id: "l5", activity: "Protocolo Ponentes", status: "Completado", progress: 100, details: "Acompañamiento en tarima y tiempos." },
          { id: "l6", activity: "Flujo de Asistentes", status: "Completado", progress: 100, details: "Control de acceso en Auditorio y Edificio 14 (Talleres)." }
        ]
      },
      {
        name: "Comunicaciones",
        lead: "Equipo Comunicaciones",
        icon: Megaphone,
        color: "text-green-800",
        borderColor: "border-green-600",
        bgLight: "bg-green-50",
        stats: [
          { label: "Cobertura", value: "En Vivo" },
          { label: "Entrevistas", value: "Realizadas" },
          { label: "Stories", value: "+50 Publicadas" }
        ],
        tasks: [
          { id: "c4", activity: "Registro Fotográfico", status: "Completado", progress: 100, details: "Cobertura completa en ambas sedes (Ponencias y Talleres)." },
          { id: "c5", activity: "Gestión Redes", status: "Completado", progress: 100, details: "Minuto a minuto en Instagram/FB." },
          { id: "c6", activity: "Entrevistas", status: "Completado", progress: 100, details: "Testimonios de asistentes y expertos." }
        ]
      }
    ],
    despues: [
      {
        name: "Gestión y Alianzas",
        lead: "Equipo Gestión",
        icon: Briefcase,
        color: "text-blue-800",
        borderColor: "border-blue-600",
        bgLight: "bg-blue-50",
        stats: [
          { label: "Agradecimientos", value: "100% Enviados" },
          { label: "Informe", value: "Entregado" },
          { label: "Relaciones", value: "Consolidadas" }
        ],
        tasks: [
          { id: "g7", activity: "Cartas Agradecimiento", status: "Completado", progress: 100, details: "Envío a los 17 aliados estratégicos." },
          { id: "g8", activity: "Informe Gestión", status: "Completado", progress: 100, details: "Balance de impacto y aportes." },
          { id: "g9", activity: "Devolución Bienes", status: "Completado", progress: 100, details: "Retorno de mobiliario prestado." }
        ]
      },
      {
        name: "Logística de Cierre",
        lead: "Equipo Logística",
        icon: Layout,
        color: "text-amber-800",
        borderColor: "border-amber-600",
        bgLight: "bg-amber-50",
        stats: [
          { label: "Certificados", value: "Distribuidos" },
          { label: "Inventario", value: "Paz y Salvo" },
          { label: "Desmontaje", value: "Total" }
        ],
        tasks: [
          { id: "l7", activity: "Certificación Digital", status: "Completado", progress: 100, details: "Envío masivo a asistentes." },
          { id: "l8", activity: "Desmontaje", status: "Completado", progress: 100, details: "Retiro de decoración cafetera y limpieza." },
          { id: "l9", activity: "Informe Final", status: "Completado", progress: 100, details: "Evaluación logística y operativa." }
        ]
      },
      {
        name: "Comunicaciones",
        lead: "Equipo Comunicaciones",
        icon: Megaphone,
        color: "text-green-800",
        borderColor: "border-green-600",
        bgLight: "bg-green-50",
        stats: [
          { label: "Memorias", value: "Publicadas" },
          { label: "Aftermovie", value: "Editado" },
          { label: "Álbum", value: "Online" }
        ],
        tasks: [
          { id: "c7", activity: "Post-Producción", status: "Completado", progress: 100, details: "Edición de video resumen y fotos." },
          { id: "c8", activity: "Memorias Académicas", status: "Completado", progress: 100, details: "Compilación PDF para asistentes." },
          { id: "c9", activity: "Informe Métricas", status: "Completado", progress: 100, details: "Análisis de alcance digital." }
        ]
      }
    ]
  };

  // --- Datos DOFA (Extraídos de Informes) ---
  const swotAnalysis = {
    fortalezas: ["Trabajo en equipo y liderazgo", "Identidad Cafetera clara", "Capacidad de adaptación", "17 Aliados confirmados"],
    oportunidades: ["Posicionar a Pereira como eje académico", "Alianzas con nuevos emprendimientos", "Expandir cobertura digital"],
    debilidades: ["Recursos técnicos limitados", "Tiempos ajustados en piezas gráficas", "Presupuesto dependiente de gestión"],
    amenazas: ["Imprevistos logísticos de última hora", "Ausencia de ponentes (riesgo latente)", "Fallas técnicas en auditorio"]
  };

  return (
    <div className="min-h-screen bg-stone-100 p-4 md:p-8 font-sans text-stone-800">
      
      {/* --- HEADER CON FONDO Y LOGOTIPO --- */}
      <header className="relative bg-stone-900 rounded-2xl shadow-2xl overflow-hidden mb-8 border-b-8 border-amber-600">
        {/* Imagen de Fondo con Overlay */}
        <div className="absolute inset-0 z-0">
          <img 
            src="image_2141b3.jpg" 
            alt="Fondo Congreso" 
            className="w-full h-full object-cover opacity-30 mix-blend-luminosity"
            onError={(e) => {
               (e.target as HTMLImageElement).style.display = 'none';
            }}
          />
          <div className="absolute inset-0 bg-gradient-to-r from-stone-900/95 via-stone-900/80 to-transparent"></div>
        </div>

        <div className="relative z-10 p-6 md:p-10 flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="flex flex-col md:flex-row items-center md:items-start text-center md:text-left gap-6">
             {/* LOGOTIPO ACTUALIZADO - APARTADO LOGO XI CONGRESO */}
            <div className="w-40 h-40 md:w-48 md:h-48 bg-white/10 backdrop-blur-sm rounded-full shadow-2xl border-2 border-amber-500/30 flex items-center justify-center overflow-hidden shrink-0 transition-transform hover:scale-105 duration-300">
               <img 
                 src="logotipo congreso medicina prehospitalaria (2).png" 
                 alt="Logo XI Congreso Medicina Prehospitalaria" 
                 className="w-full h-full object-contain p-2"
                 onError={(e) => {
                   (e.target as HTMLImageElement).src = 'https://placehold.co/150x150/FFF/B45309?text=Logo+XI+Congreso';
                 }}
               />
            </div>
            
            <div className="text-white">
              <div className="inline-flex items-center px-3 py-1 rounded-full bg-amber-600/20 border border-amber-500/50 text-amber-400 text-xs font-bold mb-3 tracking-wide uppercase">
                <Coffee className="w-3 h-3 mr-1" /> Edición Especial
              </div>
              <h1 className="text-3xl md:text-5xl font-extrabold leading-tight mb-2 drop-shadow-md">
                XI Congreso Nacional <br/>
                <span className="text-amber-500">Medicina Prehospitalaria</span>
              </h1>
              <p className="text-lg text-stone-300 font-medium italic mb-4">"Identidad Cafetera en la Emergencia"</p>
              
              <div className="flex flex-wrap gap-4 justify-center md:justify-start">
                <span className="flex items-center text-sm font-semibold bg-white/10 px-4 py-2 rounded-lg text-stone-200 border border-white/10 backdrop-blur-sm">
                  <Calendar className="w-4 h-4 mr-2 text-amber-400" /> 23-25 Octubre 2025
                </span>
                <span className="flex items-center text-sm font-semibold bg-white/10 px-4 py-2 rounded-lg text-stone-200 border border-white/10 backdrop-blur-sm">
                  <MapPin className="w-4 h-4 mr-2 text-amber-400" /> Aud. Jorge Roa & Edificio 14 (Talleres)
                </span>
              </div>
            </div>
          </div>

          {/* Quick Stats Banner */}
          <div className="grid grid-cols-2 gap-4 w-full md:w-auto">
             <div className="bg-amber-600/90 backdrop-blur-md text-white p-4 rounded-xl text-center shadow-lg border border-amber-500/50">
                <Users className="w-7 h-7 mx-auto mb-1 opacity-90" />
                <span className="block text-3xl font-bold">200+</span>
                <span className="text-xs opacity-80 uppercase tracking-wider">Asistentes</span>
             </div>
             <div className="bg-stone-800/90 backdrop-blur-md text-white p-4 rounded-xl text-center shadow-lg border border-stone-700">
                <Handshake className="w-7 h-7 mx-auto mb-1 opacity-90 text-green-400" />
                <span className="block text-3xl font-bold">17</span>
                <span className="text-xs opacity-80 uppercase tracking-wider">Aliados</span>
             </div>
          </div>
        </div>
      </header>

      {/* --- NAVEGACIÓN PRINCIPAL --- */}
      <Tabs defaultValue="resumen" className="space-y-6" onValueChange={setActiveTab}>
        <div className="sticky top-2 z-30 bg-white/90 backdrop-blur-md p-2 rounded-xl shadow-sm border border-stone-200">
          <TabsList className="grid grid-cols-3 w-full h-auto bg-stone-100/50 p-1">
            <TabsTrigger value="resumen" className="py-2.5 data-[state=active]:bg-white data-[state=active]:shadow-sm data-[state=active]:text-amber-700">
              <TrendingUp className="w-4 h-4 mr-2" /> Resumen & DOFA
            </TabsTrigger>
            <TabsTrigger value="fases" className="py-2.5 data-[state=active]:bg-white data-[state=active]:shadow-sm data-[state=active]:text-amber-700">
              <Clock className="w-4 h-4 mr-2" /> Cronograma (3 Fases)
            </TabsTrigger>
            <TabsTrigger value="aliados" className="py-2.5 data-[state=active]:bg-white data-[state=active]:shadow-sm data-[state=active]:text-amber-700">
              <Handshake className="w-4 h-4 mr-2" /> Matriz Aliados
            </TabsTrigger>
          </TabsList>
        </div>

        {/* --- CONTENIDO: RESUMEN Y DOFA --- */}
        <TabsContent value="resumen" className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card className="md:col-span-2 border-t-4 border-amber-500 shadow-md">
              <CardHeader>
                <CardTitle className="flex items-center text-amber-900">
                  <FileText className="w-5 h-5 mr-2" /> Análisis de Impacto (DOFA)
                </CardTitle>
                <CardDescription>Evaluación estratégica basada en informes finales.</CardDescription>
              </CardHeader>
              <CardContent className="grid grid-cols-1 md:grid-cols-2 gap-4">
                 {/* Fortalezas */}
                 <div className="bg-green-50 p-4 rounded-lg border border-green-100">
                    <h3 className="font-bold text-green-800 flex items-center mb-2"><Award className="w-4 h-4 mr-2"/> Fortalezas</h3>
                    <ul className="list-disc pl-4 space-y-1 text-sm text-green-700">
                      {swotAnalysis.fortalezas.map((item, i) => <li key={i}>{item}</li>)}
                    </ul>
                 </div>
                 {/* Debilidades */}
                 <div className="bg-red-50 p-4 rounded-lg border border-red-100">
                    <h3 className="font-bold text-red-800 flex items-center mb-2"><AlertTriangle className="w-4 h-4 mr-2"/> Debilidades</h3>
                    <ul className="list-disc pl-4 space-y-1 text-sm text-red-700">
                      {swotAnalysis.debilidades.map((item, i) => <li key={i}>{item}</li>)}
                    </ul>
                 </div>
                 {/* Oportunidades */}
                 <div className="bg-blue-50 p-4 rounded-lg border border-blue-100">
                    <h3 className="font-bold text-blue-800 flex items-center mb-2"><TrendingUp className="w-4 h-4 mr-2"/> Oportunidades</h3>
                    <ul className="list-disc pl-4 space-y-1 text-sm text-blue-700">
                      {swotAnalysis.oportunidades.map((item, i) => <li key={i}>{item}</li>)}
                    </ul>
                 </div>
                 {/* Amenazas */}
                 <div className="bg-amber-50 p-4 rounded-lg border border-amber-100">
                    <h3 className="font-bold text-amber-800 flex items-center mb-2"><Target className="w-4 h-4 mr-2"/> Amenazas</h3>
                    <ul className="list-disc pl-4 space-y-1 text-sm text-amber-700">
                      {swotAnalysis.amenazas.map((item, i) => <li key={i}>{item}</li>)}
                    </ul>
                 </div>
              </CardContent>
            </Card>

            <Card className="border-t-4 border-green-600 shadow-md">
               <CardHeader>
                 <CardTitle className="text-green-900">Métricas Clave</CardTitle>
               </CardHeader>
               <CardContent className="space-y-6">
                 <div>
                   <div className="flex justify-between text-sm font-medium mb-1">
                     <span>Asistencia vs Meta</span>
                     <span className="text-green-700">100%</span>
                   </div>
                   <Progress value={100} className="h-2 bg-green-100" />
                   <p className="text-xs text-gray-500 mt-1">200 participantes certificados</p>
                 </div>
                 <div>
                   <div className="flex justify-between text-sm font-medium mb-1">
                     <span>Cumplimiento Cronograma</span>
                     <span className="text-amber-700">98%</span>
                   </div>
                   <Progress value={98} className="h-2 bg-amber-100" />
                   <p className="text-xs text-gray-500 mt-1">Actividades ejecutadas a tiempo</p>
                 </div>
                 <div>
                   <div className="flex justify-between text-sm font-medium mb-1">
                     <span>Satisfacción Aliados</span>
                     <span className="text-blue-700">90%</span>
                   </div>
                   <Progress value={90} className="h-2 bg-blue-100" />
                   <p className="text-xs text-gray-500 mt-1">17 Empresas vinculadas</p>
                 </div>
               </CardContent>
               <CardFooter className="bg-stone-50 text-xs text-stone-500 italic p-4">
                 *Datos basados en informe final gestión y logística.
               </CardFooter>
            </Card>
          </div>
        </TabsContent>

        {/* --- CONTENIDO: FASES Y CRONOGRAMA --- */}
        <TabsContent value="fases">
          <Tabs defaultValue="antes" className="w-full">
            <div className="flex justify-center mb-6">
              <TabsList className="bg-stone-200 p-1 rounded-full">
                <TabsTrigger value="antes" className="rounded-full px-6 data-[state=active]:bg-amber-600 data-[state=active]:text-white">1. PRE (Antes)</TabsTrigger>
                <TabsTrigger value="durante" className="rounded-full px-6 data-[state=active]:bg-amber-600 data-[state=active]:text-white">2. PRO (Durante)</TabsTrigger>
                <TabsTrigger value="despues" className="rounded-full px-6 data-[state=active]:bg-amber-600 data-[state=active]:text-white">3. POST (Después)</TabsTrigger>
              </TabsList>
            </div>

            {['antes', 'durante', 'despues'].map((phaseKey) => (
              <TabsContent key={phaseKey} value={phaseKey} className="animate-in fade-in slide-in-from-bottom-2">
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                  {phases[phaseKey].map((commission, idx) => (
                    <Card key={idx} className={`border-t-4 ${commission.borderColor} hover:shadow-lg transition-all duration-300`}>
                      <CardHeader className={`${commission.bgLight} border-b border-stone-100 pb-4`}>
                        <div className="flex justify-between items-start">
                          <div className={`p-2.5 rounded-xl bg-white shadow-sm ${commission.color}`}>
                            <commission.icon className="w-6 h-6" />
                          </div>
                          <span className="text-[10px] font-bold px-2 py-1 rounded-full bg-white text-stone-500 uppercase tracking-wider border border-stone-100 shadow-sm">
                            Comisión
                          </span>
                        </div>
                        <CardTitle className={`text-lg mt-3 ${commission.color}`}>{commission.name}</CardTitle>
                        <CardDescription className="flex items-center text-xs font-medium text-stone-500">
                          <Users className="w-3 h-3 mr-1" /> {commission.lead}
                        </CardDescription>
                      </CardHeader>
                      
                      <CardContent className="pt-6">
                        {/* KPIs Rápidos */}
                        <div className="grid grid-cols-3 gap-2 mb-6">
                          {commission.stats.map((stat, sIdx) => (
                            <div key={sIdx} className="text-center p-2 rounded-lg bg-stone-50 border border-stone-100">
                              <p className="text-[9px] text-stone-400 uppercase font-bold tracking-wider">{stat.label}</p>
                              <p className="text-sm font-bold text-stone-700 mt-1">{stat.value}</p>
                            </div>
                          ))}
                        </div>

                        {/* Lista de Tareas */}
                        <div className="space-y-5">
                          {commission.tasks.map((task) => (
                            <div key={task.id} className="relative pl-4 border-l-2 border-stone-200">
                              <div className={`absolute -left-[5px] top-1 w-2.5 h-2.5 rounded-full ${task.progress === 100 ? 'bg-green-500' : 'bg-amber-400'}`}></div>
                              <div className="flex justify-between text-sm mb-1">
                                <span className="font-semibold text-stone-700">{task.activity}</span>
                                <span className={`text-xs font-bold ${task.progress === 100 ? 'text-green-600' : 'text-amber-600'}`}>{task.progress}%</span>
                              </div>
                              <p className="text-xs text-stone-500 leading-relaxed">
                                {task.details}
                              </p>
                            </div>
                          ))}
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </TabsContent>
            ))}
          </Tabs>
        </TabsContent>

        {/* --- CONTENIDO: MATRIZ DE ALIADOS --- */}
        <TabsContent value="aliados">
          <Card>
            <CardHeader className="bg-gradient-to-r from-blue-50 to-white">
              <CardTitle className="text-blue-900 flex items-center">
                <Handshake className="w-6 h-6 mr-2" />
                Matriz de Gestión de Alianzas
              </CardTitle>
              <CardDescription>
                Resumen de los 17 aliados estratégicos gestionados por la comisión de Gestión y Alianzas.
              </CardDescription>
            </CardHeader>
            <CardContent className="p-0">
               <div className="overflow-x-auto">
                 <table className="w-full text-sm text-left">
                   <thead className="text-xs text-stone-500 uppercase bg-stone-50 border-b">
                     <tr>
                       <th className="px-6 py-3">Tipo de Aliado</th>
                       <th className="px-6 py-3">Gestión</th>
                       <th className="px-6 py-3 text-center">Estado</th>
                       <th className="px-6 py-3 text-right">Aporte Principal</th>
                     </tr>
                   </thead>
                   <tbody className="divide-y divide-stone-100">
                     <tr className="hover:bg-stone-50 transition-colors">
                       <td className="px-6 py-4 font-medium text-stone-900">Universidades (Pereira)</td>
                       <td className="px-6 py-4">Cartas y visitas</td>
                       <td className="px-6 py-4 text-center"><span className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-bold">Confirmado</span></td>
                       <td className="px-6 py-4 text-right">Difusión y Aval Académico</td>
                     </tr>
                     <tr className="hover:bg-stone-50 transition-colors">
                       <td className="px-6 py-4 font-medium text-stone-900">Empresas de Insumos</td>
                       <td className="px-6 py-4">Llamadas y Propuestas</td>
                       <td className="px-6 py-4 text-center"><span className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-bold">Confirmado</span></td>
                       <td className="px-6 py-4 text-right">Stands y Muestras</td>
                     </tr>
                     <tr className="hover:bg-stone-50 transition-colors">
                       <td className="px-6 py-4 font-medium text-stone-900">Cooperativas de Café</td>
                       <td className="px-6 py-4">Gestión en especie</td>
                       <td className="px-6 py-4 text-center"><span className="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-bold">Confirmado</span></td>
                       <td className="px-6 py-4 text-right">Decoración y Refrigerios</td>
                     </tr>
                     <tr className="hover:bg-stone-50 transition-colors">
                       <td className="px-6 py-4 font-medium text-stone-900">IPS y Brigadas</td>
                       <td className="px-6 py-4">Convenios</td>
                       <td className="px-6 py-4 text-center"><span className="bg-amber-100 text-amber-800 px-2 py-1 rounded-full text-xs font-bold">Parcial</span></td>
                       <td className="px-6 py-4 text-right">Apoyo en Simulacros</td>
                     </tr>
                     <tr className="bg-stone-50 font-bold">
                       <td className="px-6 py-4 text-right" colSpan={3}>TOTAL ALIADOS ACTIVOS:</td>
                       <td className="px-6 py-4 text-right text-blue-700">17 ENTIDADES</td>
                     </tr>
                   </tbody>
                 </table>
               </div>
            </CardContent>
          </Card>
        </TabsContent>

      </Tabs>
    </div>
  );
};

export default DashboardCongreso;