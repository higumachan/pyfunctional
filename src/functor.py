
from abc import ABCMeta, abstractmethod

class Functor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, value):
        pass

    @classmethod
    @abstractmethod
    def unit(cls, x):
        pass

    @classmethod
    def map(cls, fn):
        return lambda x: cls.map_detail(fn, x)

    @classmethod
    @abstractmethod
    def map_detail(cls,fn, a):
        pass
