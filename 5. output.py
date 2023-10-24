import cv2 
from keras.models import model_from_json
import numpy as np

json_file = open("trainedbatchf2.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)

model.load_weights("trainedbatchf2.h5")
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 256, 256, 1)
    return feature / 255.0

webcam = cv2.VideoCapture(0)
labels = {0: 'Drunk', 1: 'Sober'}
while True:
    ret, im = webcam.read()  # Capture a frame and check if it was successful
    if not ret:
        print("Failed to capture a frame from the webcam.")
        break  # Exit the loop if frame capture fails

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(im, 1.3, 5)

    try:
        for (p, q, r, s) in faces:
            image = gray[q:q+s, p:p+r]
            cv2.rectangle(im, (p, q), (p+r, q+s), (255, 0, 0), 2)
            image = cv2.resize(image, (256, 256))
            img = extract_features(image)
            pred = model.predict(img)
            prediction_label = labels[pred.argmax()]
            cv2.putText(im, '%s' % (prediction_label), (p - 10, q - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
        
        cv2.imshow("Output", im)
        if cv2.waitKey(27) == 27:  # Press 'Esc' to exit the loop
            break
    except cv2.error:
        pass

webcam.release()
cv2.destroyAllWindows()
