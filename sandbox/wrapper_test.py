import numpy as np
import cv2
import texturesynth
import sys

obj = texturesynth.TextureSynth('../textureSynth', '~/src/matlabPyrTools')
img = cv2.imread(sys.argv[1], 0)
res = obj.analyze(img, 4, 4, 7)

ims = obj.synthesis(res)
print ims
