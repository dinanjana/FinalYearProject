import base64
import cv2
import numpy as np
from matplotlib import pyplot as plt
import json

def histogramCalc(path) :
    img = cv2.imread(path)
    color = ('b','g','r')
    result=[None]*3
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
        result[i] = (histr).tolist()
    plt.savefig('test.png')
    plt.show()
    return json.dumps(result,separators=(',', ':'), sort_keys=True)


def takePhoto():
    return

def imageToBase64():
    with open("test.png", "rb") as imageFile:
        return base64.b64encode(imageFile.read())



histogramCalc('vim.jpg')

