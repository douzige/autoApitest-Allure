#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 17:29
# @Author  : ChenYQ
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
import sys

import pytest
from gevent import os

presentPath = os.getcwd()
print(presentPath)
sys.path.append(presentPath)
from conf.test_evn import conf
'''
设置在本包下fixture 的作用范围在本包下
'''

