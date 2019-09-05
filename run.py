#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 19:57
# @Author  : ChenYQ
# @Site    : 
# @File    : run.py
# @Software: PyCharm
import allure
import pytest
from gevent import os

from common.shell import Shell

if __name__ == '__main__':


    va = pytest.main(["-q"])

    print(type(va))







    # shell = Shell()
    # result_path= os.getcwd()+"\\result"
    # report_path = os.getcwd()+'/report/'
    #
    # print(result_path)
    # args =[ '--alluredir', result_path]
    # pytest.main(args)
    # cmd = 'allure generate %s -o %s' % (result_path, report_path)

    # shell.invoke(cmd)






