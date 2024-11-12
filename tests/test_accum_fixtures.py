from source.accum import Accumulator
import pytest
from source.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()


def test_new_accum(accum):
    assert accum.count == 0


def test_add_counts(accum):
    accum.add_counts()
    assert accum.count == 1


def test_add_counts_twice(accum):
    accum.add_counts()
    accum.add_counts()
    assert accum.count == 2


def test_add_counts_with_params(accum):
    accum.add_counts(10)
    assert accum.count == 10


def test_add_counts_and_setter(accum):
    accum.count = 2
    accum.add_counts()
    assert accum.count == 3


def test_get_brand(accum):
    with pytest.raises(AttributeError) as err:
        print(accum.__brand)

    assert str(err.value) == "'Accumulator' object has no attribute '__brand'"
