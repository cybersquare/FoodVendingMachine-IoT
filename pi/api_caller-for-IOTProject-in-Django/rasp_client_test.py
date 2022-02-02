
# importing the requests library
import requests
  
# api-endpoint
URL = "http://127.0.0.1:8000/test_call"
  
# location given here
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
print(r.status_code)
print(r.content)
  
  