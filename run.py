#! /usr/bin/env python3

#Script to ulpload descriptions of fruits stored in local directory at a txt file
#and convert them to json to be posted using the requests module

import os
import requests

src = "/home/student-03-ec1bef4a57c1/supplier-data/descriptions/"
url = "http://34.136.29.87/fruits/"

#function to read txt file, convert to json, and post to url
def process_txt(txt_path):
  dict = {}
  with open(os.path.join(src,txt_path), 'r') as txt:
    img_name = txt_path.strip('.txt')
    img_name = img_name + '.jpeg'
    dict.update({"name":txt.readline().strip()})
    dict.update({"weight":int(txt.readline().strip(' lbs\n'))})
    dict.update({"description":txt.readline().strip()})
    dict.update({"image_name":img_name})
  response = requests.post(url,data=dict)
  response.raise_for_status()

for file in os.listdir(src):
  if not file.startswith('.'):
    process_txt(file)
