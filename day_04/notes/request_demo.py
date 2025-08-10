import requests

site = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(site)

if response.status_code == 200:
    joke = response.json()
    print(joke['setup'])
    print(joke['punchline'])
else:
    print("Error: ", response.status_code)
