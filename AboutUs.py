import cv2


img = cv2.imread("aboutme.png")
# bigger = cv2.resize(img, (1000, 750))
# h,w,z = img.shape
Half = cv2.resize(img,(int(w/1.5),int(h/1.5)))
cv2.imshow("About Us", Half)
cv2.waitKey(0)
cv2.destroyAllWindows()