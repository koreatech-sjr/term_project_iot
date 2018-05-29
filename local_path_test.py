import json
import urllib
import requests
import os
import sys

from pprint import pprint
from os.path import expanduser

subscription_key = 'f7261a9c39f44a15aa74fcd99969ea00'

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
})

url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?%s' % params


imagepath = "./face.jpg"
takePictureCommand = "raspistill -br 50 -t 1000 -o " + imagepath 


while True:
    os.system(takePictureCommand)  

    img = open(expanduser('./image.jpg'), 'rb')
    response = requests.post(url, data=img, headers=headers)
    pprint(response.json()[0])
    if response.status_code != 200:
        raise ValueError(
            'Request to Azure returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

    os.remove(imagepath)
