# -*- coding: utf-8 -*-
"""
Main execution loop for the Gobernador Agentico project.
"""
import sys
import re
import os
from src.model_dispatcher import invoke_agent

def check_initial_setup():
    """
    Acts on behalf of the Orchestrator to check for essential configurations.
    If the .env file is missing, it invokes the Setup Assistant's guidance.
    """
    if not os.path.exists('.env'):
        print("\033[93m" + "="*60 + "\033[0m")
        print("\033[93m" + "  [Orquestador] -> Invocando al Asistente de Configuración" + "\033[0m")
        print("\033[93m" + "="*60 + "\033[0m")
        print("\n¡Bienvenido! Parece que es tu primera vez ejecutando este proyecto.")
        print("El archivo de configuración '.env' no ha sido encontrado.\n")
        print("Por favor, ejecuta el script de configuración para empezar:")
        print("\n    \033[1mpython scripts/setup.py\033[0m\n")
        print("El asistente te guiará para crear el entorno, instalar dependencias")
        print("y generar el archivo '.env' que necesitas llenar con tus API keys.")
        print("\033[93m" + "="*60 + "\033[0m")
        sys.exit(0) # Exit gracefully without an error.

def parse_delegation(response: str):
    """
    Parses the response to find a delegation command.
    A delegation command is expected in the format:
    [DELEGATE: agent_name, PROMPT: "The prompt for the agent..."]
    """
    match = re.search(
        r'\\[DE-?LEGATE:\s*([\w-]+),\s*PROMPT:\s*"(.*?)\"\\]',
        response,
        re.DOTALL | re.IGNORECASE
    )
    if match:
        agent_name = match.group(1).strip()
        prompt = match.group(2).strip()
        return agent_name, prompt
    return None, None

def main():
    """
    Main chat loop.
    """
    # The Orchestrator's first action is to check the setup.
    check_initial_setup()

    print("--- Gobernador Agentico ---")
    print("Sistema de agentes multi-modelo iniciado. Escribe 'salir' para terminar.")
    print("="*30)

    coordinator_agent_name = "default_coordinator"

    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("Finalizando sesión. ¡Hasta luego!")
                break

            if not user_input:
                continue

            agent_call_log = []

            print(f"\n[Gobernador] -> Invocando al coordinador ('{coordinator_agent_name}')...")
            coordinator_response = invoke_agent(
                coordinator_agent_name,
                user_input,
                call_history=agent_call_log
            )

            agent_to_delegate, prompt_for_agent = parse_delegation(coordinator_response)

            final_response = ""
            if agent_to_delegate:
                print(f"[Gobernador] -> Delegando tarea al agente '{agent_to_delegate}'...")
                try:
                    final_response = invoke_agent(
                        agent_to_delegate,
                        prompt_for_agent,
                        call_history=agent_call_log
                    )
                except Exception as e:
                    final_response = f"❌ Error al invocar al agente '{agent_to_delegate}': {e}"
            else:
                final_response = coordinator_response

            if agent_call_log:
                route_summary = " -> ".join([call['name'] for call in agent_call_log])
                print(f"\n[Ruta de Agentes: {route_summary}]")

            print(f"\nRespuesta:\n{final_response}")
            print("="*30)

        except (ValueError, NotImplementedError, RuntimeError) as e:
            print(f"\n❌ Ocurrió un error en el flujo principal: {e}", file=sys.stderr)
        except KeyboardInterrupt:
            print("\n\nFinalizando sesión por interrupción del usuario. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Ocurrió un error inesperado: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()