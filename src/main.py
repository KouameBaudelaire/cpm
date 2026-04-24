# src/main.py

from src.config import DATABASE_URL, SECRET_KEY, DEBUG

def afficher_config():
    print(f"Base de données : {DATABASE_KEY}")
    print(f"Debug activé : {DEBUG}")
