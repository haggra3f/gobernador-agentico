# -*- coding: utf-8 -*-
"""
Main execution loop for the Gobernador Agentico project.

This script serves as the primary entry point for interacting with the multi-model
agentic system. It orchestrates the overall workflow:

1.  Initializes a chat session with a primary "coordinator" agent.
2.  Accepts user input in a continuous loop.
3.  Sends the user's request to the coordinator agent via the model_dispatcher.
4.  Parses the coordinator's response to detect delegation commands.
5.  If a delegation command (e.g., `[DELEGATE: agent_name]`) is found, it
    invokes the specified sub-agent with the provided context.
6.  Prints the final response to the user.
"""
import sys
import re
from src.model_dispatcher import invoke_agent

def parse_delegation(response: str):
    """
    Parses the response to find a delegation command.
    A delegation command is expected in the format:
    [DELEGATE: agent_name, PROMPT: "The prompt for the agent..."]
    """
    # A more robust regex to handle multi-line and complex prompts
    match = re.search(
        r'\\[DELEGATE:\s*(\\w+),\s*PROMPT:\s*"(.*?)"\\]',
        response,
        re.DOTALL
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
    print("--- Gobernador Agentico ---")
    print("Sistema de agentes multi-modelo iniciado. Escribe 'salir' para terminar.")
    print("="*30)

    # The 'default_coordinator' is the main agent that interprets user requests.
    # Its personality and rules are defined in .claude/CLAUDE.md.
    coordinator_agent_name = "default_coordinator"

    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("Finalizando sesión. ¡Hasta luego!")
                break

            if not user_input:
                continue

            # 1. Invoke the main coordinator agent
            print(f"\n[Gobernador] -> Invocando al coordinador ('{coordinator_agent_name}')...")
            coordinator_response = invoke_agent(coordinator_agent_name, user_input)

            # 2. Check for delegation
            agent_to_delegate, prompt_for_agent = parse_delegation(coordinator_response)

            final_response = ""
            if agent_to_delegate:
                print(f"[Gobernador] -> Delegando tarea al agente '{agent_to_delegate}'...")
                # 3. If delegation is detected, invoke the specified agent
                try:
                    final_response = invoke_agent(agent_to_delegate, prompt_for_agent)
                except Exception as e:
                    final_response = f"❌ Error al invocar al agente '{agent_to_delegate}': {e}"
            else:
                # If no delegation, the coordinator's response is the final one
                final_response = coordinator_response

            # 4. Print the final response
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
