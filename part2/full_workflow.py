import time

SLEEP_TIME = 1

def backup_files():
    print("Backing up files...")
    time.sleep(SLEEP_TIME)
    print("Backup done!")


def fetch_data():
    print("Fetching data...")
    time.sleep(SLEEP_TIME)
    print("Data fetched!")
    return False


def process_data(data):
    print("Processing data...")
    time.sleep(SLEEP_TIME)
    print("Data processed!")


def generate_report():
    print("Generating...")
    time.sleep(SLEEP_TIME)
    print("Generating!")


def send_email():
    print("Sending...")
    time.sleep(SLEEP_TIME)
    print("Sent!")



def full_workflow():
    backup_files()
    data = fetch_data()
    process_data(data)
    generate_report()
    send_email()


if __name__ == "__main__":
    full_workflow()