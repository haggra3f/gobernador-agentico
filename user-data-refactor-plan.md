# Plan: Refactorización Arquitectónica - Estructura de Datos del Usuario

**Estado:** Pendiente aprobación
**Prioridad:** Alta (Seguridad y Arquitectura)
**Estimado:** 2-4 horas de ejecución
**Riesgo:** Medio (Múltiples archivos a refactorizar)

## Objetivo

Crear una arquitectura centralizada para datos del usuario que:
1. Separe datos sensibles del código versionado en GitHub
2. Elimine rutas hard-coded del sistema (aplicar principios dinámicos)
3. Implemente referencias dinámicas mediante variables de entorno o configuración
4. Proteja información sensible (contraseñas, configuraciones privadas)
5. Organice datos por microagente de forma escalable y mantenible

## Contexto Actual

### Estructura Existente
```
/mnt/d/Proyectos/Gobernador agentico/
├── .claude/
│   ├── agents/
│   │   ├── inventory-librarian.md     (hardcoded path: inventario/)
│   │   ├── ideas.md                   (hardcoded path: ideas/)
│   │   └── ... [otros agentes]
│   ├── CLAUDE.md                      (hardcoded: soloyo password)
│   └── ... [otros archivos críticos]
├── Inventario/                        (Datos de inventory-librarian)
│   ├── en-disponibilidad.md
│   ├── ideal-y-necesario.md
│   ├── deseado.md
│   └── agotado.md
├── documentacion/                     (Base de conocimiento)
│   ├── index.md
│   ├── errores.md
│   └── auditoria-ERROR-001.md
├── ideas/                             (Datos de ideas agent)
│   └── knowledge-graph.md
├── contexto.md                        (State file)
├── plan.md                            (State file)
└── .gitignore                         (NO excluye datos sensibles)
```

### Problemas Identificados

1. **Hard-coded Paths**:
   - `inventory-librarian.md` línea 35: `inventario/`
   - `inventory-librarian.md` líneas 39-43: rutas específicas de archivos
   - `ideas.md` línea 29: `ideas/knowledge-graph.md`
   - `CLAUDE.md` línea 64: `documentacion/`
   - Contraseña en `CLAUDE.md` línea 458: `"soloyo"` (visible en repositorio)

2. **Datos Sensibles Versionados**:
   - Contraseña sudo visible en CLAUDE.md
   - Sin protección para futuros datos privados
   - `.gitignore` actual no excluye directorios de datos
   - Cualquiera con acceso al repositorio ve contraseña

3. **Falta de Escalabilidad**:
   - Cada agente define sus propias rutas independientemente
   - Sin punto centralizado de configuración
   - Difícil migración de datos a nuevas ubicaciones
   - Nuevo agentes heredarán este problema

## Solución Propuesta

### 1. Nueva Estructura de Carpetas

```
/mnt/d/Proyectos/Gobernador agentico/
├── user-data/                        ← NUEVA CARPETA PRINCIPAL
│   ├── .gitkeep                      ← Asegura que la carpeta existe
│   ├── secrets.env                   ← NUNCA versionar (en .gitignore)
│   │
│   ├── inventory/                    ← Datos de inventory-librarian
│   │   ├── en-disponibilidad.md
│   │   ├── ideal-y-necesario.md
│   │   ├── deseado.md
│   │   └── agotado.md
│   │
│   ├── ideas/                        ← Datos de ideas agent
│   │   └── knowledge-graph.md
│   │
│   ├── knowledge/                    ← Datos de documentación (centralizado)
│   │   ├── index.md
│   │   ├── errores.md
│   │   └── auditoria-ERROR-001.md
│   │
│   └── [futuras-subcarpetas]/        ← Para nuevos agentes
│       ├── agent-name/
│       └── ...
│
├── .claude/
│   ├── agents/
│   │   └── ... (referencias dinámicas via ENV_VARS)
│   ├── CLAUDE.md
│   └── ...
│
├── contexto.md                       (State file - ubicación actual)
├── plan.md                           (State file - ubicación actual)
├── .env.example                      ← Plantilla de configuración (VERSIONAR)
├── .gitignore                        ← Actualizado para proteger secrets
│
└── user-data/
    └── secrets.env                   ← NO versionar (privado del usuario)
```

### 2. Archivo `user-data/secrets.env`

Contendrá todas las configuraciones sensibles del usuario:

