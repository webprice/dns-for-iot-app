import pprint
import requests

#CHANGE TOKEN, EMAIL, APIKEY,DOMAIN_REMOED TO YOUR DATA
token= "your token here"
email = "name@gmail.com"
apikey = "your apikey here"

#DOMAIN YOU WANT TO REMOVE:
domain_removed = "your domain here"

pload = {"email":email,"apikey":apikey,"domain_removed":domain_removed}
headers = {"Authorization": f"Bearer {token}"}
response = requests.delete('http://136.244.82.142:8000/delete/', json=pload,headers = headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
