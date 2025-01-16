import shutil
from datetime import datetime

# Byt ut mot giltig sökväg
source = "C:/Users/rudbe/Documents/GitHub/upf-automation/source"
destination = "C:/Users/rudbe/Documents/GitHub/upf-automation/backups/backup"

def backup_files():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    target = f"{destination}_{timestamp}"
    shutil.copytree(source, target, dirs_exist_ok=True)
    print("Backup done!!")

if __name__ == "__main__":
    backup_files()