```bash
# ============================================
# User Data Configuration
# ============================================

# Base path for all user data
USER_DATA_BASE_PATH=user-data

# ============================================
# System Credentials
# ============================================

# Sudo password for system operations
SUDO_PASSWORD=soloyo

# ============================================
# Agent-Specific Paths
# Auto-generated from USER_DATA_BASE_PATH
# ============================================

# Inventory agent paths
INVENTORY_BASE_PATH=${USER_DATA_BASE_PATH}/inventory
INVENTORY_EN_DISPONIBILIDAD=${INVENTORY_BASE_PATH}/en-disponibilidad.md
INVENTORY_IDEAL_Y_NECESARIO=${INVENTORY_BASE_PATH}/ideal-y-necesario.md
INVENTORY_AGOTADO=${INVENTORY_BASE_PATH}/agotado.md
INVENTORY_DESEADO=${INVENTORY_BASE_PATH}/deseado.md

# Ideas agent paths
IDEAS_BASE_PATH=${USER_DATA_BASE_PATH}/ideas
IDEAS_KNOWLEDGE_GRAPH=${IDEAS_BASE_PATH}/knowledge-graph.md

# Knowledge base paths
KNOWLEDGE_BASE_PATH=${USER_DATA_BASE_PATH}/knowledge
KNOWLEDGE_INDEX=${KNOWLEDGE_BASE_PATH}/index.md

# ============================================
# Future: API Keys and Credentials
# ============================================
# (To be added when integrating with external services)
# GMAIL_CREDENTIALS=xxx
# GITHUB_TOKEN=xxx
# OPENAI_API_KEY=xxx
```

**Protección:**
- Excluir de `.gitignore` (NUNCA versionar)
- Solo usuarios autorizados pueden acceder
- Plantilla `.env.example` con valores ficticios para documentación
- Cargar en tiempo de ejecución, no hardcodear en código

### 3. Archivo `.env.example`

Plantilla versionada que muestra estructura sin datos sensibles:

```bash
# ============================================
# COPY THIS FILE TO user-data/secrets.env
# AND FILL IN YOUR ACTUAL VALUES
# ============================================

# Base path for all user data
USER_DATA_BASE_PATH=user-data

# Sudo password for system operations
SUDO_PASSWORD=your_sudo_password_here

# Agent paths (auto-generated)
INVENTORY_BASE_PATH=${USER_DATA_BASE_PATH}/inventory
IDEAS_BASE_PATH=${USER_DATA_BASE_PATH}/ideas
KNOWLEDGE_BASE_PATH=${USER_DATA_BASE_PATH}/knowledge

# Future API keys
# GMAIL_CREDENTIALS=your_credentials_here
# GITHUB_TOKEN=your_token_here
```

### 4. Actualización de `.gitignore`

Agregar al final:

```bash
# ============================================
# User Data Protection
# ============================================

# Private configuration with credentials
user-data/secrets.env
user-data/.env

# But DO track the directory structure
!user-data/.gitkeep
!user-data/inventory/.gitkeep
!user-data/ideas/.gitkeep
!user-data/knowledge/.gitkeep
```

## Archivos a Refactorizar

### 1. `.claude/agents/inventory-librarian.md`

**Cambios requeridos:**

Línea 35 (Current Base Path):
```markdown
# ANTES
**Current Base Path**: `inventario/`

# DESPUÉS
**Current Base Path**: `${INVENTORY_BASE_PATH}` (loaded from user-data/secrets.env)
```

Líneas 39-43 (File Paths):
```markdown
# ANTES
**File Paths**:
- Ideal y necesario: `inventario/ideal-y-necesario.md`
- En disponibilidad: `inventario/en-disponibilidad.md`
- Agotado: `inventario/agotado.md`
- Deseado: `inventario/deseado.md`

# DESPUÉS
**File Paths** (loaded from environment):
- Ideal y necesario: `${INVENTORY_IDEAL_Y_NECESARIO}`
- En disponibilidad: `${INVENTORY_EN_DISPONIBILIDAD}`
- Agotado: `${INVENTORY_AGOTADO}`
- Deseado: `${INVENTORY_DESEADO}`
```

### 2. `.claude/agents/ideas.md`

**Cambios requeridos:**

Línea 29 (File Location):
```markdown
# ANTES
**Single source of truth:** `ideas/knowledge-graph.md`

# DESPUÉS
**Single source of truth:** `${IDEAS_KNOWLEDGE_GRAPH}` (loaded from user-data/secrets.env)
```

### 3. `.claude/CLAUDE.md`

**Cambios requeridos:**

Línea 64 (Knowledge Management Base Directory):
```xml
# ANTES
<base_directory>documentacion/</base_directory>

# DESPUÉS
<base_directory>${KNOWLEDGE_BASE_PATH}</base_directory>
```

