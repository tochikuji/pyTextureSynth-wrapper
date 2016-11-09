import numpy as np
import cv2
import texturesynth
import sys

obj = texturesynth.TextureSynth('../textureSynth', '~/src/matlabPyrTools')
img = cv2.imread(sys.argv[1], 0)
res = obj.analyze(img, 4, 4, 7)

arr = texturesynth.util.obj2array(res)
print arr, arr.shape

obj = texturesynth.util.array2obj(arr)
print obj, type(obj)
