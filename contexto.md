# Contexto del Proyecto: Gobernador Agentico

Ultima actualizacion: 2025-10-17

## Proposito del Proyecto

Sistema de coordinacion agentica con capacidades de sintesis y comandos reflexivos. El proyecto implementa un ecosistema de agentes especializados coordinados por Claude Code, donde tareas complejas de desarrollo son delegadas a agentes especializados mientras se mantienen capacidades de meta-directivas para evolucion del sistema.

## Arquitectura del Sistema

### Tier 1: Agente Coordinador Principal
- **Claude Code**: Coordinador principal del sistema
- **Responsabilidades**:
  - Coordinacion de agentes especializados
  - Gestion de conocimiento y documentacion
  - Comandos reflexivos (*recuerda*, *evoluciona*)
  - Principio Synthesis First (actualizacion sobre creacion)
  - Tracking de uso de tokens
  - Manejo de estado (contexto.md)

### Tier 2: Agentes de Desarrollo Complejo
- **desarrollador**: Agente para tareas de desarrollo complejas
  - Workflow: Plan → Aprobacion → Ejecucion → Reporte
  - Maneja archivos de estado: plan.md, project-tracking.md
  - Contiene directivas completas de CLAUDE.md
  - Triggers: Codigo complejo, arquitectura, multi-archivo, features grandes

### Tier 3: Agentes Operacionales
- **inventory-librarian**: Gestion de inventarios
  - Ejecucion directa sin workflow de aprobacion
  - Maneja: ideal-y-necesario, en-disponibilidad, agotado, deseado
  - Triggers: Adquisiciones, depletions, queries de inventario, deseos

- **Explore**: Exploracion de codebase
  - Ejecucion directa sin workflow de aprobacion
  - Niveles: quick, medium, very thorough
  - Triggers: Preguntas de codigo, patrones, comprension de sistemas

## Estructura de Directorios

```
/mnt/d/Proyectos/Gobernador agentico/
├── .claude/
│   ├── CLAUDE.md                    # Sistema de coordinacion principal (v2.1)
│   ├── settings.local.json          # Permisos de lectura
│   └── agents/
│       ├── desarrollador.md         # Agente de desarrollo complejo
│       ├── inventory-librarian.md   # Agente de gestion de inventario
│       └── ... [otros agentes especializados]
├── user-data/                       # NUEVA: Datos del usuario (NO versionados)
│   ├── secrets.env                  # Configuracion sensible (gitignored)
│   ├── inventory/                   # Datos de inventory-librarian
│   │   ├── en-disponibilidad.md
│   │   ├── ideal-y-necesario.md
│   │   ├── agotado.md
│   │   └── deseado.md
│   ├── ideas/                       # Datos de ideas agent
│   │   └── knowledge-graph.md
│   └── knowledge/                   # Base de conocimiento
│       ├── index.md
│       ├── errores.md
│       └── auditoria-ERROR-001.md
├── contexto.md                      # Este archivo
├── plan.md                          # Plan activo del agente desarrollador
└── .env.example                     # Plantilla de configuracion (versionada)
```

## Archivos de Estado

### Gestionados por Claude Code
- **contexto.md**: Awareness continua del proyecto (este archivo)
- Actualizacion: Cuando se ganan insights significativos del proyecto

### Gestionados por Agente Desarrollador
- **plan.md**: Plan de ejecucion para tarea activa
- **project-tracking.md**: Master tracker de progreso (actualmente no existe)

## Principios Core

### Synthesis First (Critical/Mandatory)
- Siempre actualizar contenido existente antes de crear nuevo
- Protocolo: Read → Analyze → Merge → Preserve → Create (last resort)
- Aplica a: Codigo, documentacion, reglas, estado de proyecto

### Knowledge Management
Base: `user-data/knowledge/` (configurado via ${KNOWLEDGE_BASE_PATH})
- Priority 1: Consultar user-data/knowledge/index.md
- Priority 2: Busqueda externa si insuficiente
- Priority 3: Documentar hallazgos con Synthesis Protocol

## Comandos Reflexivos

### *recuerda*
Agregar nuevas reglas sistemicas a CLAUDE.md usando Synthesis Protocol

### *evoluciona*
Auto-analisis critico y mejora evolutiva de CLAUDE.md
- Usa thinking mode
- Preserva meta-directivas
- Maximo 30% de cambios por iteracion
- Refinamiento, no revolucion

## Tecnologias y Herramientas

- **Plataforma**: Linux (WSL2)
- **Coordinacion**: Claude Code CLI
- **Sistema de Agentes**: Arquitectura de 3 tiers (Coordinador → Desarrollo → Operacional)
- **Gestion de Estado**: Archivos markdown
- **Version Control**: Sin repositorio git actualmente

## Estado Actual del Proyecto

### Evolucion Reciente (v1.3 - 2025-10-17)
- Delegacion de workflow complejo a agente desarrollador
- Simplificacion de CLAUDE.md (~30% reduccion)
- Enfoque en coordinacion de agentes + capacidades reflexivas
- Separacion clara: desarrollo complejo vs tareas operacionales

### Inventario Activo
- Sistema de inventario operacional
- 2 items en disponibilidad (uvas verdes y rojas)
- Perecederos con tracking de caducidad

### Plan Activo
Creacion de agente "Desarrollador" (completo segun plan.md)
- Objetivo: Separar workflow complejo de operaciones simples
- Estado: Implementacion aparentemente completa

## Insights de Arquitectura

1. **Delegacion Inteligente**: El coordinador no ejecuta desarrollo complejo, delega a agente especializado
2. **Proactividad de Agentes**: Invocacion automatica sin esperar instruccion explicita del usuario
3. **Flujo de Aprobacion**: El coordinador debe relay preguntas de aprobacion y re-invocar agentes para mantener contexto
4. **Synthesis sobre Creacion**: Anti-patron fundamental: crear archivos nuevos cuando se pueden extender existentes

## Notas Importantes

- Sistema de autenticacion sudo: password configurado en user-data/secrets.env via ${SUDO_PASSWORD}
- Token tracking: Reportar uso al final de CADA respuesta
- No usar emojis a menos que el usuario lo solicite explicitamente
- Paths absolutos siempre, nunca relativos
