import requests

mydata={"nama" : "andi"}

req = requests.post("http://127.0.0.1:5000/login",data=mydata)

print(req.text)