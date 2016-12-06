from unittest import TestCase
from nose.tools import eq_, ok_
from src.list import List
from src.monad import Monad
from src.applicative_functor import ApplicativeFunctor
from src.functor import Functor

class ListMonadTest(TestCase):
    def test_type(self):
        print List([1, 2, 3])
        ok_(isinstance(List([1,2,3]), List))
        ok_(issubclass(List([1,2,3]).__class__, Monad))
        ok_(issubclass(List([1,2,3]).__class__, ApplicativeFunctor))
        ok_(issubclass(List([1,2,3]).__class__, Functor))

    def test_map(self):
        l = List([1, 2, 3])
        eq_(List.map(lambda x: x + 1)(l).to_pylist(), [2, 3, 4])
        eq_(List.map(lambda x: x * 2)(l).to_pylist(), [2, 4, 6])
        eq_(List.map(lambda x: x * 2)(List([[1], [2], [3]])).to_pylist(), [[1, 1], [2, 2], [3, 3]])

    def test_bind(self):
        l = List([1, 2, 3])
        eq_(List.bind(lambda x: List([x + 1, x + 2, x + 3]))(l).to_pylist(),
            [2, 3, 4, 3, 4 ,5, 4, 5, 6])

    def test_apply(self):
        fns = List([lambda x: x * 1, lambda x: x * 2, lambda x: x * 3])
        xs = List.unit(1)
        xs2 = List([1, 2])

        print type(fns)
        eq_(List.apply(fns)(xs).to_pylist(), [1, 2, 3])
        eq_(List.apply(fns)(xs2).to_pylist(), [1, 2, 2, 4, 3, 6])

    def test_map2(self):
        xs1 = List([0, 1])
        xs2 = List([1, 2])
        eq_(List.map2(lambda x, y: x + y)(xs1, xs2).to_pylist(), [1, 3])
