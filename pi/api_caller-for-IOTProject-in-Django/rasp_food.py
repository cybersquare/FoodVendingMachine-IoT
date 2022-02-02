
# importing the requests library
import requests
  
# api-endpoint
URL = "http://127.0.0.1:8000/food/"
  
# location given here
fp = "09986544322245567543678989"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'fingerprint':fp}
photo = open("billgates.jpg", 'rb')
  
# sending get request and saving the response as response object
r = requests.post(url = URL, 
                data = PARAMS, files={"photo":photo})
                # headers={'Content-Type': 'application/octet-stream'})
  
print(r.status_code)
print(r.content)