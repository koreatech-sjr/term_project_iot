import requests
from IPython.display import HTML
import requests
from io import BytesIO
from PIL import Image, ImageDraw


image_url = './image.jpg'
subscription_key = '06a63edf95824aeb91c168e77bdd9817'

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',   
    'returnFaceAttributes': 'emotion',
}


response = requests.post(face_api_url, params=params, headers=headers, json={"path": image_url})
faces = response.json()
HTML("<font size='5'>Detected <font color='blue'>%d</font> faces in the image</font>" % len(faces))

print(faces)

#Convert width height to a point in a rectangle


def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))


#Download the image from the url
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

#For each face returned use the face rectangle and draw a red box.
draw = ImageDraw.Draw(img)
for face in faces:
    draw.rectangle(getRectangle(face), outline='red')

#Display the image in the users default image browser.
img.show()


