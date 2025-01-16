import requests
from bs4 import BeautifulSoup

response = requests.get("https://docs.python.org/3/")

soup = BeautifulSoup(response.text, "html.parser")
footers = soup.find_all("div", class_="footer")

for footer in footers:  
    footer_part = footer.text.split("Copyright")[1].strip()
    print(footer_part.split("2001-")[1].split(",")[0])


# Bygga script: 30 min
# Kolla manuellt: 1 min
# Behov: Kontrollera varje år

# Bygga script: 1 tim
# Uppdatera manuellt: 30 min
# Behov: Uppdatera varje dag