# Documentación - Índice General

**Propósito:** Índice centralizado de toda la documentación del proyecto.

**Última actualización:** 2025-10-21

---

## Documentos Disponibles

### Sistema y Operaciones

#### errores.md
**Descripción:** Base de conocimiento de errores resueltos, sus causas y soluciones.
**Mantenido por:** error-documenter agent
**Uso:** Consultar cuando se encuentre un error similar o documentar nuevos errores resueltos
**Cómo buscar:** Usar Grep con mensaje de error, síntomas o tags de dominio
**Última actualización:** 2025-10-21
**Errores documentados:** 2
- ERROR-001: Direct Read of Agent-Owned File Violating Encapsulation (High severity)
- ERROR-002: Triple Violation - Direct Git Execution + Incorrect Error Documentation (Critical severity)
**Patrones identificados:** 1 (Agent Encapsulation Violations - 2 occurrences)

#### auditoria-ERROR-001.md
**Descripción:** Reporte de auditoría completo sobre resolución de ERROR-001 (Agent Encapsulation Violation).
**Mantenido por:** desarrollador agent
**Uso:** Referencia para verificar que ERROR-001 está completamente resuelto y entender gaps menores identificados
**Contenido:** Análisis de documentación, cobertura de políticas, mecanismos de enforcement, gaps identificados, y 5 recomendaciones de mejora
**Fecha:** 2025-10-21
**Estado:** ERROR-001 RESUELTO SATISFACTORIAMENTE (riesgo de recurrencia: BAJO)
**Gaps encontrados:** 3 (todos BAJA severidad)
**Recomendaciones:** 5 (2 media prioridad, 3 baja prioridad)

---

## Cómo Usar Este Índice

1. **Buscar información:** Revisa este índice antes de crear nueva documentación
2. **Agregar documentos:** Al crear nuevo documento, agregar entrada aquí con descripción
3. **Mantener actualizado:** Actualizar "Última actualización" al modificar documentos referenciados

---

## Estructura de Documentación

```
user-data/knowledge/
├── index.md (este archivo)
├── errores.md (base de conocimiento de errores)
├── auditoria-ERROR-001.md (reporte de auditoría ERROR-001)
└── [otros documentos futuros]
```

**Nota Arquitectónica:** Esta carpeta fue migrada desde `documentacion/` a `user-data/knowledge/` el 2025-10-21 como parte de la refactorización de estructura de datos del usuario. Todas las referencias a rutas fueron actualizadas en agentes y archivos de configuración.

---

**Nota:** Este índice crece a medida que se agrega documentación al proyecto.
