import requests

URL = 'https://wttr.in/'

def get_weather(city):
  params = {'M':'',
            'nTqu': '',
            'lang': 'ru',
          }
  response = requests.get(f'{URL}{city}', params=params)
  response.raise_for_status()
  return(response.text)

def main():
  cities = ['Лондон', 'Шереметьево', 'Череповец']
  for city in cities: 
    print(get_weather(city))

if __name__ == '__main__':
  main()
