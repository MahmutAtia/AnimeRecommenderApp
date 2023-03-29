import requests
import getpass
url = "http://localhost:8000/animes/"
auth = "http://localhost:8000/login/"
# token =     "1a26bc81098d4e5a0fc267f134a95464b32512fb"


res = requests.post(auth, json={ "username":"mamo", "password":getpass.getpass()})
if res.status_code == 200:
    token = res.json().get("token")
    res2 = requests.get(url,headers={"Authorization":f"Token {token}"})
    print(res2.json())