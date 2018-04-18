from FaceDetector import FaceDetector
import cv2 as cv
detector = FaceDetector("LeBron James")
detector.detect()
i = 0
for face in detector.faces:
    cv.imshow("image" , face)
    i+=1
    cv.waitKey(1000)
cv.destroyAllWindows()