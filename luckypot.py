import requests
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "luckypot.log")
SECRETS_FILE = os.path.join(BASE_DIR, "secrets.py")

if not os.path.exists(SECRETS_FILE):
    print("❌ Fichier secrets.py manquant.")
    exit()

secrets = {}
with open(SECRETS_FILE) as f:
    exec(f.read(), secrets)

EMAIL = secrets.get("EMAIL")
PASSWORD = secrets.get("PASSWORD")

if not EMAIL or not PASSWORD:
    print("❌ EMAIL ou PASSWORD non défini dans secrets.py")
    exit()

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {message}\n")
    print(f"{timestamp} {message}")

def main():
    session = requests.Session()
    login = session.post("https://dashboard.honeygain.com/api/v1/users/tokens", json={
        "email": EMAIL,
        "password": PASSWORD
    })

    if login.status_code != 200:
        log(f"❌ Échec de connexion : {login.status_code}")
        return

    log("✅ Connexion réussie.")

    reward = session.post("https://dashboard.honeygain.com/api/v1/contest_winnings")
    if reward.status_code == 200:
        data = reward.json().get("data", {})
        credits = data.get("credits", 0)
        log(f"🍯 Pot ouvert : +{credits} crédits")
    elif reward.status_code == 409:
        log("⏱ Pot déjà ouvert aujourd’hui.")
    elif reward.status_code == 401:
        log("🔒 Non éligible ou token expiré.")
    else:
        log(f"❌ Erreur LuckyPot : {reward.status_code}")

if __name__ == "__main__":
    main()
