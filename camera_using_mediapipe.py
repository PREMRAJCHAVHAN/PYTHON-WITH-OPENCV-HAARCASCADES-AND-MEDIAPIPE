import cv2
import mediapipe as mp

def prem():
    cap=cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh()
    if not cap.isOpened():
        print("camera is not open")
        return
    while True:
        ret,frame =cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor (frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)
        if results.multi_face_landmarks:
            for lm in results.multi_face_landmarks:
                for pt in lm.landmark:
                    h ,w,_=frame.shape
                    x, y = int(pt.x *w), int(pt.y *h)
                    cv2.circle(frame,(x, y), 2, (0,0,255),-1)
        cv2.imshow('camera',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    prem()
