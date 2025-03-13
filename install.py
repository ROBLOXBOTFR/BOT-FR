#!/usr/bin/env python3
"""
Script d'installation pour le bot de tickets Discord.
Ce script installe les dépendances nécessaires et crée un fichier .env.
"""

import os
import sys
import subprocess
import shutil

# Couleurs pour le terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_header():
    """Affiche l'en-tête du programme d'installation"""
    print(f"{BOLD}{GREEN}")
    print("===============================================")
    print("    INSTALLATION DU BOT DE TICKETS DISCORD    ")
    print("===============================================")
    print(f"{RESET}")

def check_python_version():
    """Vérifie la version de Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"{RED}[ERREUR] Python 3.8 ou supérieur est requis.{RESET}")
        print(f"Version actuelle: {version.major}.{version.minor}.{version.micro}")
        sys.exit(1)
    
    print(f"{GREEN}[OK] Version Python {version.major}.{version.minor}.{version.micro}{RESET}")

def install_dependencies():
    """Installe les dépendances requises"""
    print(f"{YELLOW}Installation des dépendances...{RESET}")
    
    requirements = [
        "discord.py>=2.0.0",
        "aiosqlite>=0.17.0",
        "python-dotenv>=0.19.0"
    ]
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        for req in requirements:
            print(f"Installation de {req}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", req])
        print(f"{GREEN}[OK] Dépendances installées avec succès{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}[ERREUR] Échec de l'installation des dépendances: {e}{RESET}")
        sys.exit(1)

def setup_env_file():
    """Configure le fichier .env"""
    if os.path.exists(".env"):
        print(f"{YELLOW}Un fichier .env existe déjà.{RESET}")
        overwrite = input("Voulez-vous le remplacer? (o/n): ").lower() == "o"
        if not overwrite:
            print(f"{YELLOW}Conservation du fichier .env existant.{RESET}")
            return
    
    print(f"{YELLOW}Configuration du fichier .env...{RESET}")
    token = input("Entrez votre token Discord (ou laissez vide pour le configurer plus tard): ")
    
    with open(".env", "w") as f:
        f.write("# Discord Bot Token - Ne partagez jamais ce token!\n")
        f.write(f"DISCORD_TOKEN={token}\n")
    
    print(f"{GREEN}[OK] Fichier .env créé avec succès{RESET}")

def final_instructions():
    """Affiche les instructions finales"""
    print(f"{GREEN}")
    print("===============================================")
    print("         INSTALLATION TERMINÉE!")
    print("===============================================")
    print(f"{RESET}")
    print(f"{BOLD}Comment démarrer le bot:{RESET}")
    print("1. Exécutez la commande: python main.py")
    print("2. Une fois le bot en ligne, utilisez la commande /setup dans Discord")
    print("3. Configurez le rôle staff avec /setstaff @role")
    print("\nBesoin d'aide supplémentaire? Consultez les fichiers:")
    print("- README.md          - Pour une vue d'ensemble")
    print("- GETTING_STARTED.md - Pour un guide de démarrage rapide")
    print("- COMMANDS.md        - Pour la liste complète des commandes")
    print("- EXAMPLES.md        - Pour des exemples pratiques")

def main():
    """Fonction principale du programme d'installation"""
    print_header()
    check_python_version()
    install_dependencies()
    setup_env_file()
    final_instructions()

if __name__ == "__main__":
    main()