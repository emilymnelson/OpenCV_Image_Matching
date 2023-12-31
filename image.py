

import cv2 as cv
import pprint as pp
import numpy as np
from matplotlib import pyplot as py
from google.colab.patches import cv2_imshow

r_c = 10680

#smallest number of bins = blue
#medium number of bins = red
#largest number of bins = green

red_bins = 64
green_bins = 128
blue_bins = 64

img1 = cv.imread('i01.jpg', cv.IMREAD_COLOR)
img2 = cv.imread('i02.jpg', cv.IMREAD_COLOR)
img3 = cv.imread('i03.jpg', cv.IMREAD_COLOR)
img4 = cv.imread('i04.jpg', cv.IMREAD_COLOR)
img5 = cv.imread('i05.jpg', cv.IMREAD_COLOR)
img6 = cv.imread('i06.jpg', cv.IMREAD_COLOR)
img7 = cv.imread('i07.jpg', cv.IMREAD_COLOR)
img8 = cv.imread('i08.jpg', cv.IMREAD_COLOR)
img9 = cv.imread('i09.jpg', cv.IMREAD_COLOR)
img10 = cv.imread('i10.jpg', cv.IMREAD_COLOR)
img11 = cv.imread('i11.jpg', cv.IMREAD_COLOR)
img12 = cv.imread('i12.jpg', cv.IMREAD_COLOR)
img13 = cv.imread('i13.jpg', cv.IMREAD_COLOR)
img14 = cv.imread('i14.jpg', cv.IMREAD_COLOR)
img15 = cv.imread('i15.jpg', cv.IMREAD_COLOR)
img16 = cv.imread('i16.jpg', cv.IMREAD_COLOR)
img17 = cv.imread('i17.jpg', cv.IMREAD_COLOR)
img18 = cv.imread('i18.jpg', cv.IMREAD_COLOR)
img19 = cv.imread('i19.jpg', cv.IMREAD_COLOR)
img20 = cv.imread('i20.jpg', cv.IMREAD_COLOR)
img21 = cv.imread('i21.jpg', cv.IMREAD_COLOR)
img22 = cv.imread('i22.jpg', cv.IMREAD_COLOR)
img23 = cv.imread('i23.jpg', cv.IMREAD_COLOR)
img24 = cv.imread('i24.jpg', cv.IMREAD_COLOR)
img25 = cv.imread('i25.jpg', cv.IMREAD_COLOR)
img26 = cv.imread('i26.jpg', cv.IMREAD_COLOR)
img27 = cv.imread('i27.jpg', cv.IMREAD_COLOR)
img28 = cv.imread('i28.jpg', cv.IMREAD_COLOR)
img29 = cv.imread('i29.jpg', cv.IMREAD_COLOR)
img30 = cv.imread('i30.jpg', cv.IMREAD_COLOR)
img31 = cv.imread('i31.jpg', cv.IMREAD_COLOR)
img32 = cv.imread('i32.jpg', cv.IMREAD_COLOR)
img33 = cv.imread('i33.jpg', cv.IMREAD_COLOR)
img34 = cv.imread('i34.jpg', cv.IMREAD_COLOR)
img35 = cv.imread('i35.jpg', cv.IMREAD_COLOR)
img36 = cv.imread('i36.jpg', cv.IMREAD_COLOR)
img37 = cv.imread('i37.jpg', cv.IMREAD_COLOR)
img38 = cv.imread('i38.jpg', cv.IMREAD_COLOR)
img39 = cv.imread('i39.jpg', cv.IMREAD_COLOR)
img40 = cv.imread('i40.jpg', cv.IMREAD_COLOR)


for i in range(1, 41):
  exec('hist%s = cv.calcHist([img%s],[0,1,2],None,[red_bins, green_bins, blue_bins],[0,256, 0, 256, 0, 256])' % (i, i))


for i in range(1, 41):
  differences = []

  for j in range(1, 41):
    hist_diff = eval('hist%s - hist%s' % (i,j) )
    difference = sum(sum(sum(abs(hist_diff))))
    difference = difference/r_c
    differences.append(difference)

  differences = np.argsort(differences)
  #print(differences)
  print("Query number:", i)
  for x in range(1,4):
    print("Image number: ", differences[x]+1)



#2^(8+8+8) is 2^24, which is 16M
#2^(2+2+2) is 2^6, which is 64
#2^(1+1+1) is 2^3, which is 8
#number of bins should be between 2 and 256
#2 is not enough bins, 256 is too many

import cv2 as cv
import pprint as pp
import numpy as np
from matplotlib import pyplot as py
from google.colab.patches import cv2_imshow

r_c = 10680

