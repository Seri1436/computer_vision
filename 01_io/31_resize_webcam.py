import cv2

# read webcam
print("read webcam...")
webcam = cv2.VideoCapture(0)

frameWidth = 640
frameHeight = 480
webcam.set(3, frameWidth)
webcam.set(4, frameHeight)

# visualize webcam
print("visualize webcam...")

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # if you want exit, press a 'q' key
        break

webcam.release()
cv2.destroyAllWindows()