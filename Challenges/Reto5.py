import requests

request = requests.get('https://codember.dev/mecenas.json')
data = request.text

arr_mod = [pair for pair in enumerate(data.split(","))]


while len(arr_mod)>1:
    if len(arr_mod)%2==1:
        arr_mod = [pair[1] for pair in enumerate(arr_mod) if pair[0]%2==0]
        arr_mod.pop(0)
    elif len(arr_mod)%2==0:
        arr_mod = [pair[1] for pair in enumerate(arr_mod) if pair[0]%2==0]

print(arr_mod)