import random
import os
import base64
import sys
from imagekitio import ImageKit

PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')

imagekit = ImageKit(
    private_key='private_14HavAbKV7J1AvBUHKypUQ/4UjQ=',
    public_key='public_rXfGljrkT3jh84HCHQTs3c7eJDw=',
    url_endpoint='https://ik.imagekit.io/ShaiTestingPython')
img_list = []

list_files = imagekit.list_files({"path": "zoz"})
for i in range(0, len(list_files['response'])):
    img_list.append(list_files['response'][i]['url'])


