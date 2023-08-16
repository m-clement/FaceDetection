import cv2

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
# Replace 'test.jpg' with the path to your image
img = cv2.imread('test.jpg')

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with detected faces
cv2.imshow('img', img)
cv2.waitKey()

# Save the processed image
cv2.imwrite('face_detected.jpg', img)
