import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

if response.status_code == 200:
    results = response.json()
    usd = results['rates']['USD']
    print(usd)
    php = results['rates']['PHP']
    print(php)
else:
    print("Error occurred: ", response.status_code)