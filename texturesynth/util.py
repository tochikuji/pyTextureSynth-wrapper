import numpy
import matlab
from texture_param import TextureParam


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
