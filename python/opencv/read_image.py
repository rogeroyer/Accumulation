
image = cv2.imread('image/FaceDB_orl/001/01.png')   # 考虑是否使用RGB格式，极大增加计算量
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)     # 将RGB图转化为灰度图
print(image.shape)

cv2.namedWindow("Image")
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
