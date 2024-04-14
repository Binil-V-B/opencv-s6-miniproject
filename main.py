import cv2
import cvzone
import pickle
import numpy as np

width = 105
height = 48

cap=cv2.VideoCapture("carPark.mp4") # use 1 for using the input from the irius camera

with open("car_positions",'rb') as f:
    posList=pickle.load(f)

def checkParkingSpaces():
    for pos in posList:
        x,y=pos


        imgCrop=img[y:y+height,x:x+width]
        cv2.imshow(str(x*y),imgCrop)

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success, img = cap.read()

    checkParkingSpaces()
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 0), 2)

    cv2.imshow("video",img)
    cv2.waitKey(10)