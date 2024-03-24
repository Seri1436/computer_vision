import cv2
import pafy

# read youtube
url = "https://www.youtube.com/watch?v=B5xckyNsWKw"
video = pafy.new(url)
best = video.getbest(preftype = 'mp4')     # 'webm','3gp'

capture = cv2.VideoCapture(best.url)
    
print("video title : {}".format(video.title))  # 제목
print("video rating : {}".format(video.rating))  # 평점
print("video viewcount : {}".format(video.viewcount))  # 조회수
print("video author : {}".format(video.author))  # 저작권자
print("video length : {}".format(video.length))  # 길이
print("video duration : {}".format(video.duration))  # 길이
print("video likes : {}".format(video.likes)) # 좋아요
print("video dislikes : {}".format(video.dislikes)) #싫어요
 
best = video.getbest(preftype='mp4')     # 'webm','3gp'
print("best resolution : {}".format(best.resolution))

cap = cv2.VideoCapture(best.url) 

# visualize video
print("visualize video...")
frameRate = 30

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(frameRate)    # frameRate msec동안 한 프레임을 보여준다
    if key == 27:                   # 키 입력을 받으면 키값을 key로 저장 -> esc == 27
        break
    
cap.release()
cv2.destroyAllWindows()

################################################################
# cv2.VideoCapture
# - 카메라에서 영상을 가져올 때
# - 동영상 파일을 읽어올 때
# - youtube에서 영상을 가져올 때
# - web에서 영상을 받아올 때

# cv2.VideoCapture.get(옵션)
# - 영상의 지정한 옵션 속성을 반환
################################################################
