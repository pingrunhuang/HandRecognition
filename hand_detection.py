import cv2

class Hand():
    HUE_MIN = 0
    HUE_MAX = 20
    SATURATION_MIN = 75
    SATURATION_MAX = 190
    def __init__(self, mat):
        self.img = mat
        return

    def face_subtraction(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(self.img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            self.img[y:y+h, x:x+w] = (255,0,0)
        return self.img

    def hand_detection(self, isFaceSubtraction):
        if isFaceSubtraction:
            img_without_face = self.ace_subtraction()
            img_without_face = cv2.cvtColor(src=img_without_face, code=cv2.COLOR_BGR2HSV)
            
        else
            pass

        return
