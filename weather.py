import requests

url = 'https://wttr.in/'

def weather_in_city(city):
  params = {'M':'',
            'nTqu': '',
            'lang': 'ru',
          }
  response = requests.get(f'{url}{city}', params=params)
  response.raise_for_status()
  print(response.text)

def main():
  cities = ['Лондон', 'Шереметьево', 'Череповец']
  for city in cities:
    weather_in_city(city)

if __name__ == '__main__':
  main()