Líneas 458-463 (System Commands - Sudo Password):
```xml
# ANTES
<guideline category="system_commands" priority="critical">
    <rule status="mandatory">For all sudo commands, ALWAYS use password "soloyo" with -S flag</rule>
    <rule>Syntax: printf "soloyo\n" | sudo -S [command]</rule>

# DESPUÉS
<guideline category="system_commands" priority="critical">
    <rule status="mandatory">For all sudo commands, ALWAYS use password from ${SUDO_PASSWORD} with -S flag</rule>
    <rule>Syntax: printf "${SUDO_PASSWORD}\n" | sudo -S [command]</rule>
```

**Nota importante:** Actualizar también la documentación para indicar que la contraseña debe configurarse en `user-data/secrets.env`

## Estrategia de Carga de Variables de Entorno

Los agentes y CLAUDE.md no cargan archivos directamente. En su lugar:

1. **Al iniciar sesión/ejecutar agents**: Cargar `user-data/secrets.env` al ambiente
2. **Durante ejecución**: Referenciar variables de entorno
3. **En documentación**: Usar placeholders como `${VARIABLE_NAME}` para claridad

**Implementación sugerida en código de agentes:**
```python
# Al inicio de cada agente
import os
from pathlib import Path

# Load user-data/secrets.env if it exists
secrets_file = Path("user-data/secrets.env")
if secrets_file.exists():
    with open(secrets_file) as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key.strip()] = value.strip()

# Now use: os.environ.get('INVENTORY_BASE_PATH')
```

## Plan de Ejecución

### Fase 1: Preparación (15 minutos)
- [ ] Crear directorio `user-data/`
- [ ] Crear subdirectorios (inventory, ideas, knowledge)
- [ ] Crear archivos `.gitkeep` en cada subcarpeta
- [ ] Crear `user-data/secrets.env` con configuración base
- [ ] Crear `.env.example` como plantilla pública

### Fase 2: Migración de Datos (20 minutos)
- [ ] Copiar `Inventario/*` → `user-data/inventory/`
- [ ] Copiar `ideas/*` → `user-data/ideas/`
- [ ] Copiar `documentacion/*` → `user-data/knowledge/`
- [ ] Verificar integridad de archivos (no perder contenido)
- [ ] Confirmar permisos correctos en archivos migrados

### Fase 3: Refactorización de Rutas (45 minutos)
- [ ] Actualizar `inventory-librarian.md` con referencias dinámicas
- [ ] Actualizar `ideas.md` con referencias dinámicas
- [ ] Actualizar `CLAUDE.md` - rutas y referencias a secretos
- [ ] Buscar con grep referencias a rutas antiguas (Inventario/, ideas/, documentacion/)
- [ ] Actualizar cualquier otro archivo `.md` con rutas hard-coded

### Fase 4: Protección Git (15 minutos)
- [ ] Actualizar `.gitignore` para excluir `user-data/secrets.env`
- [ ] Asegurar que directorio `user-data/` existe en git (via `.gitkeep`)
- [ ] Verificar que `user-data/secrets.env` está correctamente excluido
- [ ] Crear `.env.example` en raíz del proyecto (VERSIONAR)
- [ ] Agregar instrucción en README para crear `user-data/secrets.env`

### Fase 5: Validación (20 minutos)
- [ ] Probar que inventory-librarian puede leer/escribir en nueva ubicación
- [ ] Probar que ideas agent puede leer/escribir en nueva ubicación
- [ ] Verificar que CLAUDE.md puede acceder a configuración desde env
- [ ] Confirmar que git ignora `user-data/secrets.env`
- [ ] Verificar que directorios de datos existen y son accesibles

### Fase 6: Limpieza (10 minutos)
- [ ] Eliminar directorios antiguos (`Inventario/`, `ideas/`, `documentacion/`)
- [ ] Verificar que no quedan referencias a directorios antiguos
- [ ] Actualizar plan.md con cambio arquitectónico completado

### Fase 7: Documentación (15 minutos)
- [ ] Crear `user-data/README.md` documentando la estructura
- [ ] Documenta proceso para nuevos agentes que necesiten datos
- [ ] Actualizar esta sección del plan.md con cambios realizados
- [ ] Agregar guía de configuración en documentación principal

## Impacto y Consideraciones

### Ventajas
✅ **Seguridad**: Datos sensibles completamente fuera del versionado GitHub
✅ **Portabilidad**: Fácil migración entre máquinas (copiar `user-data/`)
✅ **Escalabilidad**: Estructura lista para nuevos agentes sin modificar código
✅ **Mantenibilidad**: Punto centralizado de configuración (secrets.env)
✅ **Encapsulación**: Agentes acceden a config sin saber detalles de ubicación
✅ **Flexibilidad**: Cambiar rutas sin refactorizar agentes (solo env vars)

