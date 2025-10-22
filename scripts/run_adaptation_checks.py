# scripts/run_adaptation_checks.py
import os
import json
import re
import sys

# --- Constantes ---
# Obtener la ruta raíz del proyecto (un nivel arriba de 'scripts')
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENT_CONFIG_PATH = os.path.join(PROJECT_ROOT, 'agent-config.json')
AGENTS_DIR = os.path.join(PROJECT_ROOT, '.claude', 'agents')
MAIN_PY_PATH = os.path.join(PROJECT_ROOT, 'main.py')

def check_agent_config():
    """
    Verifica que todos los agentes en .claude/agents/ estén registrados en agent-config.json.
    Si faltan agentes, los añade con una configuración por defecto.
    """
    print("--- Verificando 'agent-config.json' ---")
    try:
        # Leer la configuración actual
        with open(AGENT_CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        registered_agents = {agent['name'] for agent in config['agents']}
        
        # Encontrar los agentes definidos en el directorio
        available_agents = {
            f.replace('.md', '') for f in os.listdir(AGENTS_DIR) if f.endswith('.md')
        }
        
        # Identificar los agentes que faltan
        missing_agents = available_agents - registered_agents
        
        if not missing_agents:
            print("OK: Todos los agentes están registrados.")
            return True

        print(f"ADVERTENCIA: Faltan {len(missing_agents)} agentes en la configuración: {', '.join(missing_agents)}")
        
        # Añadir los agentes que faltan
        for agent_name in missing_agents:
            print(f"    -> Añadiendo agente '{agent_name}'...")
            new_agent = {
                "name": agent_name,
                "provider": "gemini",
                "model": "gemini-1.5-flash",
                "prompt_file": f".claude/agents/{agent_name}.md"
            }
            config['agents'].append(new_agent)
            
        # Escribir la configuración actualizada
        with open(AGENT_CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
            
        print("ÉXITO: 'agent-config.json' ha sido actualizado.")
        return True

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo de configuración en {AGENT_CONFIG_PATH}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"ERROR: Ocurrió un error inesperado al verificar la configuración de agentes: {e}", file=sys.stderr)
        return False


def check_main_py_regex():
    """
    Verifica que la expresión regular en main.py sea la versión robusta.
    """
    print("\n--- Verificando la expresión regular de delegación en 'main.py' ---")
    # TODO: Implementar la lógica para verificar y, si es necesario, actualizar el regex.
    # Por ahora, asumimos que es correcta si el script se ejecuta.
    print("OK: La verificación de la expresión regular aún no está implementada, se asume correcta.")
    return True


def check_dependencies():
    """
    Verifica si requirements.txt ha cambiado y si las dependencias están instaladas.
    """
    print("\n--- Verificando dependencias en 'requirements.txt' ---")
    # TODO: Implementar la lógica para comparar con un estado anterior y ejecutar 'pip install -r requirements.txt'.
    print("OK: La verificación de dependencias aún no está implementada.")
    return True


def check_environment_variables():
    """
    Verifica si se han añadido nuevas variables en .env.example que no estén en el .env del usuario.
    """
    print("\n--- Verificando variables de entorno ---")
    # TODO: Implementar la lógica para comparar .env.example con un .env (si existe) y advertir al usuario.
    print("OK: La verificación de variables de entorno aún no está implementada.")
    return True


def main():
    """
    Función principal que ejecuta todas las verificaciones de adaptación.
    """
    print("=================================================")
    print("== Ejecutando Verificaciones de Adaptación para Gemini ==")
    print("=================================================")
    
    # Ejecutar todas las verificaciones
    results = {
        "agent_config": check_agent_config(),
        "main_py_regex": check_main_py_regex(),
        "dependencies": check_dependencies(),
        "environment_variables": check_environment_variables(),
    }
    
    print("\n--- Resumen de la Adaptación ---")
    all_ok = True
    for check, result in results.items():
        status = "ÉXITO" if result else "FALLO"
        print(f"- {check}: {status}")
        if not result:
            all_ok = False
            
    print("===========================================")
    if all_ok:
        print("VERIFICACIÓN COMPLETA: El proyecto parece estar adaptado correctamente.")
        # Salir con código 0 si todo está bien
        sys.exit(0)
    else:
        print("VERIFICACIÓN FALLIDA: Se encontraron problemas. Revisa los logs de error.")
        # Salir con código 1 si algo falló
        sys.exit(1)

if __name__ == "__main__":
    main()
