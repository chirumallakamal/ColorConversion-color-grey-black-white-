import cv2
##import matplot.pyplot as plt

Img=cv2.imread('1.jpg');
##plt.title('Image')
##plt.imshow(Img)
cv2.imshow('original Image',Img);
gray = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY);
cv2.imshow('Gray image',gray);
thresh,bandw=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

cv2.imshow("black",bandw)

cv2.waitKey(0)
cv2.destroyAllWindows()
