import numpy
import matlab


class TextureParam(object):

    def __init__(self, ml_param=None):

        if ml_param is None:
            self.varianceHPR = None
            self.cousinRealCorr = None
            self.parentRealCorr = None
            self.pixelStats = None
            self.autoCorrReal = None
            self.pixelLPStats = None
            self.autoCorrMag = None
            self.cousinMagCorr = None
            self.parentMagCorr = None
            self.magMeans = None

        else:
            self.varianceHPR = ml2np(ml_param['varianceHPR'])
            self.cousinRealCorr = ml2np(ml_param['cousinRealCorr'])
            self.parentRealCorr = ml2np(ml_param['parentRealCorr'])
            self.pixelStats = ml2np(ml_param['pixelStats'])
            self.autoCorrReal = ml2np(ml_param['autoCorrReal'])
            self.pixelLPStats = ml2np(ml_param['pixelLPStats'])
            self.autoCorrMag = ml2np(ml_param['autoCorrMag'])
            self.cousinMagCorr = ml2np(ml_param['cousinMagCorr'])
            self.parentMagCorr = ml2np(ml_param['parentMagCorr'])
            self.magMeans = ml2np(ml_param['magMeans'])


def ml2np(x, dtype=None):
    if dtype is None:
        dtype = numpy.float32

    return numpy.asarray(x, dtype=dtype)


def np2ml(x, dtype=None):

    if dtype is None:
        if isinstance(x, numpy.ndarray):
            dtype = x.dtype

        else:
            dtype = numpy.float32

    if dtype is numpy.float32:
        mdtype = matlab.mlarray.double
    elif dtype is numpy.int32:
        mdtype = matlab.mlarray.int32
    elif dtype is numpy.int8:
        mdtype = matlab.mlarray.int8
    elif dtype is numpy.uint32:
        mdtype = matlab.mlarray.uint32
    elif dtype is numpy.uint8:
        mdtype = matlab.mlarray.uint8

    else:
        raise TypeError("Unsupported type conversion")

    if isinstance(x, numpy.ndarray):

        return mdtype(x.tolist())
    else:

        return mdtype(list(x))


def conv_texture_param(param):
    return TextureParam(param)
