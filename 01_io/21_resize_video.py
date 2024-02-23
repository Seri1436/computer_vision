import os
import cv2
import time

# read video
video_path = os.path.join('.', 'data', 'ski.mp4')
video = cv2.VideoCapture(video_path)

# visualize video
print("visualize video...")
time_start = time.time()

frameWidth = 640
frameHeight = 360

print("if you want exit, press a 'q' key")
ret = True
while ret:
    ret, frame = video.read()

    frame = cv2.resize(frame, (frameWidth, frameHeight))

    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):  # if you want exit, press a 'q' key
            break

video.release()
cv2.destroyAllWindows()

time_end = time.time()
print(f"play time : {time_end - time_start}")