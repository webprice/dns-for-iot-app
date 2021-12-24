import pprint
import requests

#change email and password to yours data
email = "valeryboss@gmail.com"
password = "valerypasswd"


dictToSend = {'email':email,'password': password}

res = requests.post('http://136.244.82.142:8000/register', json=dictToSend)
print ('response from server:',res.status_code,":", res.text)
print("res,json",res.json())
pprint.pprint(res.json())
