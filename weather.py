import requests


citys = ['Лондон','Череповец','Шереметьево']

payload = {"lang":"ru","n":"","T":"","q":"","m":""}

url_template = 'http://wttr.in/{}'
for city in citys:
    url = url_template.format(city)

    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)


