import json
import urllib
import requests

from pprint import pprint
from os.path import expanduser

subscription_key = '06a63edf95824aeb91c168e77bdd9817'

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
})

url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?%s' % params

img = open(expanduser('./image.jpg'), 'rb')
response = requests.post(url, data=img, headers=headers)
pprint(response.json())
if response.status_code != 200:
    raise ValueError(
        'Request to Azure returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
