# importing the requests library
import requests
  
# api-endpoint
# URL = "http://ijaz.pythonanywhere.com/check/"

URL = "http://127.0.0.1:8000/check/"
  
# location given here
fingerprint = open("creta.jpg", 'rb')

  
# defining a params dict for the parameters to be sent to the API
photo = open("hpy3.jpg", 'rb')

# sending get request and saving the response as response object
res = requests.post(url = URL, files={"photo":photo, "fingerprint":fingerprint})
print(res.content)

