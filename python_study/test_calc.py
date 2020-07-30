import pytest
from python_study.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    # 正整数加法
    def test_add_1(self):
        assert self.calc.add(1, 2) == 3

    # 负整数加法
    def test_add_2(self):
        assert self.calc.add(-1, -2) == -3

    # 正小数加法
    def test_add_3(self):
        assert round(self.calc.add(1.1, 2.2), 1) == 3.3

    # 负小数相加
    def test_add_4(self):
        assert round(self.calc.add(-1.1, -2.2), 1) == -3.3

    # 除数为0
    def test_div_1(self):
        try:
            self.calc.div(1, 0)
        except Exception as e:
            assert str(e) == "division by zero"

    # 正整数相除
    def test_div_2(self):
        assert self.calc.div(1, 2) == 0.5

    # 负整数相除
    def test_div_3(self):
        assert self.calc.div(-1, -2) == 0.5

    # 正小数相除
    def test_div_4(self):
        assert self.calc.div(0.1, 0.2) == 0.5

    # 负小数相除
    def test_div_5(self):
        assert self.calc.div(-0.1 / -0.2) == 0.5


if __name__ == '__main__':
    pytest.main("TestCalc")
