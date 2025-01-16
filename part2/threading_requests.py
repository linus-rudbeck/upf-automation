import threading
import requests
import time

def fetch_url(url):
    print(f"Getting {url}...")
    response = requests.get(url)
    print(f"Got {url} with status {response.status_code}")

urls = [
    "https://example.com/",
    "https://google.com/",
    "https://python.org/"
]

time.sleep(2)

print("Sequential... (one by one)")

for url in urls:
    fetch_url(url)



time.sleep(2)

print("Parallell... (all at once)")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()