img1 = cv.imread('i01.jpg', cv.COLOR_BGR2GRAY)
img2 = cv.imread('i02.jpg', cv.COLOR_BGR2GRAY)
img3 = cv.imread('i03.jpg', cv.COLOR_BGR2GRAY)
img4 = cv.imread('i04.jpg', cv.COLOR_BGR2GRAY)
img5 = cv.imread('i05.jpg', cv.COLOR_BGR2GRAY)
img6 = cv.imread('i06.jpg', cv.COLOR_BGR2GRAY)
img7 = cv.imread('i07.jpg', cv.COLOR_BGR2GRAY)
img8 = cv.imread('i08.jpg', cv.COLOR_BGR2GRAY)
img9 = cv.imread('i09.jpg', cv.COLOR_BGR2GRAY)
img10 = cv.imread('i10.jpg', cv.COLOR_BGR2GRAY)
img11 = cv.imread('i11.jpg', cv.COLOR_BGR2GRAY)
img12 = cv.imread('i12.jpg', cv.COLOR_BGR2GRAY)
img13 = cv.imread('i13.jpg', cv.COLOR_BGR2GRAY)
img14 = cv.imread('i14.jpg', cv.COLOR_BGR2GRAY)
img15 = cv.imread('i15.jpg', cv.COLOR_BGR2GRAY)
img16 = cv.imread('i16.jpg', cv.COLOR_BGR2GRAY)
img17 = cv.imread('i17.jpg', cv.COLOR_BGR2GRAY)
img18 = cv.imread('i18.jpg', cv.COLOR_BGR2GRAY)
img19 = cv.imread('i19.jpg', cv.COLOR_BGR2GRAY)
img20 = cv.imread('i20.jpg', cv.COLOR_BGR2GRAY)
img21 = cv.imread('i21.jpg', cv.COLOR_BGR2GRAY)
img22 = cv.imread('i22.jpg', cv.COLOR_BGR2GRAY)
img23 = cv.imread('i23.jpg', cv.COLOR_BGR2GRAY)
img24 = cv.imread('i24.jpg', cv.COLOR_BGR2GRAY)
img25 = cv.imread('i25.jpg', cv.COLOR_BGR2GRAY)
img26 = cv.imread('i26.jpg', cv.COLOR_BGR2GRAY)
img27 = cv.imread('i27.jpg', cv.COLOR_BGR2GRAY)
img28 = cv.imread('i28.jpg', cv.COLOR_BGR2GRAY)
img29 = cv.imread('i29.jpg', cv.COLOR_BGR2GRAY)
img30 = cv.imread('i30.jpg', cv.COLOR_BGR2GRAY)
img31 = cv.imread('i31.jpg', cv.COLOR_BGR2GRAY)
img32 = cv.imread('i32.jpg', cv.COLOR_BGR2GRAY)
img33 = cv.imread('i33.jpg', cv.COLOR_BGR2GRAY)
img34 = cv.imread('i34.jpg', cv.COLOR_BGR2GRAY)
img35 = cv.imread('i35.jpg', cv.COLOR_BGR2GRAY)
img36 = cv.imread('i36.jpg', cv.COLOR_BGR2GRAY)
img37 = cv.imread('i37.jpg', cv.COLOR_BGR2GRAY)
img38 = cv.imread('i38.jpg', cv.COLOR_BGR2GRAY)
img39 = cv.imread('i39.jpg', cv.COLOR_BGR2GRAY)
img40 = cv.imread('i40.jpg', cv.COLOR_BGR2GRAY)

##Laplacian function as learned from OpenCV documentation
#Kernel set to 8 as per instructions so that each pixel's Laplacian
#value is 8 times the original

