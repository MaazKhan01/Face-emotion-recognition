import cv2
from deepface import DeepFace

facecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise IOError('Cannot Open webcam')
while True:
    ret,frame = cap.read()
    result = DeepFace.analyze(frame, actions = ['emotion'], enforce_detection=False)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecade.detectMultiScale(gray, 1.1,4)
    
    for(x, y, w,h) in faces: 
        cv2.rectangle(frame, (x,y),(x+w , y+h),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame,
           result['dominant_emotion'],
           (15,50),
           font,2,
           (255,0,0),
           3,
           cv2.LINE_4);
    cv2.imshow('Original Video',frame)
    
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()