import pprint
import requests
token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo1LCJleHAiOjE2NDI3MzQ5Mjl9.SyiaAglQV-MkN6ktyi9AHctPY7LPQkL7FdBCPJtxjDo"

email = "valery3@gmail.com"
#apikey = "s1UuaB2AFiz"
password = "valerypasswd"
pload = {"email":email,"password":password}
headers = {"Authorization": f"Bearer {token}"}
response = requests.post('http://136.244.82.142:8000/forgot_apikey', json=pload, headers=headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
