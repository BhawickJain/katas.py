import numpy as np  # type: ignore

from katas.add import add


###################
# Test: integers  #
###################


def test_integers_add():
    assert add(1, 2) == 3
