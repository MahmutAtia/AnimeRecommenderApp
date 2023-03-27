import requests
url = "http://localhost:8000/login/"
res = requests.post(url, json={"username":"ran3","password":"123456"})
print(res.json())