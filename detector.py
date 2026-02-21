from checks.process_checker import check_processes
from checks.startup_checker import check_startup
from checks.file_activity_checker import check_files
from checks.usb_checker import check_usb

print(" Running Keylogger Detection Tool...\n")

alerts = []
alerts += check_processes()
alerts += check_startup()
alerts += check_files()
alerts += check_usb()

if alerts:
    print(" Potential threats detected:\n")
    for alert in alerts:
        print(" -", alert)
else:
    print(" No obvious keylogger activity detected")


print("\n Scan complete")
