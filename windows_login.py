import pprint
import requests

#change email and password to yours data
email = "valery3@gmail.com"
password = "valerypasswd"

pload = {"username":email,"password":password}
response = requests.post('http://136.244.82.142:8000/login', data=pload)
print ('Status:',response.status_code)
pprint.pprint(response.json())




