import psutil

SUSPICIOUS_KEYWORDS = ["keylog", "logger", "hook", "spy", "input"]

def check_processes():
    alerts = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name'].lower()
            if any(word in name for word in SUSPICIOUS_KEYWORDS):
                alerts.append(f"Suspicious process: {proc.info['name']} (PID {proc.info['pid']})")
        except:
            pass

    return alerts