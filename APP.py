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
  Coffee,
  PieChart as PieChartIcon,
  BarChart as BarChartIcon,
  AlertTriangle,
  Handshake,
  MapPin,
  Info,
  ChevronRight
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Progress } from "@/components/ui/progress";

// --- COMPONENTES DE GRÁFICOS PERSONALIZADOS (SVG Puro) ---

const DonutChart = ({ data, colors, title }: { data: { name: string, value: number }[], colors: string[], title?: string }) => {
  const total = data.reduce((acc, item) => acc + item.value, 0);
  let currentAngle = 0;

  return (
    <div className="flex flex-col items-center justify-center p-4">
      <div className="relative w-48 h-48">
        <svg viewBox="0 0 100 100" className="transform -rotate-90 w-full h-full shadow-sm rounded-full">
          {data.map((item, index) => {
            const angle = (item.value / total) * 360;
            const x1 = 50 + 40 * Math.cos((Math.PI * currentAngle) / 180);
            const y1 = 50 + 40 * Math.sin((Math.PI * currentAngle) / 180);
            const x2 = 50 + 40 * Math.cos((Math.PI * (currentAngle + angle)) / 180);
            const y2 = 50 + 40 * Math.sin((Math.PI * (currentAngle + angle)) / 180);
            const largeArcFlag = angle > 180 ? 1 : 0;
            const pathData = `M 50 50 L ${x1} ${y1} A 40 40 0 ${largeArcFlag} 1 ${x2} ${y2} Z`;
            currentAngle += angle;
            return <path key={index} d={pathData} fill={colors[index % colors.length]} stroke="white" strokeWidth="1" className="hover:opacity-90 transition-opacity cursor-pointer"/>;
          })}
          <circle cx="50" cy="50" r="25" fill="white" />
        </svg>
        {title && (
           <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
             <span className="text-[10px] font-bold text-center text-gray-400 leading-tight">{title}</span>
           </div>
        )}
      </div>
      <div className="mt-4 grid grid-cols-2 gap-x-4 gap-y-1">
        {data.map((item, index) => (
          <div key={index} className="flex items-center text-xs">
            <span className="w-2.5 h-2.5 rounded-full mr-2 shadow-sm" style={{ backgroundColor: colors[index % colors.length] }}></span>
            <span className="text-gray-600 truncate max-w-[100px]">{item.name}: <strong>{item.value}</strong></span>
          </div>
        ))}
      </div>
    </div>
  );
};

const HorizontalBarChart = ({ data, color }: { data: { label: string, value: number, max: number }[], color: string }) => {
  return (
    <div className="space-y-3 w-full">
      {data.map((item, index) => (
        <div key={index} className="w-full">
          <div className="flex justify-between text-xs mb-1 font-medium text-gray-700">
            <span>{item.label}</span>
            <span>{item.value}%</span>
          </div>
          <div className="w-full bg-gray-100 rounded-full h-3 overflow-hidden">
            <div 
              className={`h-full rounded-full ${color} transition-all duration-1000 ease-out`} 
              style={{ width: `${(item.value / item.max) * 100}%` }}
            ></div>
          </div>
        </div>
      ))}
    </div>
  );
};

// --- ESTRUCTURA DE DATOS ---

