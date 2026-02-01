import requests
import json

url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'

from_country = input('From: ')
to_country = input('To: ')
amount = float(input('Amount: '))
found = 0

from_country.lower()
to_country.lower()

from_country_name = ''
to_country_name = ''

list_of_countries = requests.get(url).json()

for (key , value) in list_of_countries.items():
    if found == 2:
        break
    elif (from_country == key) and (to_country == key):
        found += 2
        from_country_name = value
        to_country_name = value
        break
    elif (from_country == key):
        found += 1
        from_country_name = value
        continue
    elif (to_country == key):
        found += 1
        to_country_name = value
        continue
    
if found != 2:
    exit('Error, couldnt match currency')
    
url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_country}.json'

exchange_rates = requests.get(url).json()

for (key , value) in exchange_rates[f'{from_country}'].items():
    if(to_country == key):
        print(f'{amount} {from_country_name} = {round((amount * float(value)),2)} {to_country_name}.')
        break
    