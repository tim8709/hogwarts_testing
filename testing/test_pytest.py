import yaml

from calc.calc import Calc
import pytest


def data():
    with open("test_pyteset_data.yaml") as f:
        return yaml.load(f)


class TestCalc:
    def setup(self):
        self.calc = Calc()

    '''
    1.正数相加
    2.负数相加
    3.小数相加
    4.0相加    
    '''

    # @pytest.mark.parametrize("a,b,result", [
    #     (1, 2, 3),
    #     (-1, -2, -3),
    #     (0.1, 0.2, 0.3),
    #     (0, 0, 0)
    # ])
    @pytest.mark.parametrize("a,b,result", data())
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

#
# def setup_module():
#     pass
#
#
# def teardown_module():
#     pass


# class TestCase:
#     @classmethod
#     def setup_class(cls):
#         cls.calc = Calc()
#
#     @pytest.mark.demo1
#     def test_case(self):
#         assert (self.calc.add(1, 2), 3)
#
#     @pytest.mark.demo2
#     def test_case1(self):
#         assert (self.calc.div(1, 2), 0.5)
#
#     def setup(self):
#         pass
#
#     def teardown(self):
#         pass
