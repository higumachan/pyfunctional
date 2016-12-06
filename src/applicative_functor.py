
from abc import ABCMeta, abstractmethod
from functor import Functor
from typeutil import typecheck, Function

class ApplicativeFunctor(Functor):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    @typecheck(object, Functor)
    def apply(cls, afn):
        if not issubclass(afn.__class__, cls):
            raise TypeError
        return lambda x: cls.apply_detail(afn, x)

    @classmethod
    def map2(cls, fn):
        return lambda x, y: cls.map2_detail(fn, x, y)

    @classmethod
    def traverse(cls, fn):
        return lambda xs: cls.traverse_detail(fn, xs)

    @classmethod
    @typecheck(object, list)
    def sequence(cls, xs):
        return reduce(
            lambda acc, x: cls.map2_detail(
                lambda y, z: y + z, acc, x
            ),
            xs,
            cls.unit([])
        )

    @classmethod
    @abstractmethod
    @typecheck(object, Function, Functor)
    def apply_detail(cls, afn, a):
        cls.map2_detail(lambda fn, x: fn(x), afn, a)

    @classmethod
    @typecheck(object, Function, Functor)
    def map_detail(cls, fn, a):
        return cls.apply_detail(cls.unit(fn), a)

    @classmethod
    @typecheck(object, Function, Functor, Functor)
    def map2_detail(cls, fn, a, b):
        cls.map_detail(lambda x: (lambda y: fn(x, y)), a)
        return cls.apply_detail(
            cls.map_detail(lambda x: (lambda y: fn(x, y)), a),
            b
        )

    @classmethod
    @typecheck(object, Function, list)
    def traverse_detail(cls, fn, xs):
        return reduce(lambda acc, x: cls.map2_detail(lambda y, z: z + y, fn(x), acc),
            xs,
            cls.unit([])
        )
