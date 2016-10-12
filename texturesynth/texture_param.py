"""
TextureParam
===

steerable pyramid texture parameters

"""

from util import ml2np


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