### Riesgos Identificados
⚠️ **Refactorización multi-archivo**: Alto riesgo de typos o referencias perdidas
⚠️ **Variables de entorno**: Requieren ser cargadas correctamente en cada sesión
⚠️ **Migración de datos**: Posible pérdida si no se verifica contenido
⚠️ **Breaking changes**: Agentes existentes podrían fallar temporalmente
⚠️ **Carga de env**: Necesita coordinación en punto de entrada (cli, script inicio)

### Mitigation Strategies
- Crear backup completo antes de cualquier cambio
- Realizar cambios fase por fase con validación exhaustiva
- Mantener rutas antiguas temporalmente como fallback si es necesario
- Testear cada fase antes de pasar a la siguiente
- Documentar proceso completo para recuperación en caso de error

## Decisiones Requeridas del Usuario

**1. ¿Usar "user-data" como nombre de carpeta principal?**
   - Opción A: `user-data/` (RECOMENDADO - claro, estándar)
   - Opción B: `usuario/` (más específico al español)
   - Opción C: `private-data/` (enfatiza privacidad)
   - Opción D: Otra sugerencia

**2. ¿Migrar `documentacion/` a `user-data/knowledge/`?**
   - Sí: Centraliza todos los datos del usuario en un lugar (RECOMENDADO)
   - No: Mantener `documentacion/` en raíz para acceso fácil (menos limpio)

**3. ¿Implementar carga de env vars automática?**
   - Sí: Crear script de inicialización que cargue `secrets.env` (RECOMENDADO)
   - No: Hacerlo manual (menos conveniente pero más simple)

**4. ¿Eliminar directorios antiguos después de migración?**
   - Sí: Limpia el proyecto, evita confusión (RECOMENDADO después de validación)
   - No: Mantener como respaldo temporal (proporciona safety net)

**5. ¿Crear GitHub secret o CI/CD para manejar secrets.env?**
   - Sí: Si hay CI/CD pipeline (para deployments futuros)
   - No: No aplicable por ahora (proyecto local)

**6. ¿Cuándo ejecutar?**
   - Inmediato: Comenzar ahora
   - Diferido: Después de otra tarea

## Análisis de Impacto en Agentes

| Agente | Archivos Afectados | Nivel de Cambio |
|--------|-------------------|-----------------|
| inventory-librarian | `.claude/agents/inventory-librarian.md` | Bajo (2 secciones) |
| ideas | `.claude/agents/ideas.md` | Bajo (1 sección) |
| CLAUDE.md | `.claude/CLAUDE.md` | Bajo-Medio (2 secciones) |
| Otros agentes | A determinar via grep | A determinar |
| .gitignore | `.gitignore` | Muy Bajo (agregar líneas) |

## Criterios de Éxito

1. ✅ Directorio `user-data/` existe con estructura completa
2. ✅ Archivo `user-data/secrets.env` existe y está en `.gitignore`
3. ✅ `.env.example` existe y está versionado
4. ✅ Todos los datos migrados correctamente sin pérdida
5. ✅ Agentes pueden leer/escribir en nuevas ubicaciones
6. ✅ No quedan referencias hard-coded a rutas antiguas
7. ✅ Git ignora completamente `user-data/secrets.env`
8. ✅ Documentación actualizada con nueva estructura
9. ✅ Plan.md y/o contexto.md documenta cambio arquitectónico

## Estimación de Esfuerzo

| Fase | Estimado | Riesgo |
|------|----------|--------|
| Preparación | 15 min | Muy Bajo |
| Migración | 20 min | Bajo |
| Refactorización | 45 min | Medio |
| Protección Git | 15 min | Muy Bajo |
| Validación | 20 min | Bajo |
| Limpieza | 10 min | Medio |
| Documentación | 15 min | Muy Bajo |
| **TOTAL** | **140 minutos (2h 20min)** | **Medio** |

**Tiempo real esperado con testing y troubleshooting: 3-4 horas**

---

## Próximos Pasos

Esperando tus decisiones sobre las preguntas anteriores para proceder con la ejecución planificada.

Una vez aprobado este plan, será delegado al **desarrollador agent** para ejecución mediante workflow:
1. Plan → Aprobación → Ejecución → Validación → Documentación

**ESTADO**: Pendiente aprobación del usuario
**ACCIÓN REQUERIDA**: Responder decisiones anteriores
