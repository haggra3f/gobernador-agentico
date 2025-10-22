import os
import subprocess
import sys
import shutil

def print_color(text, color):
    """Prints text in a given color."""
    colors = {
        "header": "\033[95m",
        "blue": "\033[94m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "bold": "\033[1m",
        "underline": "\033[4m",
        "end": "\033[0m",
    }
    sys.stdout.write(colors.get(color, "") + text + colors["end"])
    sys.stdout.flush()

def main():
    """Main function to run the setup process."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)

    print_color("=====================================================\n", "header")
    print_color("  Bienvenido al Asistente de Configuración del Proyecto\n", "header")
    print_color("=====================================================\n\n", "header")

    # 1. Create and activate virtual environment
    print_color("Paso 1: Creando entorno virtual en '.venv'...
", "blue")
    try:
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print_color("=> Entorno virtual creado exitosamente.\n\n", "green")
    except subprocess.CalledProcessError as e:
        print_color(f="> Error al crear el entorno virtual: {e}\n", "red")
        sys.exit(1)

    # Determine activator script path
    if sys.platform == "win32":
        activator = os.path.join(".venv", "Scripts", "activate")
    else:
        activator = os.path.join(".venv", "bin", "activate")

    print_color(f"Paso 2: Instalando dependencias de 'requirements.txt'...
", "blue")
    try:
        if sys.platform == "win32":
            subprocess.run(f'"{activator}" && pip install -r requirements.txt', shell=True, check=True)
        else:
            subprocess.run(f'bash -c "source {activator} && pip install -r requirements.txt"', shell=True, check=True)
        print_color("=> Dependencias instaladas exitosamente.\n\n", "green")
    except subprocess.CalledProcessError as e:
        print_color(f="> Error al instalar las dependencias: {e}\n", "red")
        sys.exit(1)

    # 3. Create .env file
    print_color("Paso 3: Creando archivo de configuración '.env'...
", "blue")
    env_example_path = ".env.example"
    env_path = ".env"
    if not os.path.exists(env_path):
        try:
            shutil.copy(env_example_path, env_path)
            print_color(f="=> Se ha copiado '{env_example_path}' a '{env_path}'.\n", "green")
            print_color("   Por favor, edita este archivo y añade tus API keys y otras configuraciones.\n\n", "yellow")
        except FileNotFoundError:
            print_color(f="=> Error: No se encontró '{env_example_path}'. Creando un '.env' vacío.\n", "red")
            open(env_path, 'a').close()
    else:
        print_color("=> El archivo '.env' ya existe. No se ha modificado.\n\n", "yellow")

    # 4. Final Instructions
    print_color("=====================================================\n", "header")
    print_color("            ¡Configuración casi completada!\n", "header")
    print_color("=====================================================\n\n", "header")

    print_color("Acciones manuales requeridas:\n", "bold")
    print_color("1. ", "blue")
    print_color("Abre el archivo ", "yellow")
    print_color(".env", "bold")
    print_color(" y añade tus claves de API.\n", "yellow")

    print_color("2. ", "blue")
    print_color("Activa el entorno virtual antes de trabajar:\n", "yellow")
    if sys.platform == "win32":
        print_color(f"   En Windows: ", "green")
        print_color(f"source .venv/Scripts/activate\n\n", "bold")
    else:
        print_color(f"   En macOS/Linux: ", "green")
        print_color(f"source .venv/bin/activate\n\n", "bold")
        
    print_color("3. ", "blue")
    print_color("IMPORTANTE: Configura tu CLI de Gemini para usar el System Prompt de este proyecto.\n", "yellow")
    print_color("   Consulta las instrucciones en el archivo ", "yellow")
    print_color("GEMINI.md", "bold")
    print_color(" para saber cómo hacerlo.\n\n", "yellow")


if __name__ == "__main__":
    main()
