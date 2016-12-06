from toolz.functoolz import pipe
from toolz.curried import map
from functools import wraps
from abc import ABCMeta, abstractmethod

class Function(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, *args):
        pass

def register_functions():
    class Type():
        @classmethod
        def cm(cls):
            pass
        def m(self):
            pass
    t = Type()
    Function.register(type(lambda:None))    # add type `function`
    Function.register(type(len))            # add type `build in function`
    Function.register(type(t.m))            # add type `instance method`
    Function.register(type(t.cm))           # add type `class method`

register_functions()

def typecheck(*type_args, **type_kwargs):
    def _(f):
        @wraps(f)
        def __(*args, **kwargs):
            #checking args type
            if not pipe(zip(type_args, args),
                map(lambda t: issubclass(t[1].__class__, t[0])),
                all,
            ):
                raise TypeError("{} is not subclass {}".format(
                    ",".join(map(lambda arg: str(arg.__class__))(args)),
                    ",".join(map(lambda arg: str(arg))(type_args)))
                )
            #checking kwargs type
            item_types = type_kwargs.items()
            items = kwargs.items()
            if (len(item_types) != len(items) or
                not pipe(zip(item_types, items),
                    map(lambda x: x[0][0] == x[0][1] and # key check
                    issubclass(x[1][1].__class__, x[1][0])),
                    all,
                )
            ):
                raise TypeError()
            return f(*args, **kwargs)
        return __
    return _
