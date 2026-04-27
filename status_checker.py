from urllib.request import urlopen
from urllib.error import URLError

try:
    with open("urls.txt", "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()

        try:
            response = urlopen(url)
            print(f"{url} → {response.getcode()} OK")

        except URLError:
            print(f"{url} → Failed")

except FileNotFoundError:
    print("urls.txt file not found.")
