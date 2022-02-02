# importing the requests library
import requests
  
# api-endpoint
URL = "http://127.0.0.1:8000/photo"
  
# location given here
photo = "09986544322245567543678989sskik"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'photo':photo}
  
# sending get request and saving the response as response object
r = requests.post(url = URL, params = PARAMS)