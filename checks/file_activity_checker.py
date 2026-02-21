import os

SUSPICIOUS_FILES = ["keylog", "keystroke", "log"]

def check_files(search_path="."):
    alerts = []

    for root, _, files in os.walk(search_path):
        for file in files:
            if any(word in file.lower() for word in SUSPICIOUS_FILES):
                alerts.append(f"Suspicious file detected: {os.path.join(root, file)}")

    return alerts