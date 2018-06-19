import json
import urllib
import requests
import os
import sys
import time

from pprint import pprint
from os.path import expanduser

subscription_key = '5f96f61c9b1242c995ea525521c5ae02'

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
        faces = response.json()
        
        for face in faces:
            fr = face["faceAttributes"]["emotion"]
            happiness = fr["happiness"]
            disgust = fr["disgust"]
            fear = fr["fear"]
            anger = fr["anger"]
            surprise = fr["surprise"]
            neutral = fr["neutral"]
            sadness = fr["sadness"]
            contempt = fr["contempt"]
            
            
        
        if response.status_code != 200:
            raise ValueError(
                'Request to Azure returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )
        time.sleep(10)
        os.remove(imagepath)
except KeyboardInterrupt:
    print("Finished!")
