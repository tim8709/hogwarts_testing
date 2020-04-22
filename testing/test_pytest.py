from python.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    '''
    1.正数相加
    2.负数相加
    3.小数相加
    4.0相加    
    '''

    @pytest.mark.parametrize("a,b,result", [
        (1, 2, 3),
        (-1, -2, -3),
        (0.1, 0.2, 0.3),
        (0, 0, 0)
    ])
    def test_add(self, a, b, result):
        assert (self.calc.add(a, b), result)

    '''
    1.正数相除
    2.负数相除
    3.小数相除
    4.除以0
    '''

    @pytest.mark.parametrize("a,b,result", [
        (1, 2, 0.5),
        (-1, -2, 0.5),
        (0.1, 0.2, 0.5),
        (1, 0, "error")
    ])
    def test_div(self, a, b, result):
        assert (self.calc.div(a, b), result)
