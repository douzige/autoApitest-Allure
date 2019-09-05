#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 17:22
# @Author  : ChenYQ
# @Site    : 
# @File    : TestClass.py
# @Software: PyCharm
from time import sleep

import allure
import pytest

from common.request import HttpUtils
from conf.test_evn import conf
from tools import calculate

@allure.feature("使用pytst+allure的demo-->算数运算")
class TestCalc(HttpUtils):
    '''测试加法用例'''
    # @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.fixture
    def foo(self):
        return 4;

    @allure.story("测试一个加法运算")
    @pytest.mark.parametrize('a,b,c,d',[(1,2,4,"用例描述1"),(2,4,6,"用例描述2"),(3,7,10,"用例描述3")])
    def test_add(self,a,b,c,d,foo):
        '''执行加法测试用例'''
        print(u''+d)
        # print("执行之前调用一次%d"%foo)
        sleep(1.1)
        result = calculate.add(a,b)
        # print("执行期间有调用一次%d"%foo)
        assert result == c
        # print("执行之后调用一次%d"%foo)

    @pytest.mark.skipif(condition=2>1,reason="我就是想测试skipif")
    @allure.story("测试一个加法运算,但是我准备跳过执行")
    def test_add_a(self):
        '''测试根据条件跳过这条用例'''
        result = calculate.add(100,100)
        assert result ==200

    @pytest.mark.xfail(condition= 2>1, reason="我就是想测试skipif")
    @allure.story("测试一个加法运算,但是我准备故意失败测试")
    def  test_add_b(self):
        '''测试根据条件故意失败用例'''
        result = calculate.add(100, 100)
        assert result == 200


if __name__ == '__main__':
    pytest.main('s test_calc.py')