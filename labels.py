import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')
print("Hello and Welcome to MLMatcher. ML Matcher uses Artificial Intellgience in order to idetify everything in any image")
print("Import all images into the image folder before running")
imgurl = input("Enter image before natural disaster")
imgbytes = image_helpers.get_image_from_url(imgurl)
recresp = client.detect_labels(Image={'Bytes': imgbytes})

#print("\n" + "Success MLMatcher found the follow from your image: ")
myList = []
for label in recresp['Labels']:
    myList.insert(0, label['Name'])
else:
    print(myList)

imgurl2 = input("Enter image after natural disaster")
imgbytes2 = image_helpers.get_image_from_url(imgurl2)
recresp2 = client.detect_labels(Image={'Bytes': imgbytes2})

#print("\n" + "Success MLMatcher found the follow from your image: ")
myList2 = []
for label in recresp2['Labels']:
    myList2.insert(0, label['Name'])
else:
    print(myList2)
length = len(myList)
for i in range(length - 1):
    if((myList[i]) != myList2[i]):
        print("After the disaster there was the loss of " + myList[i])

