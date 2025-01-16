import requests

def get_temperature():
    url = "https://api.open-meteo.com/v1/forecast"
    url += "?latitude=57.7814&longitude=14.1562&current=temperature_2m"

    print(url)
    response = requests.get(url)
    data = response.json()

    return data["current"]["temperature_2m"]


print(get_temperature())