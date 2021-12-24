import pprint
import requests

#CHANGE TOKEN, EMAIL, APIKEY, DOMAIN,IPADDRESS TO YOUR DATA
#MAKE THIS SCRIPT AS A CRON JOB

token= "yourtokenhere"
email = "name@gmail.com"
apikey = "yourapikey"
domain = "yourdomain.com"
ipaddress = "your ip address here" #for example: "1.1.1.1"


pload = {"email":email,"apikey":apikey,"domain":domain,"ipaddress":ipaddress}
headers = {"Authorization": f"Bearer {token}"}
response = requests.post('http://136.244.82.142:8000/update', json=pload, headers=headers)
print ('Status:',response.status_code)
pprint.pprint(response.json())
