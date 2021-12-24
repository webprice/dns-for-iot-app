import pprint
import requests


#CHANGE TOKEN, EMAIL, APIKEY TO YOUR DATA

token= "your token here"
email = "name@gmail.com"
apikey = "your apikey here"

pload = {"email":email,"apikey":apikey}
headers = {"Authorization": f"Bearer {token}"}
response = requests.get('http://136.244.82.142:8000/check/', json=pload,headers = headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
