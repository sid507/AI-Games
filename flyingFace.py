import cv2
import random
import time
import math
import sys
import pygame
from pygame.locals import *

face_cascade = cv2.CascadeClassifier('FlyingFace/haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

def my_rand():
  numbers = list()
  numbers.append(random.randint(200,350))
  numbers.append(random.randint(400,500))
  return numbers[0]

def initialize():
    p=[[0,90,0,200,(200+100)]]
    return p

def addbars(p):
    if (p[0][0]>150):
        n=my_rand()
        pp=[0,90,0,n,(n+100)]
        p.insert(0,pp)
    return p

def delete(p):
    for i in range(len(p)-1,-1,-1):
        if p[i][0]>=640:
            p.pop(i)
        else:
            break


def drawrec(p,img,speed,b,g,r):
    for i in range(len(p)):
        p[i][0]=p[i][0]+speed
        p[i][1]=p[i][1]+speed
        # print(p[i][0])
        cv2.rectangle(img,(p[i][0]+20,p[i][2]),(p[i][1]-20,p[i][3]-20),(b,g,r),-1)

        cv2.rectangle(img,(p[i][0],p[i][3]-20),(p[i][1],p[i][3]),(0,0,0),-1)

        cv2.rectangle(img,(p[i][0],p[i][4]),(p[i][1],p[i][4]+20),(0,0,0),-1)
        cv2.rectangle(img,(p[i][0]+20,p[i][4]+20),(p[i][1]-20,640),(b,g,r),-1)
        score='Score'+str(speed-4)
        cv2.putText(img,score,(300,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2,cv2.LINE_AA)

    return img

def check(p,q):
    for i in range(len(p)):
        if q!=[] and q[0]>p[i][0] and q[1]<p[i][1]:
            # print('q1',q[0],q[1])
            if q[2]<p[i][3] or q[3]>p[i][4]:
                # print('q2',q[2],q[3])
                return False
    return True

p=initialize()
time_=0
speed=5
b=random.randint(0,255)
g=random.randint(0,255)
r=random.randint(0,255)
crash=False

cv2.waitKey(1000)
while True:
    _,img=cap.read()
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(imggray,1.3,5)
    q=[]
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = imggray[y:y+h, x:x+w]
        roi_color = img[y+int(0.2*y):y+h, x:x+w]
        cv2.rectangle(img,(x+w//2-10,y+h//2-10),(x+w//2+10,y+h//2+10),(0,255,0),-1)
        q=[x+w//2-10,x+w//2+10,y+h//2-10,y+h//2+10]
    while q==[]:
        
        
        _,img=cap.read()
        imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(imggray,1.3,5)

        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = imggray[y:y+h, x:x+w]
            roi_color = img[y+int(0.2*y):y+h, x:x+w]
            # nose=nosecas.detectMultiScale(roi_gray)
            # for (ex,ey,ew,eh) in nose:
            #     cv2.rectangle(roi_color,(ex,ey),(ex+int(ew*0.5),ey+int(eh*0.5)),(0,255,0),-1)
            cv2.rectangle(img,(x+w//2-10,y+h//2-10),(x+w//2+10,y+h//2+10),(0,255,0),-1)
            q=[x+w//2-10,x+w//2+10,y+h//2-10,y+h//2+10]    
            cv2.putText(img,'No Face Detected',(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,25,255),2,cv2.LINE_AA)
            cv2.imshow('Flying Face',img)
    if not check(p,q):
        crash=True
      
    addbars(p)
    time_=time_+1
    
    if time_%200==0:
        speed=speed+1
        b=random.randint(0,255)
        g=random.randint(0,255)
        r=random.randint(0,255)
    img=drawrec(p,img,speed,b,g,r)
    if crash==True:
        cv2.putText(img,'Game Over. Press W to exit',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('Flying Face',img)
        if cv2.waitKey(0) & 0xFF == ord('w'):
          cv2.destroyAllWindows()
        print('Game Over')
        break
        
    delete(p)
    cv2.imshow('Flying Face',img)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        cv2.destroyAllWindows()
        break
