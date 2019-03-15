#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:24:45 2018
@Copyrights Reserved #Apache 2.0
@author: vipul tushar pradyumna
"""
#Importing the Necessary Libraries
import os
import cv2
import numpy as np

#Python Image Loader Library
from PIL import Image 

#Local Binary Pattern Histogram Facial Recognizer
recognizer=cv2.face.LBPHFaceRecognizer_create();

#Path is set to the dataset created using dataset_creator.py program
path='dataset'

#Assigning the training labels to the images in dataset using Python Method
def getImagesWithID(path):
       imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
       print(imagePaths)
       faces=[]
       IDs=[]
       #Convert the images to grayscale for processing
       for imagePath in imagePaths:
           faceImg = Image.open(imagePath).convert('L');
           faceNp = np.array(faceImg,'uint8')
	   
           #Tokenization of the images splitted into pixels
           ID = int(os.path.split(imagePath)[-1].split('.')[1])
           faces.append(faceNp)
           IDs.append(ID)
           cv2.imshow("training",faceNp)
           cv2.waitKey(10)
       return IDs, faces

#Assigning the test labels to the data trained
IDs,faces = getImagesWithID(path)
recognizer.train(faces,np.array(IDs))

#Returns the trained data with labels as trainingData.yml file
recognizer.write('recognizer/trainingData.yml')
cv2.destroyAllWindows()
       
