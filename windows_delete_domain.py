import pprint
import requests
token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo1LCJleHAiOjE2NDI3MzQwMTV9.95qoHlW42DPoHXZnnvE2lkDjLUGFgC2_-wQZFfIULwM"

email = "valery3@gmail.com"
apikey = "s1UuaB2AFiz"
domain_removed = "volodimirthegreat2.com"
pload = {"email":email,"apikey":apikey,"domain_removed":domain_removed}
headers = {"Authorization": f"Bearer {token}"}
response = requests.delete('http://136.244.82.142:8000/delete/', json=pload,headers = headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
