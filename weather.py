import requests

url = 'https://wttr.in/'
citys = ['Лондон', 'Шереметьево', 'Череповец']
for city in citys:
  full_url = f'{url}{city}?nTqu&lang=ru&M'
  response = requests.get(full_url)
  response.raise_for_status()
  print(response.text)