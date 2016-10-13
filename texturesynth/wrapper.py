"""
pyTextureSynth
===

python interface for textureSynth (https://github.com/LabForComputationalVision/textureSynth)

"""
import numpy
import matlab.engine
from util import np2ml, ml2np


class TextureSynth(object):

    def __init__(self, libpath='./TextureSynth/', toolpath='./matlabPyrTools'):
        # create matlab engine instance
        self.eng = matlab.engine.start_matlab()

        if self.eng is None:
            raise RuntimeError("failed to create matlab instance.")

        # set paths
        self.eng.path(toolpath, self.eng.path())
        self.eng.path(libpath, self.eng.path())

    def analyze(self, img, Nsc, Nor, Na=7):

        if isinstance(img, numpy.ndarray):
            if len(img.shape) != 2:
                raise TypeError("image must have single channel")

        param = self.eng.textureAnalysis(
            np2ml(img, dtype=numpy.float32),
            float(int(Nsc)),
            float(int(Nor)),
            float(int(Na))
        )

        return param

    def synthesis(self, param, im0=None, N_iter=50, cmask=None, imask=None):

        # arguments for textureAnalysis
        args = [param]

        if im0 is None:
            im0 = [192, 128]

        args.append(matlab.mlarray.double(im0))

        if not cmask is None:
            args.append(matlab.mlarray.double(cmask))

        if not imask is None:
            args.append(matlab.mlarray.double(imask))

        ret = self.eng.textureSynthesis(*args, nargout=1)

        return ml2np(ret, dtype=numpy.uint8)
