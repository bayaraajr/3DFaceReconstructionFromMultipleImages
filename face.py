import cv2 as cv
import argparse

image_db = "C:/Users/glbay/PycharmProjects/3DFaceReconstructionFromMultipleImages/images/lfw/"
name = ""
parser = argparse.ArgumentParser(description="Reconstruct 3D model from multiple images")
parser.add_argument("-n", "--name", required=False, help="name of the person" , type=str)

args = vars(parser.parse_args())
if hasattr(args , 'name'):
    name = args.name
else :
    name = raw_input("Name : ")
list = name.split(' ')
name = "_".join(list)
path_to_image = image_db+name+"/"+name+"_0001.jpg"
print path_to_image
img = cv.imread(path_to_image)
print img
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade  = cv.CascadeClassifier('haarcascade_eye.xml')

gray_image = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image , 1.3 , 5)

#for(x , y , w , h)


print img
cv.imshow("image" , img)
cv.waitKey(0)
cv.destroyAllWindows()