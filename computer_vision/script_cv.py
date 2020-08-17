import cv2

img = cv2.imread("galaxy.jpg", 0) # 0 - black and white (greyscale), 1 - colored images, -1 - colored with transparency

print(type(img))
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2))) # width, height
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resized.jpg", resized_img)
cv2.waitKey(0) # 0 - user can close the window with any key
cv2.destroyAllWindows() # closes the window