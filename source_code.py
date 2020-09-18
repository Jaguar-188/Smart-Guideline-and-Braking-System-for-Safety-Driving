from tkinter import *
import threading
import RPi.GPIO as GPIO
#GPIO.setup(25,GPIO.OUT)
     

                   
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

from matplotlib import pyplot as plt

import pygame #for sound
pygame.init() #for sound

import signal
import sys
from time import sleep
import time

import cv2
in1 = 17#24
in2 = 23   #23
en = 25
temp1=1


GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)
x='f'



class Road:
    def __init__(self,root,):
            self.root=root
            self.root.geometry('900x600')
            self.root.config(bg='#505050')
            def dist():
                    import RPi.GPIO as GPIO
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setwarnings(False)
                    GPIO.setup(26,GPIO.OUT)
                    GPIO.setup(12,GPIO.OUT)
                    GPIO.setup(4,GPIO.OUT)
                    GPIO.setup(13,GPIO.OUT)

                                       
                    # set GPIO Pins
                    pinTrigger = 18
                    pinEcho = 24
                   
                    def forwards():
                            #print("forward")
                            GPIO.output(in1,GPIO.HIGH)
                            GPIO.output(in2,GPIO.LOW)
                 

                    def stop1():
                            GPIO.output(in1,GPIO.LOW)
                            GPIO.output(in2,GPIO.LOW)
                            print("in stop")
                        
                    fm1=Frame(self.root,bd=10,relief='raised',bg='#484848').place(x=150,y=10,width=600,height=200)
                    # set GPIO input and output channels
                    GPIO.setup(pinTrigger, GPIO.OUT)
                    GPIO.setup(pinEcho, GPIO.IN)
                    self.stop_status=0
                    while True:  
                        #forwards()
                        
                        GPIO.output(pinTrigger, True)
                        time.sleep(0.00000000000001)
                        GPIO.output(pinTrigger, False)
                        startTime = time.time()
                        stopTime = time.time()

                        while 0 == GPIO.input(pinEcho):
                            startTime = time.time()

                        while 1 == GPIO.input(pinEcho):
                            stopTime = time.time()

                        TimeElapsed = stopTime - startTime
                      
                        distance = (TimeElapsed * 34300) / 2

                        print ("Distance: %.1f cm" % distance)
                        s=str(distance)
                        s1=s[:5]+" cm"
                        
                        py=30
                        px=10
                        #fm1=Frame(self.root,bd=10,relief='raised',bg='#484848').place(x=150,y=10,width=300,height=200)
                        label_dist1=Label(fm1,text="Distance:",fg='black',font=('times new roman',20,'bold')).grid(row=2,column=2,padx=px,pady=py)
                        label_dist2=Label(fm1,text=s1,fg='black',font=('times new roman',20,'bold')).grid(row=2,column=3,padx=px,pady=py)
                        label_dist1=Label(fm1,text="Satus:",fg='black',font=('times new roman',20,'bold')).grid(row=3,column=2,padx=px,pady=py)
                        if distance<30:
                            label_dist2=Label(fm1,text="Danger",bg='red',fg='black',font=('times new roman',20,'bold')).grid(row=3,column=3,padx=px,pady=py)
                        if distance<100 and distance>30:
                            label_dist2=Label(fm1,text="Normal",fg='black',bg='yellow',font=('times new roman',20,'bold')).grid(row=3,column=3,padx=px,pady=py)
                        if distance>100:
                            label_dist2=Label(fm1,text="   Safe  ",fg='black',bg='green',font=('times new roman',20,'bold')).grid(row=3,column=3,padx=px,pady=py)

                        
                        if self.stop_status==1:
                            self.root.destroy()
                        if(distance<22):
                                
                                drum=pygame.mixer.Sound("/home/pi/Downloads/SlowDownPlease.wav")
                                print("slow down")
                                drum.play()
                                GPIO.output(26,GPIO.HIGH)
                                GPIO.output(12,GPIO.HIGH)
                                GPIO.output(4,GPIO.HIGH)
                                GPIO.output(13,GPIO.HIGH)
                                stop1()  
                        else:
                            
                                GPIO.output(26,GPIO.LOW)
                                GPIO.output(12,GPIO.LOW)
                                GPIO.output(4,GPIO.LOW)
                                GPIO.output(13,GPIO.LOW)
                                forwards()
                        #time.sleep(0.00001)
                        time.sleep(0.1)
                        
      
                
                
                
                
            def cam():
                fm11=Frame(self.root,bd=10,relief='raised',bg='#484848').place(x=150,y=210,width=600,height=200)
                vid_cam = cv2.VideoCapture(0)
                
                face_detector = cv2.CascadeClassifier('stop.xml')
                face_detector1 = cv2.CascadeClassifier('cascade_left.xml')
                face_detector2 = cv2.CascadeClassifier('cascade_SchoolAhed.xml')
                
                while(True):
                    _, image_frame = vid_cam.read()
                    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
                    
                    
                    faces = face_detector.detectMultiScale(gray, 1.3, 5)
                    faces1 = face_detector1.detectMultiScale(gray, 1.3, 5)
                    faces2 = face_detector2.detectMultiScale(gray, 1.3, 5)
                    
                    
                    print(type(faces))
                    print(faces)
                    
                    py=40
                    px=10
                        #fm1=Frame(self.root,bd=10,relief='raised',bg='#484848').place(x=150,y=10,width=300,height=200)
                    label_dist11=Label(fm11,text="Road Sign:",fg='black',font=('times new roman',20,'bold')).grid(row=4,column=2,padx=px,pady=py)
                    #label_dist2=Label(fm1,text=s1,fg='black',font=('times new roman',20,'bold')).grid(row=2,column=3,padx=px,pady=py)
                                        
                    if len(faces)!=0:
                        label_dist11=Label(fm11,text="Stop",fg='black',font=('times new roman',20,'bold')).grid(row=4,column=3,padx=px,pady=py)

                    else:
                        label_dist11=Label(fm11,text="       ",fg='black',font=('times new roman',20,'bold')).grid(row=4,column=3,padx=px,pady=py)
                    
                    if len(faces1)!=0:
                        label_dist11=Label(fm11,text="Left",fg='black',font=('times new roman',20,'bold')).grid(row=4,column=4,padx=px,pady=py)
                    else:
                         label_dist11=Label(fm11,text="      ",fg='black',font=('times new roman',20,'bold')).grid(row=4,column=4,padx=px,pady=py)

                         
                   
            def stop():
                self.stop_status=1
            def start():        
                t1=threading.Thread(target=dist)
                t1.start()
                t2=threading.Thread(target=cam)
                t2.start()          
                
            
            button_dist=Button(self.root,text="start",fg='black',bg='green', command=start)
            button_dist.grid(row=5,column=0,pady=200,padx=60)
            
            button_dist=Button(self.root,text="Stop",fg='black',bg='red', command=stop)
            button_dist.grid(row=5,column=1,pady=200,padx=10)
     
            
            
root=Tk()
wind=Road(root)
root.mainloop()
    