#!/usr/bin/env python3

#script to upload all jpeg files from 'src' to the website 'url'
import requests
import os

url = "http://localhost/upload/"
src = "/home/student-03-ec1bef4a57c1/supplier-data/images"

for img in os.listdir(src):
  if img.endswith('.jpeg'):
    with open(os.path.join(src,img), 'rb') as opened:
      r = requests.post(url, files={'file': opened})
