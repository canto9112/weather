import requests


citys = ['Лондон','Череповец','Шереметьево']

payload = {"nTqM&lang":"ru"}

url_template = 'http://wttr.in/{}'
for town in citys:
    url = url_template.format(town)

    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)