lap1 = cv.Laplacian(img1, cv.CV_16S, 8)
abs_lap1 = cv.convertScaleAbs(lap1)
lap2 = cv.Laplacian(img2, cv.CV_16S, 8)
abs_lap2 = cv.convertScaleAbs(lap2)
lap3 = cv.Laplacian(img3, cv.CV_16S, 8)
abs_lap3 = cv.convertScaleAbs(lap3)
lap4 = cv.Laplacian(img4, cv.CV_16S, 8)
abs_lap4 = cv.convertScaleAbs(lap4)
lap5 = cv.Laplacian(img5, cv.CV_16S, 8)
abs_lap5 = cv.convertScaleAbs(lap5)
lap6 = cv.Laplacian(img6, cv.CV_16S, 8)
abs_lap6 = cv.convertScaleAbs(lap6)
lap7 = cv.Laplacian(img7, cv.CV_16S, 8)
abs_lap7 = cv.convertScaleAbs(lap7)
lap8 = cv.Laplacian(img8, cv.CV_16S, 8)
abs_lap8 = cv.convertScaleAbs(lap8)
lap9 = cv.Laplacian(img9, cv.CV_16S, 8)
abs_lap9 = cv.convertScaleAbs(lap9)
lap10 = cv.Laplacian(img10, cv.CV_16S, 8)
abs_lap10 = cv.convertScaleAbs(lap10)
lap11 = cv.Laplacian(img11, cv.CV_16S, 8)
abs_lap11 = cv.convertScaleAbs(lap11)
lap12 = cv.Laplacian(img12, cv.CV_16S, 8)
abs_lap12 = cv.convertScaleAbs(lap12)
lap13 = cv.Laplacian(img13, cv.CV_16S, 8)
abs_lap13 = cv.convertScaleAbs(lap13)
lap14 = cv.Laplacian(img14, cv.CV_16S, 8)
abs_lap14 = cv.convertScaleAbs(lap14)
lap15 = cv.Laplacian(img15, cv.CV_16S, 8)
abs_lap15 = cv.convertScaleAbs(lap15)
lap16 = cv.Laplacian(img16, cv.CV_16S, 8)
abs_lap16 = cv.convertScaleAbs(lap16)
lap17 = cv.Laplacian(img17, cv.CV_16S, 8)
abs_lap17 = cv.convertScaleAbs(lap17)
lap18 = cv.Laplacian(img18, cv.CV_16S, 8)
abs_lap18 = cv.convertScaleAbs(lap18)
lap19 = cv.Laplacian(img19, cv.CV_16S, 8)
abs_lap19 = cv.convertScaleAbs(lap19)
lap20 = cv.Laplacian(img20, cv.CV_16S, 8)
abs_lap20 = cv.convertScaleAbs(lap20)
lap21 = cv.Laplacian(img21, cv.CV_16S, 8)
abs_lap21 = cv.convertScaleAbs(lap21)
lap22 = cv.Laplacian(img22, cv.CV_16S, 8)
abs_lap22 = cv.convertScaleAbs(lap22)
lap23 = cv.Laplacian(img23, cv.CV_16S, 8)
abs_lap23 = cv.convertScaleAbs(lap23)
lap24 = cv.Laplacian(img24, cv.CV_16S, 8)
abs_lap24 = cv.convertScaleAbs(lap24)
lap25 = cv.Laplacian(img25, cv.CV_16S, 8)
abs_lap25 = cv.convertScaleAbs(lap25)
lap26 = cv.Laplacian(img26, cv.CV_16S, 8)
abs_lap26 = cv.convertScaleAbs(lap26)
lap27 = cv.Laplacian(img27, cv.CV_16S, 8)
abs_lap27 = cv.convertScaleAbs(lap27)
lap28 = cv.Laplacian(img28, cv.CV_16S, 8)
abs_lap28 = cv.convertScaleAbs(lap28)
lap29 = cv.Laplacian(img29, cv.CV_16S, 8)
abs_lap29 = cv.convertScaleAbs(lap29)
lap30 = cv.Laplacian(img30, cv.CV_16S, 8)
abs_lap30 = cv.convertScaleAbs(lap30)
lap31 = cv.Laplacian(img31, cv.CV_16S, 8)
abs_lap31 = cv.convertScaleAbs(lap31)
lap32 = cv.Laplacian(img32, cv.CV_16S, 8)
abs_lap32 = cv.convertScaleAbs(lap32)
lap33 = cv.Laplacian(img33, cv.CV_16S, 8)
abs_lap33 = cv.convertScaleAbs(lap33)
lap34 = cv.Laplacian(img34, cv.CV_16S, 8)
abs_lap34 = cv.convertScaleAbs(lap34)
lap35 = cv.Laplacian(img35, cv.CV_16S, 8)
abs_lap35 = cv.convertScaleAbs(lap35)
lap36 = cv.Laplacian(img36, cv.CV_16S, 8)
abs_lap36 = cv.convertScaleAbs(lap36)
lap37 = cv.Laplacian(img37, cv.CV_16S, 8)
abs_lap37 = cv.convertScaleAbs(lap37)
lap38 = cv.Laplacian(img38, cv.CV_16S, 8)
abs_lap38 = cv.convertScaleAbs(lap38)
lap39 = cv.Laplacian(img39, cv.CV_16S, 8)
abs_lap39 = cv.convertScaleAbs(lap39)
lap40 = cv.Laplacian(img40, cv.CV_16S, 8)
abs_lap40 = cv.convertScaleAbs(lap40)


