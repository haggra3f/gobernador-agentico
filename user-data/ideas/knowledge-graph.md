# Knowledge Graph - Ideas

Sistema de gestión de conocimiento que captura, organiza y sintetiza ideas mediante un grafo de conocimiento.

**Total Ideas:** 4 (4 agentes conceptuales + 1 hub de sistemas)
**Last Updated:** 2025-10-21
**Agent:** ideas (Haiku)

---

## 📊 Estructura del Grafo

Este archivo mantiene todas las ideas en formato de grafo de conocimiento:

- **Nodos**: Cada idea con ID único
- **Relaciones**: Enlaces bidireccionales entre ideas
- **Tags**: Categorización y búsqueda rápida
- **Evolution Log**: Historia de cambios y síntesis

## 🎯 Tipos de Relaciones

| Tipo | Significado |
|------|-------------|
| **Extends** | Construye sobre el concepto |
| **Complements** | Funciona en conjunto |
| **Contradicts** | Enfoque alternativo |
| **Depends on** | Requiere entendimiento previo |
| **Merged into** | Idea fue integrada |
| **HUB** | Concepto integrador (conecta múltiples ideas) |

## 🔍 Búsqueda Rápida

```bash
# Por tag
grep "Tags:.*#nombre-tag" knowledge-graph.md

# Por palabra clave
grep -i "keyword" knowledge-graph.md

# Ideas activas
grep "Status: active" knowledge-graph.md
```

---

<!-- ========================================================================== -->
<!-- IDEAS COMIENZAN AQUÍ                                                       -->
<!-- ========================================================================== -->

<!-- Las ideas se agregarán automáticamente debajo de esta línea -->

---
# [ID: #001] 🏥 Agente de Salud - Predicciones y Recomendaciones Médicas

