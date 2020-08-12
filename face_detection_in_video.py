import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 4)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'What a beautiful face ;)'
    frame = cv2.putText(frame, text, (10, 40), font, 0.9, (255, 0, 0), 2, cv2.LINE_AA)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (250, 0, 0), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

