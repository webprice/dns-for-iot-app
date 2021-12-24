import pprint
import requests

#CHANGE TOKEN, EMAIL, APIKEY, DOMAIN,IPADDRESS TO YOUR DATA

token= "your token here"
email = "name@gmail.com"
apikey = "your apikey here"
ipaddress = "3.3.3.3" #your ip here
domain= "your domain here"

pload = {"email":email,"apikey":apikey,"ipaddress":ipaddress,"domain":domain}
headers = {"Authorization": f"Bearer {token}"}
response = requests.post('http://136.244.82.142:8000/add', json=pload,headers = headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
