import cv2
import glob # finds pathnames of files
import os

path = "sample_images/*.jpg" # creates a list for files with jpg extension
files = glob.glob(path)
# print(files)

for file in files:
    img = cv2.imread(file, 1)
    img_re = cv2.resize(img, (100,100))
    cv2.imshow(file, img_re)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("sample_images/resized_"+ os.path.basename(file), img_re)