import re
from collections import defaultdict
from datetime import datetime, timedelta
from config import LOG_FILE, MAX_FAILED_ATTEMPTS, FAILED_LOGINS_PATTERNS, TIME_WINDOW_SECONDS

def log_auth_event(message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")

def detect_bruteforce_time_window():
    attempts = defaultdict(list)

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            for pattern in FAILED_LOGINS_PATTERNS:
                if re.search(pattern, line):
                    ts_match = re.search(
                        r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line
                    )
                    ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                    if ts_match and ip_match:
                        timestamp = datetime.strptime(
                            ts_match.group(1),
                            "%Y-%m-%d %H:%M:%S"
                        )
                        ip = ip_match.group(1)

                        attempts[ip].append(timestamp)
                    break

    alerts = {}

    for ip, times in attempts.items():
        times.sort()

        for i in range(len(times)):
            window = times[i:i + MAX_FAILED_ATTEMPTS]
            if len(window) >= MAX_FAILED_ATTEMPTS:
                if (window[-1] - window[0]).seconds <= TIME_WINDOW_SECONDS:
                    alerts[ip] = window
                    break

    return alerts

def detect_failed_logins_by_ip():
    attempts_by_ip = {}

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            for pattern in FAILED_LOGINS_PATTERNS:
                if re.search(pattern, line):
                    ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                    if ip_match:
                        ip = ip_match.group(1)

                        if ip not in attempts_by_ip:
                            attempts_by_ip[ip] = 1
                        else:
                            attempts_by_ip[ip] += 1
                    break

    return attempts_by_ip

if __name__ == "__main__":
    print("[GuardLog] Monitor iniciado")

    alerts = detect_bruteforce_time_window()

    for ip, times in alerts.items():
        print(f"ALERTA: Força bruta detectada")
        print(f"IP: {ip}")
        print(f"Tentativas: {len(times)}")
        print(f"Janela: {(times[-1] - times[0]).seconds} segundos")


