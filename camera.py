import cv2

def prem():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("camera is not open")
        return
    while True:
        ret,frame =cap.read()
        if not ret or cv2.waitKey(1) & 0xFF == ord("q"):
            break
        cv2.imshow('camera',frame)
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    prem()
