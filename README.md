# Gobernador Agentico

Bienvenido al proyecto Gobernador Agentico. Este es un sistema de agentes de IA diseñado para operar de manera autónoma y coordinada, utilizando un modelo de delegación de tareas.

## 🚀 Configuración Inicial

Para empezar a utilizar el proyecto, sigue estos sencillos pasos.

### 1. Ejecuta el Script de Configuración

Este proyecto incluye un script que automatiza la creación del entorno virtual, la instalación de dependencias y la configuración inicial de archivos.

Abre una terminal en la raíz del proyecto y ejecuta el siguiente comando:

```bash
python scripts/setup.py
```

El script te guiará a través del proceso.

### 2. Configura tus Credenciales

El script de configuración creará un archivo llamado `.env` en la raíz del proyecto. Ábrelo y añade tus claves de API y cualquier otra configuración personal que necesites.

```plaintext
# .env
GEMINI_API_KEY="TU_API_KEY_AQUI"
# Otras variables...
```

### 3. Configura el CLI de Gemini (¡Muy Importante!)

Para que el agente Gemini funcione como se espera, su CLI debe estar configurado para usar el "System Prompt" centralizado de este proyecto.

Las instrucciones detalladas sobre cómo hacer esto se encuentran en el archivo `GEMINI.md`. **No omitas este paso**, ya que es crucial para el comportamiento del agente.

### 4. Activa el Entorno Virtual

Una vez finalizada la configuración, recuerda activar el entorno virtual cada vez que vayas a trabajar en el proyecto:

**En Windows:**
```bash
source .venv/Scripts/activate
```

**En macOS/Linux:**
```bash
source .venv/bin/activate
```

¡Y eso es todo! Ya estás listo para empezar.
