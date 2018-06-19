import requests

requestURL = 'http://192.168.0.6:3000'
body = {
    "happiness" : 0,
    "disgust" : 0,
    "fear" : 0,
    "anger" : 0,
    "surprise" : 0,
    "neutral" : 0,
    "sadness" : 0,
    "contempt" : 0
}

nodeRes = requests.post(requestURL, body)
print(nodeRes)
