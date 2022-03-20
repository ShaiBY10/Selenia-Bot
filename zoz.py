import random

from imagekitio import ImageKit
import os

PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')

imagekit = ImageKit(
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    url_endpoint='https://ik.imagekit.io/ShaiTestingPython')
img_list = []

list_files = imagekit.list_files({"path": "zoz"})
for i in range(0, len(list_files['response'])):
    img_list.append(list_files['response'][i]['url'])

pic = random.choice(img_list)
print(pic)
