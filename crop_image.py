import cv2
import numpy as np
import math
rotateimg=cv2.imread('D:/table/dbnet_torch-kd/test_image-barcode/1.jpg')
cnt = np.array([[245, 555],[327 ,547],[332 ,593],[250 ,601]])
rect = cv2.minAreaRect(cnt)#rect为[(旋转中心x坐标，旋转中心y坐标)，(矩形长，矩形宽),旋转角度]
box_origin = cv2.boxPoints(rect)#box_origin为[(x0,y0),(x1,y1),(x2,y2),(x3,y3)]
M = cv2.getRotationMatrix2D(rect[0],rect[2],1)
dst = cv2.warpAffine(rotateimg,M,(2*rotateimg.shape[0],2*rotateimg.shape[1]))
#逆时针旋转
def Nrotate(angle,valuex,valuey,pointx,pointy):
      angle = (angle/180)*math.pi
      valuex = np.array(valuex)
      valuey = np.array(valuey)
      nRotatex = (valuex-pointx)*math.cos(angle) - (valuey-pointy)*math.sin(angle) + pointx
      nRotatey = (valuex-pointx)*math.sin(angle) + (valuey-pointy)*math.cos(angle) + pointy
      return (nRotatex, nRotatey)
#顺时针旋转
def Srotate(angle,valuex,valuey,pointx,pointy):
      angle = (angle/180)*math.pi
      valuex = np.array(valuex)
      valuey = np.array(valuey)
      sRotatex = (valuex-pointx)*math.cos(angle) + (valuey-pointy)*math.sin(angle) + pointx
      sRotatey = (valuey-pointy)*math.cos(angle) - (valuex-pointx)*math.sin(angle) + pointy
      return (sRotatex,sRotatey)
#将四个点做映射
def rotatecordiate(angle,rectboxs,pointx,pointy):
      output = []
      for rectbox in rectboxs:
        if angle>0:
          output.append(Srotate(angle,rectbox[0],rectbox[1],pointx,pointy))
        else:
          output.append(Nrotate(-angle,rectbox[0],rectbox[1],pointx,pointy))
      return output

box = rotatecordiate(rect[2],box_origin,rect[0][0],rect[0][1])

#剪裁
def imagecrop(image, box):
    xs = [x[1] for x in box]
    ys = [x[0] for x in box]
    print(xs)
    print(min(xs), max(xs), min(ys), max(ys))
    cropimage = image[min(xs):max(xs), min(ys):max(ys)]
    print(cropimage.shape)
    cv2.imwrite('cropimage.png', cropimage)
    return cropimage

imagecrop(dst, np.int0(box))
