# Plan de Ejecución: Arquitectura Jerárquica de Coordinación de Desarrollo

## Objetivo
Crear un agente coordinador intermedio `dev-coordinator` que maneje la categoría de desarrollo, reduciendo congestión en orchestrator.md mediante una arquitectura jerárquica: Main Thread → Orchestrator → Dev-Coordinator → Sub-agentes de desarrollo.

## Análisis

### Situación Actual
- **Agentes de desarrollo actuales**:
  - `desarrollador`: Desarrollo complejo con workflow Plan → Approval → Execute
  - `github-manager`: Operaciones git/GitHub (Haiku, ejecución directa)
  - `Explore`: **NO EXISTE** (mencionado en tarea pero no encontrado - posible gap)

- **Problema identificado**:
  - orchestrator.md está creciendo con múltiples agentes
  - Se beneficiaría de nivel intermedio de coordinación por categoría
  - Categoría "development" es suficientemente amplia para justificar coordinador especializado

### Arquitectura Propuesta
```
Main Thread
    ↓
Orchestrator (orchestrator.md) - Coordinación estratégica de alto nivel
    ↓
Dev-Coordinator (dev-coordinator.md) - Coordinación táctica de desarrollo
    ↓
    ├── desarrollador (desarrollo complejo, arquitectura, multi-archivo)
    ├── github-manager (git/GitHub operations)
    └── [Explore si existe, o crear gap entry]
```

### Decisiones de Diseño

**Dev-Coordinator**:
- **Modelo**: Haiku (routing rápido, decisiones determinísticas)
- **Modo**: Direct Execution (router, no planifica)
- **Responsabilidad**: Clasificar tareas de desarrollo y delegar a sub-agentes
- **Valor agregado**: Consolidación de respuestas, reducción de complejidad en orchestrator

**Cambios Requeridos**:
1. ✅ Crear `dev-coordinator.md`
2. ✅ Actualizar `orchestrator.md` (refactorización significativa)
3. ⚠️ Verificar si `CLAUDE.md` necesita actualización (probablemente NO - ya delega a orchestrator)
4. ✅ Validar flujo de routing completo

## Steps

### Step 1: Diseñar dev-coordinator.md
- Analizar patrones de desarrollador y github-manager para entender triggers y capabilities
- Diseñar lógica de routing para clasificar tareas de desarrollo
- Crear frontmatter con metadata apropiada
- Documentar protocolo de consolidación de respuestas
- Incluir ejemplos de routing decisions
- Definir anti-patterns y reglas de encapsulación

### Step 2: Crear archivo dev-coordinator.md
- Ubicación: `.claude/agents/dev-coordinator.md`
- Frontmatter: name, description, model (haiku), color
- Secciones completas: Purpose, Capabilities, Routing Logic, Delegation Protocol, Examples
- Registry de sub-agentes: desarrollador, github-manager, [nota sobre Explore gap]

### Step 3: Refactorizar orchestrator.md
- Leer orchestrator.md completo (ya leído)
- Crear nueva sección para dev-coordinator en registry
- Actualizar Decision Matrix para delegar "development" a dev-coordinator
- Mover desarrollador y github-manager a sección de "sub-agents managed by dev-coordinator"
- Actualizar Agent Encapsulation Policy para incluir dev-coordinator
- Mantener todos los tracking fields y gap tracking system intactos
- Verificar que otros agentes (inventory, gmail, ideas) no se vean afectados

### Step 4: Validar arquitectura jerárquica
- Verificar que no hay loops de delegación
- Confirmar que routing fluye: Main → Orchestrator → Dev-Coordinator → Sub-agent
- Validar que dev-coordinator retorna información consolidada (no verbosa)
- Verificar que desarrollador mantiene su workflow Plan → Approval → Execute intacto
- Confirmar que github-manager mantiene ejecución directa

### Step 5: Actualizar CLAUDE.md (si necesario)
- Leer CLAUDE.md actual (ya leído)
- Verificar task_categories y routing_patterns
- **Decisión preliminar**: PROBABLEMENTE NO REQUIERE CAMBIOS
  - CLAUDE.md ya delega "development" a orchestrator
  - Orchestrator se encarga de routing granular (incluyendo a dev-coordinator)
  - Arquitectura de separación ya está correcta
- Solo actualizar si encontramos inconsistencia

### Step 6: Documentar validación
- Crear ejemplos de flujo completo de routing
- Documentar casos de prueba cubiertos
- Confirmar que Gap Tracking System sigue funcionando
- Validar que execution tracking sigue intacto
- Reportar arquitectura final

## Tools
- Read (leer archivos existentes - ya usado)
- Write (crear dev-coordinator.md)
- Edit (actualizar orchestrator.md, posiblemente CLAUDE.md)
- Grep (validar referencias y consistencia)

## Verification

### Criterios de Éxito
1. ✅ dev-coordinator.md creado con estructura completa y routing logic clara
2. ✅ orchestrator.md actualizado con dev-coordinator en registry
3. ✅ Decision Matrix en orchestrator delega "development" a dev-coordinator
4. ✅ Sub-agentes (desarrollador, github-manager) correctamente asociados a dev-coordinator
5. ✅ No loops de delegación (routing es unidireccional y claro)
6. ✅ Información retornada es consolidada, no verbosa
7. ✅ CLAUDE.md consistente con nueva arquitectura (o sin cambios si no necesario)
8. ✅ Gap Tracking System y Execution Tracking intactos
9. ✅ Documentación de validación completa con ejemplos

### Validación de Routing
**Test Case 1**: "Implementa autenticación JWT"
- Main → Orchestrator → Dev-Coordinator → desarrollador

**Test Case 2**: "Crea un PR para esta feature"
- Main → Orchestrator → Dev-Coordinator → github-manager

**Test Case 3**: "¿Cómo funciona el auth system?" (si Explore existe)
- Main → Orchestrator → Dev-Coordinator → Explore
- (Si Explore no existe: Gap tracking + fallback)

**Test Case 4**: "Compré café" (NO development)
- Main → Orchestrator → inventory-librarian (NO pasa por dev-coordinator)

## Notas Importantes

### Sobre Explore Agent
- **NO encontrado en `.claude/agents/Explore.md`**
- Mencionado en orchestrator.md registry (líneas 235-265)
- **Acción**: Verificar si existe o si debe estar en Gap Tracking System
- Si no existe: Documentar como gap y omitir de dev-coordinator registry

### Crítico: Synthesis Protocol
- Aplicar Synthesis Protocol al actualizar orchestrator.md
- NO duplicar información - consolidar inteligentemente
- Preservar estructura y tracking existente
- Mejorar organización, no destruir lo que funciona

### Cambio Arquitectural Significativo
- Este cambio introduce jerarquía de coordinación (L1: Orchestrator, L2: Dev-Coordinator)
- Escalabilidad: Permite crear coordinadores por categoría (email-coordinator, knowledge-coordinator, etc.)
- Precedente: Si funciona bien, replicable para otras categorías cuando crezcan
