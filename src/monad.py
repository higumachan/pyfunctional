
from abc import ABCMeta, abstractmethod
from typeutil import typecheck, Function
from applicative_functor import ApplicativeFunctor

class Monad(ApplicativeFunctor):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @classmethod
    @typecheck(object, Function)
    def bind(cls, fn):
        return lambda x: cls.bind_detail(fn, x)

    @classmethod
    @abstractmethod
    def bind_detail(cls, fn, x):
        return cls.flatten(cls.map_detail(fn, x))

    @classmethod
    @abstractmethod
    def flatten(cls, x):
        return cls.bind_detail(lambda x: x, x)

    @classmethod
    def map_detail(cls, fn, a):
        return cls.bind_detail(lambda x: cls.unit(fn(x)), a)

    @classmethod
    def apply_detail(cls, fn, x):
        return cls.bind_detail(
            lambda f: cls.map_detail(lambda y: f(y), x),
            fn
        )