lhist1 = cv.calcHist([abs_lap1],[0],None,[256],[0,256])
lhist2 = cv.calcHist([abs_lap2],[0],None,[256],[0,256])
lhist3 = cv.calcHist([abs_lap3],[0],None,[256],[0,256])
lhist4 = cv.calcHist([abs_lap4],[0],None,[256],[0,256])
lhist5 = cv.calcHist([abs_lap5],[0],None,[256],[0,256])
lhist6 = cv.calcHist([abs_lap6],[0],None,[256],[0,256])
lhist7 = cv.calcHist([abs_lap7],[0],None,[256],[0,256])
lhist8 = cv.calcHist([abs_lap8],[0],None,[256],[0,256])
lhist9 = cv.calcHist([abs_lap9],[0],None,[256],[0,256])
lhist10 = cv.calcHist([abs_lap10],[0],None,[256],[0,256])
lhist11 = cv.calcHist([abs_lap11],[0],None,[256],[0,256])
lhist12 = cv.calcHist([abs_lap12],[0],None,[256],[0,256])
lhist13 = cv.calcHist([abs_lap13],[0],None,[256],[0,256])
lhist14 = cv.calcHist([abs_lap14],[0],None,[256],[0,256])
lhist15 = cv.calcHist([abs_lap15],[0],None,[256],[0,256])
lhist16 = cv.calcHist([abs_lap16],[0],None,[256],[0,256])
lhist17 = cv.calcHist([abs_lap17],[0],None,[256],[0,256])
lhist18 = cv.calcHist([abs_lap18],[0],None,[256],[0,256])
lhist19 = cv.calcHist([abs_lap19],[0],None,[256],[0,256])
lhist20 = cv.calcHist([abs_lap20],[0],None,[256],[0,256])
lhist21 = cv.calcHist([abs_lap21],[0],None,[256],[0,256])
lhist22 = cv.calcHist([abs_lap22],[0],None,[256],[0,256])
lhist23 = cv.calcHist([abs_lap23],[0],None,[256],[0,256])
lhist24 = cv.calcHist([abs_lap24],[0],None,[256],[0,256])
lhist25 = cv.calcHist([abs_lap25],[0],None,[256],[0,256])
lhist26 = cv.calcHist([abs_lap26],[0],None,[256],[0,256])
lhist27 = cv.calcHist([abs_lap27],[0],None,[256],[0,256])
lhist28 = cv.calcHist([abs_lap28],[0],None,[256],[0,256])
lhist29 = cv.calcHist([abs_lap29],[0],None,[256],[0,256])
lhist30 = cv.calcHist([abs_lap30],[0],None,[256],[0,256])
lhist31 = cv.calcHist([abs_lap31],[0],None,[256],[0,256])
lhist32 = cv.calcHist([abs_lap32],[0],None,[256],[0,256])
lhist33 = cv.calcHist([abs_lap33],[0],None,[256],[0,256])
lhist34 = cv.calcHist([abs_lap34],[0],None,[256],[0,256])
lhist35 = cv.calcHist([abs_lap35],[0],None,[256],[0,256])
lhist36 = cv.calcHist([abs_lap36],[0],None,[256],[0,256])
lhist37 = cv.calcHist([abs_lap37],[0],None,[256],[0,256])
lhist38 = cv.calcHist([abs_lap38],[0],None,[256],[0,256])
lhist39 = cv.calcHist([abs_lap39],[0],None,[256],[0,256])
lhist40 = cv.calcHist([abs_lap40],[0],None,[256],[0,256])


for i in range(1, 41):
  differences = []

  for j in range(1, 41):
    hist_diff = eval('lhist%s - lhist%s' % (i,j) )
    difference = sum(sum(abs(hist_diff)))
    difference = difference/r_c
    differences.append(difference)

  differences = np.argsort(differences)
  #print(differences)
  print("Query number:", i)
  for x in range(1,4):
    print("Image number: ", differences[x]+1)

import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)



f = np.loadtxt("Crowd.txt", dtype=int)

##score checker
##to find score, use item number - 1
#for example, photos 3,10,4 are 2,9,3
#query number is also -1, for example item 1 is 0
print(f[39][29])
print(f[39][13])
print(f[39][15])


f = np.argsort(-f, axis = 1)

for i in range(40):
  #print("Query number: ", i+1)
  for j in range(3):
    item = f[i][j]
    #print(item+1)

import cv2 as cv
import pprint as pp
import numpy as np
from matplotlib import pyplot as py
from google.colab.patches import cv2_imshow

r_c = 5340

