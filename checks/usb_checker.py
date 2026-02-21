import psutil

def check_usb():
    alerts = []

    for part in psutil.disk_partitions():
        if 'removable' in part.opts.lower():
            alerts.append(f"Removable device detected: {part.device}")

    return alerts