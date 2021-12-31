import json
import requests

url = 'https://sebastian2161-ejercicio21-rama-v12-3904709.dev.odoo.com/restfulapi/login1'
headers = {'Content-type': 'application/json'}
data = {'params': {'db': 'sebastian2161-ejercicio21-rama-v12-3904709', 'login': 'admin', 'password': 'admin'}}


r = requests.get(url, data=json.dumps(data), headers=headers)

print (r.url)
print(r)

if r.status_code == 200:
    payload = r.json()
    print(payload)