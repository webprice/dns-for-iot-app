import pprint
import requests

#CHANGE TOKEN, EMAIL, APIKEY, DOMAIN,IPADDRESS TO YOUR DATA

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo1LCJleHAiOjE2NDI3MzQwMTV9.95qoHlW42DPoHXZnnvE2lkDjLUGFgC2_-wQZFfIULwM"
email = "valery3@gmail.com"
apikey = "s1UuaB2AFiz"
ipaddress = "3.3.3.3"
domain= "volodimirthegreat2.com"

pload = {"email":email,"apikey":apikey,"ipaddress":ipaddress,"domain":domain}
headers = {"Authorization": f"Bearer {token}"}
response = requests.post('http://136.244.82.142:8000/add', json=pload,headers = headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
