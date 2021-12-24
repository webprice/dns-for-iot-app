import pprint
import requests

#register
#device_ip = get('http://fra.rastem.com.ua/ip.php').text.format()
#print(device_ip)
#device_ip = "153.45.23.53"
email = "valeryboss@gmail.com"
password = "valerypasswd"
dictToSend = {'email':email,'password': password}

res = requests.post('http://136.244.82.142:8000/register', json=dictToSend)
print ('response from server:',res.status_code,":", res.text)
print("res,json",res.json())
pprint.pprint(res.json())
# print ('response from server:',res.text)
# dictFromServer = res.json()