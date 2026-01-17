import re
from datetime import datetime
from config import LOG_FILE, MAX_FAILED_ATTEMPTS, FAILED_LOGINS_PATTERNS

def log_auth_event(message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")

def detect_failed_logins():
    failed_attempts = 0

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            for line in file:
                for pattern in FAILED_LOGINS_PATTERNS:
                    if re.search(pattern, line):
                        failed_attempts += 1
                        break
    except FileNotFoundError:
        print("[GuardLog] Arquivo de log não encontrado.")
        return

    if failed_attempts >= MAX_FAILED_ATTEMPTS:
        print(f"[ALERTA] {failed_attempts} tentativas de login falhadas detectadas.")

if __name__ == "__main__":
    print("[GuardLog] Monitor iniciado")
    detect_failed_logins()
