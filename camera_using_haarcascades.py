import cv2

def prem():
    cap=cv2.VideoCapture(0)
    face_cascade =cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if not cap.isOpened():
        print("camera is not open")
        return
    while True:
        ret,frame =cap.read()
        if not ret:
            break
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for(x, y, w, h) in faces:
            cv2.rectangle(frame,(x, y),(x + w, y + h),(255, 0, 0),2)
        cv2.imshow('camera',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    prem()