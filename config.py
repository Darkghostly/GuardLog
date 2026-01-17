LOG_FILE = "logs/auth.log"
MAX_FAILED_ATTEMPTS = 4

FAILED_LOGINS_PATTERNS = [
    r"Failed password for invalid user \S+ from \S+ port \d+",
    r"Failed password for \S+ from \S+ port \d+",
]