
from scipy.misc import imread
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import colorsys

def convert2HSL(rgb_array):
	hsl_array = []
	for i in range(rgb_array):
		rgb_val = rgb_array[i]
		prev_rgb_val=rgb_val
		rgb_val = findMin(rgb_val)
		l= convert2L(rgb_val)
		s= convert2S(rgb_val,l)
		h= convert2H(rgb_val,prev_rgb_val)
		hsl_array.append([h,s,l])

	return hsl_array


def convert2H(rgb_val,prev_rgb_val):
	ind=findMAxIndex(prev_rgb_val)
	diff=rgb_val[2]-rgb_val[0]
	if ind == 0:
		return (prev_rgb_val[1] - prev_rgb_val[2])/diff
	if ind == 1:
		return 2 + (prev_rgb_val[2] -prev_rgb_val[0]) /diff
	if ind == 2:
		return 4 + (prev_rgb_val[0]-prev_rgb_val[1]) /diff

def convert2S(rgb_val,lumi):
	if(lumi > 0.5):
		return (rgb_val[2]- rgb_val[0])/(2 - rgb_val[2]- rgb_val[0] )
	else:
		return (rgb_val[2]- rgb_val[0])/(rgb_val[2]+ rgb_val[0])

def convert2L(rgb_val):
	return (rgb_val[0]+rgb_val[2])/2

def findMin(rgb_val):
	for i in range(rgb_val):
		rgb_val[i]=rgb_val[i]/255

	for x in range(len(rgb_val)-1,0,-1):
		for i in range(x):
		 	if(rgb_val[i] > rgb_val[i+1]):
				temp = rgb_val[i]
				rgb_val[i] = rgb_val[i+1]
				rgb_val[i+1] = temp
	return rgb_val

def findMAxIndex(rgb_val):
	max=0
	j=0
	for i in range(rgb_val):
		if(rgb_val > max):
			max = rgb_val
			j=i
	return j

#img = Image.open('capture.png')
#img.show()

im = imread("wat.jpg",mode='RGB')

print "Rows: %s \nColumns: %s" %(len(im), len(im[2]))

dataArray = []
redArray = []
greenArray = []
blueArray = []

# Create x Array
# Here 389 is the lowest nm and 582 is the heighest nm values for spectrometer
xdata = np.linspace(0,260,len(im[0]))

for x in im[len(im)-1]:
	#print x
	dataArray.append((sum(x[:3]))/3.0)
	redArray.append(x[0])
	greenArray.append(x[1])
	blueArray.append(x[2])

rows = len(im)    # 3 rows in your example
cols = len(im[0]) # 2 columns in your example

print 'Rows : %s \nColumns : %s' % (rows,cols)

#print dataArray
#print convert2HSL(im)
plt.plot(xdata,dataArray, color='k')
plt.plot(xdata,redArray, color='r', alpha=0.5)
plt.plot(xdata,greenArray, color='g', alpha=0.5)
plt.plot(xdata,blueArray, color='b', alpha=0.5)
plt.legend(loc='best')

plt.ylabel('Intensity %')
plt.xlabel('Intensity level')
plt.grid(True)
plt.ylim((0,255))
plt.savefig('test1.png')
plt.show()

