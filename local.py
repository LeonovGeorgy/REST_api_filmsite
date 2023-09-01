import requests

# Получить инфо по фильму
#res = requests.get("http://127.0.0.1:5000/api/films/1")

# Получить инфо по сборам
#res = requests.get("http://127.0.0.1:5000/api/films/2")

# Получить инфо по актёрскому составу
#res = requests.get("http://127.0.0.1:5000/api/films/3")

# Добавляем инфо по сборам в России
#res = requests.post("http://127.0.0.1:5000/api/films/4", json={"country": "Rus", "fees_mill$": 1.3})

# Добавляем инфо по новому фильму
res = requests.post("http://127.0.0.1:5000/api/films/5", json={"film": "The Dark Knight", "duration_min": 152})
print(res.json())