i1 = cv.imread('i01.jpg')
i2 = cv.imread('i02.jpg')
i3 = cv.imread('i03.jpg')
i4 = cv.imread('i04.jpg')
i5 = cv.imread('i05.jpg')
i6 = cv.imread('i06.jpg')
i7 = cv.imread('i07.jpg')
i8 = cv.imread('i08.jpg')
i9 = cv.imread('i09.jpg')
i10 = cv.imread('i10.jpg')
i11 = cv.imread('i11.jpg')
i12 = cv.imread('i12.jpg')
i13 = cv.imread('i13.jpg')
i14 = cv.imread('i14.jpg')
i15 = cv.imread('i15.jpg')
i16 = cv.imread('i16.jpg')
i17 = cv.imread('i17.jpg')
i18 = cv.imread('i18.jpg')
i19 = cv.imread('i19.jpg')
i20 = cv.imread('i20.jpg')
i21 = cv.imread('i21.jpg')
i22 = cv.imread('i22.jpg')
i23 = cv.imread('i23.jpg')
i24 = cv.imread('i24.jpg')
i25 = cv.imread('i25.jpg')
i26 = cv.imread('i26.jpg')
i27 = cv.imread('i27.jpg')
i28 = cv.imread('i28.jpg')
i29 = cv.imread('i29.jpg')
i30 = cv.imread('i30.jpg')
i31 = cv.imread('i31.jpg')
i32 = cv.imread('i32.jpg')
i33 = cv.imread('i33.jpg')
i34 = cv.imread('i34.jpg')
i35 = cv.imread('i35.jpg')
i36 = cv.imread('i36.jpg')
i37 = cv.imread('i37.jpg')
i38 = cv.imread('i38.jpg')
i39 = cv.imread('i39.jpg')
i40 = cv.imread('i40.jpg')

