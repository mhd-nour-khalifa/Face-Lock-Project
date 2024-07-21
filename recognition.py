import cv2
import drivers
from time import sleep
import RPi.GPIO as gp
gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(18,gp.OUT)
recognizer=cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
cam = cv2.VideoCapture(0)
display=drivers.Lcd()
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
display.lcd_display_string("Door Locked",1)
    
def unlock(id):
     cv2.putText(im,str(id), (x,y+h),font,fontscale,fontcolor)
     display.lcd_clear()
     display.lcd_display_string('Door Unlocked',1)
     display.lcd_display_string('welcome '+str(id)+' :)',2)
     gp.output(18,1) #unlock the door
     sleep(5)
     gp.output(18,0)
     display.lcd_clear()
     
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(33,255,134),2)
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(conf)
    
    if(conf < 50):           
            if(id ==1):
                id= "hamza"
                unlock(id)
                break               
            if(id ==5):
                id="omar"
                unlock(id)
                break
            if(id ==2):
                id="david"
                unlock(id)
                break
            if(id==3):
             id="mustafa"
             unlock(id)
             break    
    else:                              
        id="unknown" 
        cv2.putText(im,str(id), (x,y+h),font,fontscale,fontcolor)       


    cv2.imshow('camera',im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()
display.lcd_display_string("Door Locked",1)

