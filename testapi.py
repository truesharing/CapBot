import requests
import time

start = time.time()
url = "https://secure.runescape.com/m=adventurers-log/rssfeed?searchName=Catman"
for i in range(50):
    response = requests.get(url)
    print(response.status_code)
print(f"Took {time.time() - start} seconds. {(time.time() - start) / 50}s/request")