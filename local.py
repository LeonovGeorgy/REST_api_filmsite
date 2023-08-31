import requests

# Выполняя запрос ниже добовляем еще один фмльм
res = requests.post("http://127.0.0.1:5000/api/films/3", json={"film": "Terminator", "duration": 1.5})




print(res.json())
