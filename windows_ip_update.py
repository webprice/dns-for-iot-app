import pprint
import requests

#CHANGE TOKEN, EMAIL, APIKEY, DOMAIN,IPADDRESS TO YOUR DATA
#MAKE THIS SCRIPT AS A CRON JOB

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo1LCJleHAiOjE2NDI3MzQ5Mjl9.SyiaAglQV-MkN6ktyi9AHctPY7LPQkL7FdBCPJtxjDo"
email = "valery3@gmail.com"
apikey = "s1UuaB2AFiz"
domain = "volodimirthegreat.com"
ipaddress = "1.2.3.55"


pload = {"email":email,"apikey":apikey,"domain":domain,"ipaddress":ipaddress}
headers = {"Authorization": f"Bearer {token}"}
response = requests.post('http://136.244.82.142:8000/update', json=pload, headers=headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
