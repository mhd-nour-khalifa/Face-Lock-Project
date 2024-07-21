import cv2
import os
import numpy as np
from PIL import Image
# Path for face image database
path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def getImagesAndLabels(path):
#get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
#create empty face list
    faces=[]
#create empty ID list
    Ids=[]
#now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
#loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
#Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
#getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        print (Id)
        Ids.append(Id)
        cv2.imshow("training",imageNp)
        cv2.waitKey(10)
    return faces,Ids

faces,Ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('trainer.yml')
cv2.destroyAllWindows()