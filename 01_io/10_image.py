import os
import cv2

# read image
print("read image...")
image_path = os.path.join('.', 'data', 'bird1.png')
img = cv2.imread(image_path)

print(f"- image type : {type(img)}")
print(f"- image type : {img.shape}")

# visualize image
print("visualize image...")
cv2.imshow('image', img)

# waiting
print("- wait 2 sec")
cv2.waitKey(2000)   # waiting 2sec=2000ms
# cv2.waitKey(0)    # waiting unlimited..

cv2.destroyAllWindows()
