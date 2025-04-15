# -*- coding: utf-8 -*-
"""FaceDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vwBOre98UkuukqTxDbtJpckLp5n-ROwm
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

imgPath='celebs.jpg'
img=cv2.imread(imgPath)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.axis('off')
plt.imshow(gray,cmap='gray')
plt.show()

print(img)

faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces=faceCascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5, minSize=(30,30))
n=len(faces)
print("{0} faces are found!".format(n))

for (x,y,w,h) in faces:
  #Syntax:cv2.rectangle(image,start_point,end-point,color,thickness)
  cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0), 5)    #For BGR:(0,255,0)-green color
status=cv2.imwrite("faces_detected.jpg",img)
print("The status of the image stored:{0}".format(status))

imgPath2="faces_detected.jpg"
faces_detected=cv2.imread(imgPath2)
faces_detected=cv2.cvtColor(faces_detected,cv2.COLOR_BGR2RGB) #order of colors from BGR to RGB
plt.axis("off")
plt.imshow(faces_detected)