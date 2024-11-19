import requests # a lib for making http requests
import json # a lib for working with json

url = "https://flask-app-demo.onrender.com/predict?level=Junior&lang=Java&tweets=yes&phd=no"

response = requests.get(url=url)

# first thing, check the responses' status_code
print(response.status_code)
if response.status_code == 200:
    # status OK
    # we can extract the prediction from the responses JSON text
    json_object = json.loads(response.text)
    print(json_object)
    pred = json_object["prediction"]
    print("prediction: " , pred) 