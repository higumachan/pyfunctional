
from abc import ABCMeta
from monad import Monad

class List(Monad):
    __metaclass__ = ABCMeta

    def __init__(self, value):
        self.value = value

    def to_pylist(self):
        return self.value

    @classmethod
    def bind_detail(cls, fn, x):
        print x.to_pylist()
        print map(lambda x: x.to_pylist(), map(fn, x.value))
        return List(sum(map(lambda x: x.to_pylist(), map(fn, x.value)), []))

    @classmethod
    def unit(cls, x):
        return List([x])
