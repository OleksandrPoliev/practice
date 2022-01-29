import pytest
# from python import Loopse
from python import NumberChenge
from unittest import TestCase
# class Testopp:
#     def test_data(self):
#         data= Loopse([x for x in range(10)])
#         assert data.loos()==[0,5]
#
#
#     def test_data_error(self):
#         data2 = Loopse([10, 4, 'str'])
#         with pytest.raises(TypeError):
#             assert data2.loos()==[0,5,10]




@pytest.fixture()
def prepareddata():
    Data=NumberChenge(0)
    yield Data
    Data=NumberChenge(0)


def test_data(prepareddata:NumberChenge):
    assert prepareddata.cheng_n()==6


def test_data_error(prepareddata:NumberChenge):
    prepareddata.__init__('f')
    with pytest.raises(TypeError):
            assert prepareddata.cheng_n()==6
