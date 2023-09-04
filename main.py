import cv2
# configurable parameters
source="photo.jpg"
destination="newImage.png"

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
cv2.imshow("tittle",src)

# percent by which image is resized
scale_percent = 50

# calculate 50% of original dimension
new_width = int(src.shape[1]*scale_percent/100)
new_height = int(src.shape[0]*scale_percent/100)
dsize=(new_width,new_height)

# resize image
output=cv2.resize(src,dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)