import requests


citys = ['Лондон','Череповец','Шереметьево']

url_template = 'http://wttr.in/{}?nTqM&lang=ru'
for town in citys:
    url = url_template.format(town)

    response = requests.get(url)
    response.raise_for_status()
    print(response.text)