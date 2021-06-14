import cv2
import numpy as np
from math import hypot

img=cv2.imread('g1.jpg')
img = img[5:455, 5:455]#crop img
img= cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_CONSTANT,value=[0,0,0])
im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
im = cv2.GaussianBlur(im,(5,5),0)
#cv2.imshow('med',im)

cpy = im.copy()
cpy2 = img.copy()    
ret,thr=cv2.threshold(cpy,19,255,cv2.THRESH_BINARY)
cont,_=cv2.findContours(thr,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contex,_=cv2.findContours(thr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(cpy2, cont, -1, (0,0,255), 2)
res=cv2.drawContours(cpy2, contex, -1, (0,0,255), 2)
cnt = cont[2]
cntex = contex[0]
(x,y),r = cv2.minEnclosingCircle(cnt)
c = (int(x),int(y))
r = int(r)
cpy2 = cv2.circle(cpy2,c,r,(255,0,0),2)
(xx,yx),rx = cv2.minEnclosingCircle(cntex)
cx = (int(xx),int(yx))
rx = int(rx)
cpy2 = cv2.circle(cpy2,cx,rx,(255,0,0),2)

count=0
hull = cv2.convexHull(cntex,returnPoints = False)
deft = cv2.convexityDefects(cntex,hull)
for i in range(deft.shape[0]):
    s,e,f,d = deft[i,0]
    start = tuple(cntex[s][0])
    end = tuple(cntex[e][0])
    far = tuple(cntex[f][0])       
    cv2.line(cpy2,start,end,[0,255,0],2)
    a,b=far
    if (rx-hypot(xx-a,yx-b))>15:
        count+=1
        cv2.circle(cpy2,far,5,[255,255,255],-1)
        #cv2.circle(cpy2,far,4,[255,255,0],-1)
                
cv2.imshow('res',res)
cv2.waitKey(0)

print(r, 'is internal radius\n',rx ,'is external radius\n')
print(count)
cv2.destroyAllWindows()
cv2.imwrite('res.jpg',res)
