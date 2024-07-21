import cv2
import drivers
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

display=drivers.Lcd()
display.lcd_display_string('enter id: ',1)
Id=input('enter your id')
sampleNum=0
while(True): 
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
                sampleNum=sampleNum+1
                cv2.imwrite("dataset/User."+ str(Id)+"."+str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,132,216),2)
                cv2.waitKey(100) 
        cv2.imshow('Face',img)
        cv2.waitKey(1)
        display.lcd_display_string('registering face',1)
        display.lcd_display_string('please wait',2)
        if sampleNum>25:
                break

cam.release()
display.lcd_clear()
display.lcd_display_string('success',1)
display.lcd_display_string('face registered ',2)
cv2.destroyAllWindows()
