

subscription_key = "06a63edf95824aeb91c168e77bdd9817"
assert subscription_key

face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

import requests

headers = {'Ocp-Apim-Subscription-Key': subscription_key }

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

image_data = {'url': './image.jpeg'}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": 'https://ggia.berkeley.edu/assets/general/GGIA-HumanFace.jpg'})
faces = response.json()

print(faces)
