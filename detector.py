#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"Fast2sms API key","sender_id":"FSTSMS","message":"Suspicious Activty in your House.Please Check the Video Feed in the App.","language":"english","route":"p","numbers":"#mobile No to recieve"}

headers = {
    'cache-control': "no-cache"
}

faceDetect = cv2.CascadeClassifier(r'''/home/pi/Desktop/haarcascade_frontalface_default.xml''');//Add location of haarcascade_frontface_default
cam = cv2.VideoCapture(-1);
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("/home/pi/recognizer/trainingData.yml");
id = 0
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontsize = 1
fontcolor = (0,511,1)
count=0
c=0
while(True):
    ret,img = cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,180),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        print(conf);
        if(id==1 and conf<50):
               id="Swarn"
        elif(id==2 and conf<50):
            id="Nakul"
        else:
            id="Stranger"
            count=count+1
        

        if(count>30):
            if(c!=1):
                
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
                count=0
                c=1
                GPIO.setup(21,GPIO.OUT)
                GPIO.output(21,GPIO.HIGH)
                print("Alarm On")
                time.sleep(10)
                GPIO.output(21,GPIO.LOW)
                print("Led Off")
                time.sleep(10)
                
        cv2.putText(img,str(id),(x,y+h+25),fontface,fontsize,fontcolor,2);
        print(id)
    cv2.imshow("Face",img);

    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
