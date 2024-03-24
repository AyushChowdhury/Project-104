import cv2

img=cv2.imread("img.jpg")

cv2.putText(img,"Sun",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
cv2.putText(img,"Mercury",(100,150),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),1)
cv2.putText(img,"Venus",(150,250),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),1)
cv2.putText(img,"Earth",(280,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Mars",(380,250),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)

cv2.imshow("solar_system",img)

cv2.waitKey(2000)