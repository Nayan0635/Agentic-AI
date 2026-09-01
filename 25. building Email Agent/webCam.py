import cv2
from random import randint
#create a camera Object

camera = cv2.VideoCapture(0)
print("Press Enter or Space to Capture The Image")

 
while True:
 success,frame = camera.read()
 if not success:
        print("Error Opening WebCamera")
        exit(0)
   
 cv2.imshow("WebCam",frame)
 key = cv2.waitKey(1)

 if key == 13 or key==32:
     #Save The image
        filename = 'capture-'+str(randint(1000,9999))+".jpg"
        cv2.imwrite(filename,frame)
        print("Image Captured successfully")
        exit(0)