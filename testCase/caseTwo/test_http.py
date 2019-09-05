#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 19:14
# @Author  : ChenYQ
# @Site    : 
# @File    : test_http.py
# @Software: PyCharm
import allure
import pytest

from common.request import HttpUtils
from conf.test_evn import conf



@allure.feature("使用pytst+allure的demo-->http请求")
class  TestHttp(HttpUtils):
    @allure.story("测试一个http的get请求")
    def test_req(self, init):
        '''测试http请求情况！'''
        result = self.http_req("get", url=init[0] + "/demo/get/1", des="测试测试用例运行情况!")
        # print(result)

    @allure.story("测试一个http post请求")
    @pytest.mark.parametrize('flag,data,des', [(1, {"userName": "admin", "passWord": "123456"}, "正确的账号密码"),
                                               (2, {"userName": "admin", "passWord": "12345"}, "错误的账号密码")])
    def test_post_def(self, flag, data, des, init):
        headers = {"Content-Type": "application/json"}
        result = self.http_req("post", url=init[0] + "/demo/update", json_data=data, des=des, headers=init[1])

    @pytest.fixture(scope='class')
    def init(self):
        evn = conf.server["host"]
        header = {"content-type": "application/json"}
        return (evn, header)