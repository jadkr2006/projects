import os

def check_startup():
    alerts = []
    startup_path = os.getenv("APPDATA") + r"\Microsoft\Windows\Start Menu\Programs\Startup"

    if os.path.exists(startup_path):
        for file in os.listdir(startup_path):
            alerts.append(f"Startup item found: {file}")

    return alerts