const DashboardCongreso = () => {
  const [activeTab, setActiveTab] = useState('general');

  // Datos para Gráficos
  const aliadosData = [
    { name: "Insumos Médicos", value: 10 },
    { name: "Universidades", value: 4 },
    { name: "Café/Alimentos", value: 3 }
  ];

  const asistentesData = [
    { name: "Estudiantes UTP", value: 140 },
    { name: "Externos/Profesionales", value: 40 },
    { name: "Staff/Ponentes", value: 20 }
  ];

  const cumplimientoData = [
    { label: "Gestión Financiera (Patrocinios)", value: 91, max: 100 },
    { label: "Logística (Montaje y Tiempos)", value: 98, max: 100 },
    { label: "Comunicaciones (Cobertura)", value: 100, max: 100 },
    { label: "Asistencia (Aforo)", value: 100, max: 100 }
  ];

  // Datos Detallados por Fases (Con Tablas)
  const phases = {
    antes: [
      {
        name: "Gestión y Alianzas",
        lead: "David Muñoz & Andrés Álvarez",
        icon: Briefcase,
        color: "text-blue-700",
        border: "border-blue-500",
        bg: "bg-blue-50",
        indicators: [
          { item: "Base de Datos Aliados", meta: "1 BD", ejec: "1 BD", perc: 100 },
          { item: "Contactar Empresas Insumos", meta: "11", ejec: "10", perc: 91 },
          { item: "Contactar IPS/Brigadas", meta: "12", ejec: "7", perc: 58 },
          { item: "Gestión Universidades", meta: "5", ejec: "5", perc: 100 }
        ]
      },
      {
        name: "Logística",
        lead: "Santiago Rendón & Leymar Portilla",
        icon: Layout,
        color: "text-amber-700",
        border: "border-amber-500",
        bg: "bg-amber-50",
        indicators: [
          { item: "Contactar Ponentes", meta: "20", ejec: "20", perc: 100 },
          { item: "Diseño Certificados", meta: "1", ejec: "1", perc: 100 },
          { item: "Gestión Mobiliario", meta: "100%", ejec: "100%", perc: 100 },
          { item: "Decoración Cafetera", meta: "50 ítems", ejec: "50", perc: 100 }
        ]
      },
      {
        name: "Comunicaciones",
        lead: "Joan Sebastian Arango",
        icon: Megaphone,
        color: "text-green-700",
        border: "border-green-500",
        bg: "bg-green-50",
        indicators: [
          { item: "Manual de Marca", meta: "1", ejec: "1", perc: 100 },
          { item: "Campaña Expectativa", meta: "3 Olas", ejec: "3 Olas", perc: 100 },
          { item: "Video Teaser", meta: "1", ejec: "1", perc: 100 },
          { item: "Diseño Escarapelas", meta: "3 Tipos", ejec: "3 Tipos", perc: 100 }
        ]
      }
    ],
    durante: [
      {
        name: "Gestión y Alianzas",
        lead: "Equipo Gestión",
        icon: Briefcase,
        color: "text-blue-700",
        border: "border-blue-500",
        bg: "bg-blue-50",
        indicators: [
          { item: "Supervisión Stands", meta: "15", ejec: "15", perc: 100 },
          { item: "Entrega Refrigerios", meta: "200", ejec: "200", perc: 100 },
          { item: "Registro Aliados", meta: "17", ejec: "15", perc: 88 }
        ]
      },
      {
        name: "Logística",
        lead: "Equipo Logística",
        icon: Layout,
        color: "text-amber-700",
        border: "border-amber-500",
        bg: "bg-amber-50",
        indicators: [
          { item: "Soporte Auditorio", meta: "100%", ejec: "100%", perc: 100 },
          { item: "Control Asistencia", meta: "200", ejec: "200", perc: 100 },
          { item: "Talleres Edif. 14", meta: "6", ejec: "6", perc: 100 }
        ]
      },
      {
        name: "Comunicaciones",
        lead: "Equipo Comunicaciones",
        icon: Megaphone,
        color: "text-green-700",
        border: "border-green-500",
        bg: "bg-green-50",
        indicators: [
          { item: "Cobertura Ponencias", meta: "12", ejec: "12", perc: 100 },
          { item: "Entrevistas", meta: "10", ejec: "8", perc: 80 },
          { item: "Stories en Vivo", meta: "50", ejec: "50+", perc: 100 }
        ]
      }
    ],
    despues: [
      {
        name: "Cierre General",
        lead: "Todas las Comisiones",
        icon: CheckCircle,
        color: "text-purple-700",
        border: "border-purple-500",
        bg: "bg-purple-50",
        indicators: [
          { item: "Cartas Agradecimiento", meta: "17", ejec: "17", perc: 100 },
          { item: "Certificados Enviados", meta: "200", ejec: "200", perc: 100 },
          { item: "Memorias Digitales", meta: "1 Pack", ejec: "1 Pack", perc: 100 },
          { item: "Informe Final", meta: "1", ejec: "1", perc: 100 }
        ]
      }
    ]
  };

  return (
    <div className="min-h-screen bg-stone-100 p-4 md:p-6 font-sans text-stone-800">
      
      {/* --- HEADER CON IDENTIDAD VISUAL --- */}
      <header className="relative bg-stone-900 rounded-2xl shadow-xl overflow-hidden mb-8 border-b-8 border-amber-600">
        <div className="absolute inset-0 z-0">
          <img 
            src="image_2141b3.jpg" 
            alt="Fondo Congreso" 
            className="w-full h-full object-cover opacity-40 mix-blend-overlay"
            onError={(e) => { (e.target as HTMLImageElement).style.display = 'none'; }}
          />
          <div className="absolute inset-0 bg-gradient-to-r from-stone-900 via-stone-900/90 to-transparent"></div>
        </div>

        <div className="relative z-10 p-6 flex flex-col md:flex-row items-center gap-8">
          {/* Logo Container */}
          <div className="w-40 h-40 bg-white/10 backdrop-blur-md rounded-full border-2 border-amber-500/50 flex items-center justify-center shrink-0 shadow-2xl p-4">
             <img 
               src="logotipo congreso medicina prehospitalaria (2).png" 
               alt="Logo Congreso" 
               className="w-full h-full object-contain filter drop-shadow-lg"
               onError={(e) => { (e.target as HTMLImageElement).src = 'https://placehold.co/150x150/FFF/B45309?text=Logo+XI+Congreso'; }}
             />
          </div>
          
          <div className="text-center md:text-left text-white flex-1">
            <div className="inline-flex items-center px-3 py-1 rounded-full bg-amber-600/30 border border-amber-500 text-amber-300 text-xs font-bold mb-3 uppercase tracking-wider">
              <Coffee className="w-3 h-3 mr-2" /> Edición Especial: Identidad Cafetera
            </div>
            <h1 className="text-3xl md:text-5xl font-extrabold leading-tight mb-2">
              XI Congreso Nacional <br/>
              <span className="text-amber-500">Medicina Prehospitalaria</span>
            </h1>
            <div className="flex flex-wrap gap-4 mt-4 justify-center md:justify-start">
              <span className="flex items-center text-sm font-medium bg-white/10 px-4 py-2 rounded-lg border border-white/5">
                <Calendar className="w-4 h-4 mr-2 text-amber-400" /> 23-25 Octubre 2025
              </span>
              <span className="flex items-center text-sm font-medium bg-white/10 px-4 py-2 rounded-lg border border-white/5">
                <MapPin className="w-4 h-4 mr-2 text-amber-400" /> Aud. Jorge Roa & Edificio 14 (UTP)
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* --- NAVEGACIÓN PRINCIPAL --- */}
      <Tabs defaultValue="general" className="space-y-6" onValueChange={setActiveTab}>
        
        <div className="sticky top-4 z-50 bg-white/95 backdrop-blur-sm p-2 rounded-xl shadow-md border border-stone-200">
          <TabsList className="grid grid-cols-2 md:grid-cols-4 w-full bg-stone-100 p-1">
            <TabsTrigger value="general" className="data-[state=active]:bg-white data-[state=active]:text-amber-700 font-medium">
              <PieChartIcon className="w-4 h-4 mr-2" /> Visión General
            </TabsTrigger>
            <TabsTrigger value="antes" className="data-[state=active]:bg-amber-600 data-[state=active]:text-white font-medium">
              <Clock className="w-4 h-4 mr-2" /> 1. Pre-Evento
            </TabsTrigger>
            <TabsTrigger value="durante" className="data-[state=active]:bg-amber-600 data-[state=active]:text-white font-medium">
              <ActivityIcon className="w-4 h-4 mr-2" /> 2. Durante
            </TabsTrigger>
            <TabsTrigger value="despues" className="data-[state=active]:bg-amber-600 data-[state=active]:text-white font-medium">
              <CheckCircle className="w-4 h-4 mr-2" /> 3. Post-Evento
            </TabsTrigger>
          </TabsList>
        </div>

        {/* --- TAB 1: VISIÓN GENERAL (GRÁFICOS + DOFA) --- */}
        <TabsContent value="general" className="space-y-6 animate-in fade-in zoom-in-95 duration-300">
          
          {/* Fila de Gráficos */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card className="shadow-lg border-t-4 border-blue-600">
              <CardHeader className="pb-2">
                <CardTitle className="text-lg text-blue-900 text-center">Aliados Estratégicos</CardTitle>
                <CardDescription className="text-center">Total: 17 Entidades</CardDescription>
              </CardHeader>
              <CardContent>
                <DonutChart 
                  data={aliadosData} 
                  colors={['#1e40af', '#3b82f6', '#93c5fd']} 
                  title="Gestión"
                />
              </CardContent>
            </Card>

            <Card className="shadow-lg border-t-4 border-amber-600">
              <CardHeader className="pb-2">
                <CardTitle className="text-lg text-amber-900 text-center">Asistencia</CardTitle>
                <CardDescription className="text-center">Total: ~200 Participantes</CardDescription>
              </CardHeader>
              <CardContent>
                <DonutChart 
                  data={asistentesData} 
                  colors={['#b45309', '#f59e0b', '#fcd34d']}
                  title="Aforo"
                />
              </CardContent>
            </Card>

            <Card className="shadow-lg border-t-4 border-green-600">
              <CardHeader className="pb-2">
                <CardTitle className="text-lg text-green-900 text-center">Cumplimiento Global</CardTitle>
                <CardDescription className="text-center">Por áreas de gestión</CardDescription>
              </CardHeader>
              <CardContent className="pt-6">
                <HorizontalBarChart data={cumplimientoData} color="bg-green-600" />
              </CardContent>
            </Card>
          </div>

          {/* DOFA Resumido */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <Card className="bg-gradient-to-br from-white to-green-50 border border-green-200">
              <CardHeader>
                <CardTitle className="flex items-center text-green-800"><Award className="w-5 h-5 mr-2" /> Fortalezas</CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-green-900 font-medium">
                  <li className="flex items-start"><CheckCircle className="w-4 h-4 mr-2 mt-0.5 text-green-600"/> Identidad Cafetera clara y transversal.</li>
                  <li className="flex items-start"><CheckCircle className="w-4 h-4 mr-2 mt-0.5 text-green-600"/> Capacidad de gestión (17 aliados sin presupuesto inicial).</li>
                  <li className="flex items-start"><CheckCircle className="w-4 h-4 mr-2 mt-0.5 text-green-600"/> Trabajo articulado entre 3 comisiones.</li>
                </ul>
              </CardContent>
            </Card>
            <Card className="bg-gradient-to-br from-white to-red-50 border border-red-200">
              <CardHeader>
                <CardTitle className="flex items-center text-red-800"><AlertTriangle className="w-5 h-5 mr-2" /> Oportunidades de Mejora</CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-red-900 font-medium">
                  <li className="flex items-start"><Info className="w-4 h-4 mr-2 mt-0.5 text-red-600"/> Mayor anticipación en piezas gráficas.</li>
                  <li className="flex items-start"><Info className="w-4 h-4 mr-2 mt-0.5 text-red-600"/> Recursos técnicos propios limitados.</li>
                  <li className="flex items-start"><Info className="w-4 h-4 mr-2 mt-0.5 text-red-600"/> Dependencia alta de gestión externa para decoración.</li>
                </ul>
              </CardContent>
            </Card>
          </div>
        </TabsContent>

        {/* --- TABS FASES (CON TABLAS DETALLADAS) --- */}
        {['antes', 'durante', 'despues'].map((phaseKey) => (
          <TabsContent key={phaseKey} value={phaseKey} className="animate-in slide-in-from-right-4 duration-300">
            <div className="grid grid-cols-1 gap-6">
              {phases[phaseKey].map((commission, idx) => (
                <Card key={idx} className={`border-l-8 ${commission.border} shadow-md overflow-hidden`}>
                  <CardHeader className={`${commission.bg} border-b border-stone-100 py-4`}>
                    <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                      <div className="flex items-center gap-4">
                        <div className={`p-3 rounded-full bg-white shadow-sm ${commission.color}`}>
                          <commission.icon className="w-6 h-6" />
                        </div>
                        <div>
                          <CardTitle className={`text-xl ${commission.color}`}>{commission.name}</CardTitle>
                          <CardDescription className="flex items-center mt-1 text-stone-600 font-medium">
                            <Users className="w-3 h-3 mr-1" /> Líderes: {commission.lead}
                          </CardDescription>
                        </div>
                      </div>
                      <div className="bg-white px-4 py-2 rounded-lg border border-stone-200 shadow-sm">
                        <span className="text-xs uppercase font-bold text-stone-400">Estado Fase</span>
                        <div className="flex items-center text-green-600 font-bold text-sm">
                          <CheckCircle className="w-4 h-4 mr-1" /> Completado 100%
                        </div>
                      </div>
                    </div>
                  </CardHeader>
                  
                  <CardContent className="p-0">
                    <div className="overflow-x-auto">
                      <table className="w-full text-sm text-left">
                        <thead className="bg-stone-50 text-stone-500 uppercase text-xs font-bold border-b border-stone-200">
                          <tr>
                            <th className="px-6 py-4">Indicador / Actividad</th>
                            <th className="px-6 py-4 text-center">Meta</th>
                            <th className="px-6 py-4 text-center">Ejecutado</th>
                            <th className="px-6 py-4 text-center">Estado</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-stone-100">
                          {commission.indicators.map((ind, i) => (
                            <tr key={i} className="hover:bg-stone-50/50 transition-colors">
                              <td className="px-6 py-4 font-medium text-stone-700 flex items-center">
                                <ChevronRight className="w-3 h-3 mr-2 text-stone-400" />
                                {ind.item}
                              </td>
                              <td className="px-6 py-4 text-center text-stone-500">{ind.meta}</td>
                              <td className="px-6 py-4 text-center font-bold text-stone-800">{ind.ejec}</td>
                              <td className="px-6 py-4 text-center">
                                <div className="flex items-center justify-center gap-2">
                                  <Progress value={ind.perc} className={`w-16 h-2 ${
                                    ind.perc >= 100 ? 'bg-green-100' : 'bg-amber-100'
                                  }`} />
                                  <span className={`text-xs font-bold ${
                                    ind.perc >= 100 ? 'text-green-700' : 
                                    ind.perc >= 80 ? 'text-amber-700' : 'text-red-700'
                                  }`}>
                                    {ind.perc}%
                                  </span>
                                </div>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </CardContent>
                  {/* Pequeño footer por tarjeta para resaltar un logro clave */}
                  <CardFooter className="bg-stone-50/50 p-3 text-xs text-stone-500 italic border-t border-stone-100 flex items-center justify-center">
                    <Info className="w-3 h-3 mr-1" /> Datos extraídos del informe final de {commission.name}
                  </CardFooter>
                </Card>
              ))}
            </div>
          </TabsContent>
        ))}

      </Tabs>

      {/* --- FOOTER: MATRIZ DE ALIADOS --- */}
      <div className="mt-8">
        <Card className="border-t-4 border-stone-600 shadow-xl bg-stone-800 text-stone-100">
          <CardHeader>
            <CardTitle className="flex items-center text-white">
              <Handshake className="w-6 h-6 mr-3 text-amber-500" /> 
              Resumen de Alianzas (Matriz)
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
              <div className="p-4 bg-stone-700/50 rounded-lg border border-stone-600">
                <p className="text-amber-400 text-2xl font-bold">17</p>
                <p className="text-xs uppercase tracking-wider opacity-80">Aliados Totales</p>
              </div>
              <div className="p-4 bg-stone-700/50 rounded-lg border border-stone-600">
                <p className="text-blue-400 text-2xl font-bold">5</p>
                <p className="text-xs uppercase tracking-wider opacity-80">Universidades</p>
              </div>
              <div className="p-4 bg-stone-700/50 rounded-lg border border-stone-600">
                <p className="text-green-400 text-2xl font-bold">10</p>
                <p className="text-xs uppercase tracking-wider opacity-80">Empresas Privadas</p>
              </div>
              <div className="p-4 bg-stone-700/50 rounded-lg border border-stone-600">
                <p className="text-purple-400 text-2xl font-bold">2</p>
                <p className="text-xs uppercase tracking-wider opacity-80">Cooperativas</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

// Icon helper
const ActivityIcon = (props: any) => (
  <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
)

export default DashboardCongreso;
