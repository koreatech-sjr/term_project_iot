import json
import urllib
import requests
import os
import sys

from pprint import pprint
from os.path import expanduser

subscription_key = '55f316dfd7d649efacd9dfd91acaa123'

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
takePictureCommand = "raspistill -br 50 -t 3000 -o " + imagepath 

try:
    while True:
        os.system(takePictureCommand)  
        print("take a picture!")
        img = open(expanduser('./face.jpg'), 'rb')
        response = requests.post(url, data=img, headers=headers)
        pprint(response.json())
        if response.status_code != 200:
            raise ValueError(
                'Request to Azure returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )

        os.remove(imagepath)
except KeyboardInterrupt:
    print("Finished!")

