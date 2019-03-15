#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:32:55 2018

@author: vipul tushar pradyumna
"""

import cv2
import numpy as np
faceDetect = cv2.CascadeClassifier(r'''/home/pi/Desktop/haarcascade_frontalface_default.xml''');
cam = cv2.VideoCapture(-1);

id=input('enter the user id');
sampleNum=0;
while(cv2.waitKey(1)!=27):
    ret,img = cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataset/User."+str(id)+"."+str(sampleNum)+".png",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>100):
        break;
cam.release()
cv2.destroyAllWindows()
