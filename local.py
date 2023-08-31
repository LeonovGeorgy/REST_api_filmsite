import requests

res = requests.post("http://127.0.0.1:5000/api/films/3", json={"name": "Golang", "video": 5})
print(res.json())