img1 = cv.cvtColor(i1, cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(i2, cv.COLOR_BGR2GRAY)
img3 = cv.cvtColor(i3, cv.COLOR_BGR2GRAY)
img4 = cv.cvtColor(i4, cv.COLOR_BGR2GRAY)
img5 = cv.cvtColor(i5, cv.COLOR_BGR2GRAY)
img6 = cv.cvtColor(i6, cv.COLOR_BGR2GRAY)
img7 = cv.cvtColor(i7, cv.COLOR_BGR2GRAY)
img8 = cv.cvtColor(i8, cv.COLOR_BGR2GRAY)
img9 = cv.cvtColor(i9, cv.COLOR_BGR2GRAY)
img10 = cv.cvtColor(i10, cv.COLOR_BGR2GRAY)
img11 = cv.cvtColor(i11, cv.COLOR_BGR2GRAY)
img12 = cv.cvtColor(i12, cv.COLOR_BGR2GRAY)
img13 = cv.cvtColor(i13, cv.COLOR_BGR2GRAY)
img14 = cv.cvtColor(i14, cv.COLOR_BGR2GRAY)
img15 = cv.cvtColor(i15, cv.COLOR_BGR2GRAY)
img16 = cv.cvtColor(i16, cv.COLOR_BGR2GRAY)
img17 = cv.cvtColor(i17, cv.COLOR_BGR2GRAY)
img18 = cv.cvtColor(i18, cv.COLOR_BGR2GRAY)
img19 = cv.cvtColor(i19, cv.COLOR_BGR2GRAY)
img20 = cv.cvtColor(i20, cv.COLOR_BGR2GRAY)
img21 = cv.cvtColor(i21, cv.COLOR_BGR2GRAY)
img22 = cv.cvtColor(i22, cv.COLOR_BGR2GRAY)
img23 = cv.cvtColor(i23, cv.COLOR_BGR2GRAY)
img24 = cv.cvtColor(i24, cv.COLOR_BGR2GRAY)
img25 = cv.cvtColor(i25, cv.COLOR_BGR2GRAY)
img26 = cv.cvtColor(i26, cv.COLOR_BGR2GRAY)
img27 = cv.cvtColor(i27, cv.COLOR_BGR2GRAY)
img28 = cv.cvtColor(i28, cv.COLOR_BGR2GRAY)
img29 = cv.cvtColor(i29, cv.COLOR_BGR2GRAY)
img30 = cv.cvtColor(i30, cv.COLOR_BGR2GRAY)
img31 = cv.cvtColor(i31, cv.COLOR_BGR2GRAY)
img32 = cv.cvtColor(i32, cv.COLOR_BGR2GRAY)
img33 = cv.cvtColor(i33, cv.COLOR_BGR2GRAY)
img34 = cv.cvtColor(i34, cv.COLOR_BGR2GRAY)
img35 = cv.cvtColor(i35, cv.COLOR_BGR2GRAY)
img36 = cv.cvtColor(i36, cv.COLOR_BGR2GRAY)
img37 = cv.cvtColor(i37, cv.COLOR_BGR2GRAY)
img38 = cv.cvtColor(i38, cv.COLOR_BGR2GRAY)
img39 = cv.cvtColor(i39, cv.COLOR_BGR2GRAY)
img40 = cv.cvtColor(i40, cv.COLOR_BGR2GRAY)


ret, bny1 = cv.threshold(img1, 90, 200, cv.THRESH_BINARY)
ret, bny2 = cv.threshold(img2, 90, 200, cv.THRESH_BINARY)
ret, bny3 = cv.threshold(img3, 90, 200, cv.THRESH_BINARY)
ret, bny4 = cv.threshold(img4, 90, 200, cv.THRESH_BINARY)
ret, bny5 = cv.threshold(img5, 90, 200, cv.THRESH_BINARY)
ret, bny6 = cv.threshold(img6, 90, 200, cv.THRESH_BINARY)
ret, bny7 = cv.threshold(img7, 90, 200, cv.THRESH_BINARY)
ret, bny8 = cv.threshold(img8, 90, 200, cv.THRESH_BINARY)
ret, bny9 = cv.threshold(img9, 90, 200, cv.THRESH_BINARY)
ret, bny10 = cv.threshold(img10, 90, 200, cv.THRESH_BINARY)
ret, bny11 = cv.threshold(img11, 90, 200, cv.THRESH_BINARY)
ret, bny12 = cv.threshold(img12, 90, 200, cv.THRESH_BINARY)
ret, bny13 = cv.threshold(img13, 90, 200, cv.THRESH_BINARY)
ret, bny14 = cv.threshold(img14, 90, 200, cv.THRESH_BINARY)
ret, bny15 = cv.threshold(img15, 90, 200, cv.THRESH_BINARY)
ret, bny16 = cv.threshold(img16, 90, 200, cv.THRESH_BINARY)
ret, bny17 = cv.threshold(img17, 90, 200, cv.THRESH_BINARY)
ret, bny18 = cv.threshold(img18, 90, 200, cv.THRESH_BINARY)
ret, bny19 = cv.threshold(img19, 90, 200, cv.THRESH_BINARY)
ret, bny20 = cv.threshold(img20, 90, 200, cv.THRESH_BINARY)
ret, bny21 = cv.threshold(img21, 90, 200, cv.THRESH_BINARY)
ret, bny22 = cv.threshold(img22, 90, 200, cv.THRESH_BINARY)
ret, bny23 = cv.threshold(img23, 90, 200, cv.THRESH_BINARY)
ret, bny24 = cv.threshold(img24, 90, 200, cv.THRESH_BINARY)
ret, bny25 = cv.threshold(img25, 90, 200, cv.THRESH_BINARY)
ret, bny26 = cv.threshold(img26, 90, 200, cv.THRESH_BINARY)
ret, bny27 = cv.threshold(img27, 90, 200, cv.THRESH_BINARY)
ret, bny28 = cv.threshold(img28, 90, 200, cv.THRESH_BINARY)
ret, bny29 = cv.threshold(img29, 90, 200, cv.THRESH_BINARY)
ret, bny30 = cv.threshold(img30, 90, 200, cv.THRESH_BINARY)
ret, bny31 = cv.threshold(img31, 90, 200, cv.THRESH_BINARY)
ret, bny32 = cv.threshold(img32, 90, 200, cv.THRESH_BINARY)
ret, bny33 = cv.threshold(img33, 90, 200, cv.THRESH_BINARY)
ret, bny34 = cv.threshold(img34, 90, 200, cv.THRESH_BINARY)
ret, bny35 = cv.threshold(img35, 90, 200, cv.THRESH_BINARY)
ret, bny36 = cv.threshold(img36, 90, 200, cv.THRESH_BINARY)
ret, bny37 = cv.threshold(img37, 90, 200, cv.THRESH_BINARY)
ret, bny38 = cv.threshold(img38, 90, 200, cv.THRESH_BINARY)
ret, bny39 = cv.threshold(img39, 90, 200, cv.THRESH_BINARY)
ret, bny40 = cv.threshold(img40, 90, 200, cv.THRESH_BINARY)


#find symmetry of each image
#find items with closest symmetry

#columns 1-44 and columns 46-89

diffs = []

for i in range(40, 0, -1):
  col_diff = []
  column = 88

  for j in range(40):
    col1 = eval('bny%s[:,%s]' % (i, j) )
    col2 = eval('bny%s[:, column]' % (i))

    if np.allclose(col1, col2):
      col_diff.append(0)
    else:
      col_diff.append(1)

    column = column - 1

  diffs.append(sum(col_diff)/r_c)
  #print("Query number:", i)
  #for x in range(1,4):
    #print("Image number: ", differences[x]+1)

#diffs is an array of all images's respective symmetry scores
#print(diffs)

for x in range(40):
  print(x, diffs[x])

print(np.argsort(diffs))

import cv2 as cv
import pprint as pp
import numpy as np
from matplotlib import pyplot as py
from google.colab.patches import cv2_imshow

r_c = 10680

i1 = cv.imread('i01.jpg')
i2 = cv.imread('i02.jpg')
i3 = cv.imread('i03.jpg')
i4 = cv.imread('i04.jpg')
i5 = cv.imread('i05.jpg')
i6 = cv.imread('i06.jpg')
i7 = cv.imread('i07.jpg')
i8 = cv.imread('i08.jpg')
i9 = cv.imread('i09.jpg')
i10 = cv.imread('i10.jpg')
i11 = cv.imread('i11.jpg')
i12 = cv.imread('i12.jpg')
i13 = cv.imread('i13.jpg')
i14 = cv.imread('i14.jpg')
i15 = cv.imread('i15.jpg')
i16 = cv.imread('i16.jpg')
i17 = cv.imread('i17.jpg')
i18 = cv.imread('i18.jpg')
i19 = cv.imread('i19.jpg')
i20 = cv.imread('i20.jpg')
i21 = cv.imread('i21.jpg')
i22 = cv.imread('i22.jpg')
i23 = cv.imread('i23.jpg')
i24 = cv.imread('i24.jpg')
i25 = cv.imread('i25.jpg')
i26 = cv.imread('i26.jpg')
i27 = cv.imread('i27.jpg')
i28 = cv.imread('i28.jpg')
i29 = cv.imread('i29.jpg')
i30 = cv.imread('i30.jpg')
i31 = cv.imread('i31.jpg')
i32 = cv.imread('i32.jpg')
i33 = cv.imread('i33.jpg')
i34 = cv.imread('i34.jpg')
i35 = cv.imread('i35.jpg')
i36 = cv.imread('i36.jpg')
i37 = cv.imread('i37.jpg')
i38 = cv.imread('i38.jpg')
i39 = cv.imread('i39.jpg')
i40 = cv.imread('i40.jpg')

img1 = cv.cvtColor(i1, cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(i2, cv.COLOR_BGR2GRAY)
img3 = cv.cvtColor(i3, cv.COLOR_BGR2GRAY)
img4 = cv.cvtColor(i4, cv.COLOR_BGR2GRAY)
img5 = cv.cvtColor(i5, cv.COLOR_BGR2GRAY)
img6 = cv.cvtColor(i6, cv.COLOR_BGR2GRAY)
img7 = cv.cvtColor(i7, cv.COLOR_BGR2GRAY)
img8 = cv.cvtColor(i8, cv.COLOR_BGR2GRAY)
img9 = cv.cvtColor(i9, cv.COLOR_BGR2GRAY)
img10 = cv.cvtColor(i10, cv.COLOR_BGR2GRAY)
img11 = cv.cvtColor(i11, cv.COLOR_BGR2GRAY)
img12 = cv.cvtColor(i12, cv.COLOR_BGR2GRAY)
img13 = cv.cvtColor(i13, cv.COLOR_BGR2GRAY)
img14 = cv.cvtColor(i14, cv.COLOR_BGR2GRAY)
img15 = cv.cvtColor(i15, cv.COLOR_BGR2GRAY)
img16 = cv.cvtColor(i16, cv.COLOR_BGR2GRAY)
img17 = cv.cvtColor(i17, cv.COLOR_BGR2GRAY)
img18 = cv.cvtColor(i18, cv.COLOR_BGR2GRAY)
img19 = cv.cvtColor(i19, cv.COLOR_BGR2GRAY)
img20 = cv.cvtColor(i20, cv.COLOR_BGR2GRAY)
img21 = cv.cvtColor(i21, cv.COLOR_BGR2GRAY)
img22 = cv.cvtColor(i22, cv.COLOR_BGR2GRAY)
img23 = cv.cvtColor(i23, cv.COLOR_BGR2GRAY)
img24 = cv.cvtColor(i24, cv.COLOR_BGR2GRAY)
img25 = cv.cvtColor(i25, cv.COLOR_BGR2GRAY)
img26 = cv.cvtColor(i26, cv.COLOR_BGR2GRAY)
img27 = cv.cvtColor(i27, cv.COLOR_BGR2GRAY)
img28 = cv.cvtColor(i28, cv.COLOR_BGR2GRAY)
img29 = cv.cvtColor(i29, cv.COLOR_BGR2GRAY)
img30 = cv.cvtColor(i30, cv.COLOR_BGR2GRAY)
img31 = cv.cvtColor(i31, cv.COLOR_BGR2GRAY)
img32 = cv.cvtColor(i32, cv.COLOR_BGR2GRAY)
img33 = cv.cvtColor(i33, cv.COLOR_BGR2GRAY)
img34 = cv.cvtColor(i34, cv.COLOR_BGR2GRAY)
img35 = cv.cvtColor(i35, cv.COLOR_BGR2GRAY)
img36 = cv.cvtColor(i36, cv.COLOR_BGR2GRAY)
img37 = cv.cvtColor(i37, cv.COLOR_BGR2GRAY)
img38 = cv.cvtColor(i38, cv.COLOR_BGR2GRAY)
img39 = cv.cvtColor(i39, cv.COLOR_BGR2GRAY)
img40 = cv.cvtColor(i40, cv.COLOR_BGR2GRAY)


ret, bny1 = cv.threshold(img1, 90, 200, cv.THRESH_BINARY)
ret, bny2 = cv.threshold(img2, 90, 200, cv.THRESH_BINARY)
ret, bny3 = cv.threshold(img3, 90, 200, cv.THRESH_BINARY)
ret, bny4 = cv.threshold(img4, 90, 200, cv.THRESH_BINARY)
ret, bny5 = cv.threshold(img5, 90, 200, cv.THRESH_BINARY)
ret, bny6 = cv.threshold(img6, 90, 200, cv.THRESH_BINARY)
ret, bny7 = cv.threshold(img7, 90, 200, cv.THRESH_BINARY)
ret, bny8 = cv.threshold(img8, 90, 200, cv.THRESH_BINARY)
ret, bny9 = cv.threshold(img9, 90, 200, cv.THRESH_BINARY)
ret, bny10 = cv.threshold(img10, 90, 200, cv.THRESH_BINARY)
ret, bny11 = cv.threshold(img11, 90, 200, cv.THRESH_BINARY)
ret, bny12 = cv.threshold(img12, 90, 200, cv.THRESH_BINARY)
ret, bny13 = cv.threshold(img13, 90, 200, cv.THRESH_BINARY)
ret, bny14 = cv.threshold(img14, 90, 200, cv.THRESH_BINARY)
ret, bny15 = cv.threshold(img15, 90, 200, cv.THRESH_BINARY)
ret, bny16 = cv.threshold(img16, 90, 200, cv.THRESH_BINARY)
ret, bny17 = cv.threshold(img17, 90, 200, cv.THRESH_BINARY)
ret, bny18 = cv.threshold(img18, 90, 200, cv.THRESH_BINARY)
ret, bny19 = cv.threshold(img19, 90, 200, cv.THRESH_BINARY)
ret, bny20 = cv.threshold(img20, 90, 200, cv.THRESH_BINARY)
ret, bny21 = cv.threshold(img21, 90, 200, cv.THRESH_BINARY)
ret, bny22 = cv.threshold(img22, 90, 200, cv.THRESH_BINARY)
ret, bny23 = cv.threshold(img23, 90, 200, cv.THRESH_BINARY)
ret, bny24 = cv.threshold(img24, 90, 200, cv.THRESH_BINARY)
ret, bny25 = cv.threshold(img25, 90, 200, cv.THRESH_BINARY)
ret, bny26 = cv.threshold(img26, 90, 200, cv.THRESH_BINARY)
ret, bny27 = cv.threshold(img27, 90, 200, cv.THRESH_BINARY)
ret, bny28 = cv.threshold(img28, 90, 200, cv.THRESH_BINARY)
ret, bny29 = cv.threshold(img29, 90, 200, cv.THRESH_BINARY)
ret, bny30 = cv.threshold(img30, 90, 200, cv.THRESH_BINARY)
ret, bny31 = cv.threshold(img31, 90, 200, cv.THRESH_BINARY)
ret, bny32 = cv.threshold(img32, 90, 200, cv.THRESH_BINARY)
ret, bny33 = cv.threshold(img33, 90, 200, cv.THRESH_BINARY)
ret, bny34 = cv.threshold(img34, 90, 200, cv.THRESH_BINARY)
ret, bny35 = cv.threshold(img35, 90, 200, cv.THRESH_BINARY)
ret, bny36 = cv.threshold(img36, 90, 200, cv.THRESH_BINARY)
ret, bny37 = cv.threshold(img37, 90, 200, cv.THRESH_BINARY)
ret, bny38 = cv.threshold(img38, 90, 200, cv.THRESH_BINARY)
ret, bny39 = cv.threshold(img39, 90, 200, cv.THRESH_BINARY)
ret, bny40 = cv.threshold(img40, 90, 200, cv.THRESH_BINARY)


for i in range(1, 41):
  differences = []

  for j in range(1, 41):
    diff = eval('bny%s - bny%s' % (i,j) )
    difference = sum(sum(diff))/r_c
    differences.append(difference)

  differences = np.argsort(differences)
  #print(differences)
  print("Query number:", i)
  for x in range(1,4):
    print("Image number: ", differences[x]+1)



#print(bny1-bny2)
#print(sum(sum(sum(bny1-bny2)))/r_c)
#cv2_imshow(bny1)

