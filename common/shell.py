#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 17:24
# @Author  : ChenYQ
# @Site    : 
# @File    : shell.py
# @Software: PyCharm



import subprocess


class Shell:
    '''执行shell命令'''
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