**Created:** 2025-10-18 16:45
**Status:** active
**Tags:** #agente #salud #medicina #predicciones #recomendaciones #IA #datos-usuario
**Related Ideas:** [[#002]]

## Core Concept
Agente especializado capaz de analizar información médica del usuario para realizar predicciones de salud y generar recomendaciones personalizadas.

## Details
**Capacidades:**
- Recopilación de información médica del usuario (historial, métricas, síntomas)
- Análisis de patrones y tendencias de salud
- Predicciones de riesgos potenciales
- Recomendaciones personalizadas de salud

**Consideraciones:**
- Privacidad: Datos médicos sensibles
- Regulación: Cumplimiento HIPAA/GDPR
- Disclaimer: No sustituye consejo médico profesional
- Storage: Información encriptada

**Tecnologías potenciales:**
- MCP server de salud (si existe)
- Base de datos segura para historial médico
- Modelo especializado en salud (Claude con contexto médico)

## Connections
- **Complements** [[#002]] - Alimentación es parte integral de salud
- **Requires** Sistema de almacenamiento seguro de datos médicos
- **Could integrate** con wearables (Apple Health, Google Fit)

## Evolution Log
- 2025-10-18 16:45 - Created from user idea

---
# [ID: #002] 🥗 Agente de Alimentación - Nutrición e Interconexión con Inventario

**Created:** 2025-10-18 16:45
**Status:** active
**Tags:** #agente #alimentación #nutrición #inventario #integración #salud
**Related Ideas:** [[#001]], [[inventory-librarian]]

## Core Concept
Agente especializado en nutrición que genera recomendaciones alimenticias y se interconecta con el agente de listas de mercado (inventory-librarian) para gestión práctica de compras saludables.

## Details
**Capacidades:**
- Análisis nutricional de alimentos
- Recomendaciones de dieta personalizadas
- Planificación de comidas
- **Interconexión bidireccional** con inventory-librarian:
  - Lee inventario disponible → sugiere recetas con lo que hay
  - Genera lista de compras saludables → actualiza "ideal-y-necesario"
  - Detecta items "agotados" → prioriza según nutrición

**Flujo de integración con inventory-librarian:**
```
User: "Qué puedo cocinar con lo que tengo?"
→ Agent alimentación lee Inventario/en-disponibilidad.md
→ Sugiere recetas basadas en items disponibles
→ Considera perfiles nutricionales

User: "Necesito comer más proteína"
→ Agent alimentación genera lista de alimentos proteicos
→ Actualiza Inventario/ideal-y-necesario.md
→ Agrega items a Inventario/deseado.md con prioridad nutricional
```

**Consideraciones:**
- Alergias y restricciones alimentarias del usuario
- Preferencias culinarias
- Presupuesto (integrado con costos en inventario)
- Temporada de alimentos

## Connections
- **Complements** [[#001]] - Salud y alimentación trabajan juntas
- **Integrates with** inventory-librarian (agente existente):
  - Lee: en-disponibilidad.md, agotado.md
  - Escribe: ideal-y-necesario.md, deseado.md
  - Prioriza compras por valor nutricional
- **Could extend** con APIs de recetas (Spoonacular, Edamam)
- **Could use** MCP server de bases de datos nutricionales

## Evolution Log
- 2025-10-18 16:45 - Created from user idea with explicit inventory-librarian integration

---
# [ID: #003] 🌟 HUB: Ecosistema de Bienestar Integral

**Type:** HUB CONCEPT
**Created:** 2025-10-18 16:47
**Status:** active
**Tags:** #hub #salud #alimentación #bienestar #ecosistema #agentes
**Connected Ideas:** [[#001]], [[#002]], [[inventory-librarian]]

## Core Concept
Ecosistema integrado de agentes especializados que trabajan conjuntamente para gestionar el bienestar integral del usuario: salud, alimentación y recursos prácticos.

## Hub Structure

### 🎯 Central Vision
Crear un sistema holístico donde datos de salud informan decisiones alimenticias, que a su vez se materializan en listas de compras prácticas gestionadas por el inventario.

### 🔗 Connected Agents & Flow

```
┌─────────────────┐
│  Agente Salud   │ ──┐
│     (#001)      │   │
└─────────────────┘   │
         │            ├──→ Recomendaciones integradas
         ▼            │
┌─────────────────┐   │
│ Agente Aliment. │ ──┘
│     (#002)      │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  inventory-lib  │ (existente)
│ Listas mercado  │
└─────────────────┘
```

#### → [[#001]] Agente de Salud
**Relación:** Proporciona **contexto médico** para decisiones alimenticias
**Flujo:** Métricas salud → Restricciones/objetivos → Alimentación

#### → [[#002]] Agente de Alimentación
**Relación:** **Traduce** recomendaciones de salud en planes de comida
**Flujo:** Objetivos nutricionales → Planificación → Listas de compra

#### → inventory-librarian (existente)
**Relación:** **Ejecuta** las decisiones con gestión práctica de inventario
**Flujo:** Lista de compras → Tracking disponibilidad → Feedback a alimentación

## Use Cases del Ecosistema

### Caso 1: Usuario con objetivo de salud
```
User: "Necesito bajar mi colesterol"

Agente Salud (#001):
- Analiza historial médico
- Identifica nivel actual de colesterol
- Genera recomendaciones: ↑ fibra, ↓ grasas saturadas

Agente Alimentación (#002):
- Recibe contexto de salud
- Genera plan: avena, legumbres, pescado, nueces
- Consulta inventario actual

inventory-librarian:
- Verifica qué hay disponible
- Agrega faltantes a "Agotado"
- Prioriza en "Ideal y necesario"

Response al usuario: "Tu plan para bajar colesterol requiere:
- Ya tienes: [items disponibles]
- Necesitas comprar: [lista generada]
- Recetas sugeridas: [basadas en disponible + a comprar]"
```

### Caso 2: Planificación desde inventario
```
User: "¿Qué puedo cocinar con lo que tengo?"

inventory-librarian:
- Lee en-disponibilidad.md
- Lista: pollo, arroz, brócoli, tomates

Agente Alimentación (#002):
- Recibe lista de disponibles
- Consulta perfil nutricional usuario (de agente salud)
- Genera 3 opciones de recetas saludables

Agente Salud (#001):
- Valida que opciones cumplan objetivos de salud
- Marca la más beneficiosa

Response: "Receta recomendada: Pollo al horno con brócoli
(alta proteína, bajo colesterol - alineado con tu objetivo)"
```

## Implementation Roadmap

**Fase 1 - MVP:**
1. Crear agente salud básico (input manual de métricas)
2. Crear agente alimentación con lectura de inventario
3. Probar integración básica

**Fase 2 - Integración:**
1. Conectar salud ↔ alimentación (recomendaciones)
2. Conectar alimentación ↔ inventory (lectura/escritura)
3. Flujo completo end-to-end

**Fase 3 - Avanzado:**
1. MCP servers (bases datos nutricionales, APIs recetas)
2. Integración con wearables (Apple Health, etc)
3. Machine learning para predicciones

## Technical Considerations

**Privacy & Security:**
- Datos médicos: encriptación, cumplimiento normativo
- Storage local vs cloud
- Permisos granulares de acceso

**Data Flow:**
- Agentes comparten contexto pero mantienen independencia
- Cache de recomendaciones para no re-calcular
- Inventario como source of truth para disponibilidad

## Evolution Log
- 2025-10-18 16:47 - Created as integrating hub for health ecosystem

---
# [ID: #004] 🎯 Agente Orquestador/Router - Coordinación Inteligente de Agentes

**Created:** 2025-10-19 12:15
**Status:** active
**Tags:** #arquitectura #orquestación #routing #agentes #optimización #sistema #modularidad
**Related Ideas:** (Sistema de agentes)

## Core Concept
Agente especializado en coordinación que actúa como router inteligente para decidir qué agente debe manejar cada tarea. Extrae la lógica de selección y routing de agentes de CLAUDE.md, reduciendo su tamaño y mejorando la mantenibilidad del sistema.

## Details

### Problema Actual
- CLAUDE.md contiene ~200+ líneas dedicadas a agent_registry, agent_selection_protocol, y proactive_agent_invocation rules
- Estas reglas son principalmente lógica de ruteo y coordinación de agentes
- Modificar reglas de routing requiere editar CLAUDE.md (archivo crítico del sistema)
- El archivo crítico está cerca del límite de tamaño (47.1k chars vs 40.0k límite)

### Solución: Agent Orchestrator
Agente especializado que centraliza toda la lógica de coordinación de agentes:

**Responsabilidades:**
1. **Protocol Management**: Mantiene registro completo de protocolos de todos los agentes
2. **Agent Routing**: Analiza cada tarea y determina qué agente ejecutarla
3. **Multi-agent Coordination**: Maneja escenarios complejos donde múltiples agentes deben colaborar
4. **Rule Updating**: Permite evolucionar reglas de routing sin tocar CLAUDE.md
5. **Disambiguation**: Para casos ambiguos, proporciona opciones estructuradas

### Casos de Uso

**Caso 1: Ruteo Directo (Simple)**
```
User: "Compré 2 litros de gasolina"

Orchestrator Analysis:
- Input: "compré" + item
- Pattern recognition: inventory update
- Decision: inventory-librarian (confidence: 99%)
- Action: Direct invocation

Result: Rápido, eficiente, sin overhead
```

**Caso 2: Ruteo Ambiguo (Complex)**
```
User: "Quiero crear un sistema que maneje múltiples agentes"

Orchestrator Analysis:
- Input: desarrollo + arquitectura + agentes
- Potential agents: desarrollador, ideas, orchestrator itself
- Confidence: ambiguo
- Action: Present disambiguation to user

Result: User elige → Orchestrator ejecuta elección
```

**Caso 3: Multi-agent Coordination**
```
User: "Dame un plan de comidas saludable considerando mis objetivos"

Orchestrator Analysis:
- Requiere: agente salud + agente alimentación + inventory-librarian
- Dependencies: salud → alimentación → inventory
- Action: Orquestar secuencia de invocaciones

Execution Plan:
1. health-agent → extrae objetivos/métricas
2. nutrition-agent → genera plan con contexto de salud
3. inventory-librarian → materializa lista de compras
4. orchestrator → sintetiza respuesta integrada

Result: Coordinación seamless entre 3 agentes
```

## Ventajas de Implementación

### Reducción de Tamaño
- Extrae ~200 líneas de CLAUDE.md
- CLAUDE.md: 47.1k chars → ~40k chars (soluciona límite)
- Mantiene funcionalidad completa en archivo externo

### Modularidad Mejorada
- Reglas de routing viven en archivo dedicado
- Facilita evolución sin tocar archivo crítico
- Permite versionamiento independiente de reglas

### Mantenibilidad
- Cambios en routing NO requieren backup/restore de CLAUDE.md
- Menos riesgo de corrupción de sistema por errores en reglas
- Auditoría clara de cambios en coordinación

### Flexibilidad
- Fácil agregar nuevos agentes sin modificar CLAUDE.md
- Reglas pueden ser más sofisticadas (ML-friendly)
- Soporte para patrones de orquestación complejos

## Desventajas / Consideraciones

### Indirección
- Problema: Agentes obvios requieren invocación extra (orchestrator → agente real)
- Impacto: Latencia mínima, pero existe
- Solución: Bypass directo para casos simples (ver "Solución Híbrida")

### Complejidad
- Introduce layer de indirección
- Requiere aprender nuevo protocolo
- Riesgo: Malconfiguraciones en routing

### Punto de Fallo
- Si orchestrator falla, no se pueden invocar otros agentes correctamente
- Mitigación: Fallback a CLAUDE.md rules para casos críticos

## Arquitectura Propuesta: Solución Híbrida

**Estrategia de dos capas:**

### Capa 1: Direct Routing (Permanece en CLAUDE.md)
Reglas simples y obvias para máxima eficiencia:
```
- "compré [item]" → inventory-librarian (directa)
- "qué hace [archivo]" → Explore (directa)
- "manda un email" → gmail-manager (directa)
```

**Beneficio:** Latencia nula para casos comunes (99% de uso)

### Capa 2: Intelligent Routing (Delegada a Orchestrator)
Casos ambiguos, complejos o multi-agentes:
```
- ¿Varios agentes podrían manejar esto?
- ¿Requiere coordinación multi-agente?
- ¿Patrón no reconocido directamente?
→ Invoke orchestrator para análisis inteligente
```

**Beneficio:** Flexibilidad para casos complejos sin overhead en casos simples

## Especificación Técnica

### Orchestrator Agent File Structure
```
.claude/agents/orchestrator.md

Contenidos:
1. Agent Protocol (cómo se invoca)
2. Agent Registry (completo y detallado)
3. Agent Selection Rules (lógica de decisión)
4. Multi-agent Coordination Patterns (patrones de orquestación)
5. Ambiguity Resolution Protocol (cuando no hay decisión clara)
6. Fallback Rules (qué hacer si no hay match)
```

### Integration Points with CLAUDE.md
```
CLAUDE.md (reducido):
- Mantiene: Core principles, synthesis_first, estado management
- Extrae: agent_registry (referencia en orchestrator)
- Extrae: agent_selection_protocol (referencia en orchestrator)
- Extrae: proactive_agent_invocation rules (referencia en orchestrator)
- Mantiene: Direct routing for common cases (performance)
- Agrega: Instruction to delegate ambiguous cases

Result: CLAUDE.md enfocado en principios, orchestrator enfocado en coordinación
```

## Implementation Roadmap

**Fase 1: Design & Extraction**
1. Documentar todas las reglas de routing actuales
2. Identificar patrones similares
3. Crear plantilla de orchestrator.md
4. Validar que cobertura = 100% de reglas actuales

**Fase 2: Orchestrator Implementation**
1. Crear .claude/agents/orchestrator.md con todas las reglas
2. Crear lógica de decisión estructurada
3. Probar con casos de uso actuales
4. Validar latencia aceptable

**Fase 3: CLAUDE.md Reduction**
1. Eliminar agent_registry (excepto referencia)
2. Eliminar agent_selection_protocol (excepto referencia)
3. Actualizar proactive_agent_invocation para incluir "delegate ambiguous to orchestrator"
4. Reducir tamaño a <40k chars
5. Hacer backup y deploying

**Fase 4: Integration & Validation**
1. Pruebas exhaustivas con orchestrator
2. Validar fallback rules funcionan
3. Monitoreo de performance
4. Documentar best practices de routing

## Performance Impact Analysis

### Latency Cost
- **Direct invocation:** ~10ms (invoke agent directly)
- **Via orchestrator:** ~50-100ms (analyze request → decide → invoke)
- **Impact:** Negligible para UI (percepción: mismo)
- **Mitigation:** Caching, direct routing para 99% casos

### Token Cost
- **Analysis overhead:** ~200-500 tokens por decisión de routing ambigua
- **Frequency:** ~5-10% de todas las invocaciones
- **Monthly cost:** Mínimo (marginal)

## Success Metrics

1. ✓ CLAUDE.md reduces to <40k chars
2. ✓ 100% of existing routing rules preserved
3. ✓ Latency <500ms for routed requests (99th percentile)
4. ✓ Support for multi-agent coordination patterns
5. ✓ Easy to add new agents without CLAUDE.md edits
6. ✓ Clear fallback behavior when ambiguous

## Connections
- **Extends** agent coordination concepts in CLAUDE.md
- **Solves** size constraint issue of CLAUDE.md
- **Complements** synthesis_first principle (modular, separated concerns)
- **Enables** future sophisticated multi-agent patterns
- **Could integrate with** ideas agent (for ambiguous cases requiring knowledge graph)

## Evolution Log
- 2025-10-19 12:15 - Created from architectural proposal
  - Problem: CLAUDE.md size constraints (47.1k vs 40k limit)
  - Solution: Extract agent coordination to dedicated orchestrator
  - Approach: Hybrid model (direct for simple, orchestrator for complex)
  - Impact: Modular, maintainable, scalable architecture

---
