import requests


url = "https://tvn24.pl/"

print("Wysylamy zapytanie GET do:", url)

response = requests.get(url)

print("Otrzymaliśmy odpowiedź o statusie:", response.status_code)

if response.status_code == 200:
    # jesli status to 200 to mozemy zobaczyc co zwraca nam strona/api
    data = response.json()
    print("Zawartosc strony to:", data)
else:
    print("Nie udalo sie pobrac danych ze strony/api")
    