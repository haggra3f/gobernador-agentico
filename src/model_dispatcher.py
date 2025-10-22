# -*- coding: utf-8 -*-
"""
Model Dispatcher for the Multi-Model Agentic System.

This module is the core of the multi-model architecture. It is responsible for:
1.  Reading the agent configuration from `agent-config.json`.
2.  Loading API keys from environment variables (`user-data/secrets.env`).
3.  Providing a single function `invoke_agent` that takes an agent's name
    and a user prompt.
4.  Calling the appropriate LLM provider's API (Gemini, Anthropic, etc.) based
    on the configuration for that agent.
5.  Handling the specifics of each API's request and response format.
6.  Returning the model's response in a standardized format.
"""
import os
import json
import sys
from dotenv import load_dotenv
import google.generativeai as genai
import anthropic

# --- Constants and Configuration ---

# Add project root to the Python path to allow absolute imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Load environment variables from the secrets file
SECRETS_PATH = os.path.join(project_root, 'user-data', 'secrets.env')
if not os.path.exists(SECRETS_PATH):
    print(f"ERROR: Secrets file not found at {SECRETS_PATH}", file=sys.stderr)
    print("Please copy .env.example to user-data/secrets.env and fill in your API keys.", file=sys.stderr)
    sys.exit(1)
load_dotenv(SECRETS_PATH)

# Load agent configuration
CONFIG_PATH = os.path.join(project_root, 'agent-config.json')
if not os.path.exists(CONFIG_PATH):
    print(f"ERROR: Agent configuration not found at {CONFIG_PATH}", file=sys.stderr)
    sys.exit(1)
with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    AGENT_CONFIG = json.load(f)

# Configure API clients
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

if not ANTHROPIC_API_KEY:
    print("Warning: ANTHROPIC_API_KEY not found in environment.", file=sys.stderr)
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found in environment.", file=sys.stderr)

# --- API Specific Invocation Logic ---

def _invoke_gemini(model: str, system_prompt: str, user_prompt: str) -> str:
    """Invokes the Gemini API."""
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured.")
    try:
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name=model,
            generation_config=generation_config,
            system_instruction=system_prompt,
        )
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Gemini API call failed: {e}")

def _invoke_claude(model: str, system_prompt: str, user_prompt: str) -> str:
    """Invokes the Anthropic (Claude) API."""
    if not ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY is not configured.")
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = client.messages.create(
            model=model,
            max_tokens=4096,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        raise RuntimeError(f"Anthropic API call failed: {e}")


# --- Main Dispatcher Logic ---

def invoke_agent(agent_name: str, user_prompt: str, system_prompt: str = None, call_history: list = None) -> str:
    """
    Invokes the specified agent by calling the configured LLM provider.

    Args:
        agent_name: The name of the agent to invoke (e.g., 'orchestrator').
        user_prompt: The user's prompt or the message to send to the agent.
        system_prompt: The system prompt (instructions) for the agent. If None,
                       it's loaded from the agent's configured prompt_file.
        call_history: An optional list to which the agent call details will be appended.

    Returns:
        A string containing the response from the LLM.

    Raises:
        ValueError: If the agent is not found in the configuration.
        NotImplementedError: If the provider for the agent is not supported.
        RuntimeError: If the API call fails.
    """
    agent_info = next((agent for agent in AGENT_CONFIG['agents'] if agent['name'] == agent_name), None)

    if not agent_info:
        raise ValueError(f"Agent '{agent_name}' not found in agent-config.json")

    provider = agent_info.get('provider')
    model = agent_info.get('model')

    # Record the call if a history list is provided
    if call_history is not None:
        call_history.append({
            "name": agent_name,
            "provider": provider,
            "model": model
        })

    # Load system prompt from file if not provided
    if system_prompt is None:
        prompt_file_path = os.path.join(project_root, agent_info.get('prompt_file'))
        try:
            with open(prompt_file_path, 'r', encoding='utf-8') as f:
                system_prompt = f.read()
        except FileNotFoundError:
            raise ValueError(f"Prompt file not found for agent '{agent_name}' at {prompt_file_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to read prompt file for agent '{agent_name}': {e}")


    print(f"--- Invoking Agent ---")
    print(f"Name: {agent_name}")
    print(f"Provider: {provider}")
    print(f"Model: {model}")
    print(f"----------------------")


    if provider == 'gemini':
        return _invoke_gemini(model, system_prompt, user_prompt)
    elif provider == 'claude':
        return _invoke_claude(model, system_prompt, user_prompt)
    else:
        raise NotImplementedError(f"Provider '{provider}' is not currently supported.")

# --- Example Usage ---

if __name__ == '__main__':
    # This block allows for direct testing of the dispatcher.
    # Make sure to have your API keys in user-data/secrets.env
    print("--- Testing Model Dispatcher ---")
    
    # Check for API keys before running tests
    if not (GEMINI_API_KEY and ANTHROPIC_API_KEY):
        print("\nERROR: Both GEMINI_API_KEY and ANTHROPIC_API_KEY must be set in user-data/secrets.env to run tests.", file=sys.stderr)
        sys.exit(1)

    try:
        # Test Case 1: Invoke the orchestrator (Gemini)
        print("\n--- Test Case 1: Invoking Orchestrator (Gemini) ---")
        orchestrator_response = invoke_agent('orchestrator', 'The user wants to refactor the database module. Please provide a step-by-step plan.')
        print("\nOrchestrator Response:")
        print(orchestrator_response)

        # Test Case 2: Invoke the desarrollador (Claude)
        print("\n--- Test Case 2: Invoking Desarrollador (Claude) ---")
        desarrollador_response = invoke_agent('desarrollador', 'The user has approved the plan to refactor the database module. Please start with the first step: creating model backups.')
        print("\nDesarrollador Response:")
        print(desarrollador_response)

        # Test Case 3: Non-existent agent
        print("\n--- Test Case 3: Handling Non-Existent Agent ---")
        try:
            invoke_agent('non_existent_agent', 'This should fail.')
        except ValueError as e:
            print(f"Successfully caught expected error: {e}")

    except (ValueError, NotImplementedError, RuntimeError) as e:
        print(f"\nAn error occurred during testing: {e}", file=sys.stderr)
