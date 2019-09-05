#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 19:59
# @Author  : ChenYQ
# @Site    : 
# @File    : request.py
# @Software: PyCharm


import sys,json,re,requests,os

class  HttpUtils(object):
    '''request 封装'''
    def http_req(seif,method, url, params=None, json_data=None, cookies=None,
                      headers=None, responseStatus=None, des=None):
        print(u'***********************测试数据日志***********************')
        err_msg = ''
        if des:
            print("【测试目的】：%s" % (des))
        if len(url)>0:
            print(u'【请求方法:%s】 %s' % (method, url))
        if headers != None or headers == '':
            print(u'【header】：%s' % (json.dumps(headers, indent=4)))
        if cookies != None or cookies == '':
            print(u'【cookies】：%s' % (json.dumps(cookies, indent=4)))
        if params != None and params == '':
            try:
                print(u'【Form参数】：')
                print("\t",json.dumps(params, indent=4, ensure_ascii=False))
            except Exception as e:
                err_msg += '参数json格式化异常：%s\n' % e
                print(params)

        if json_data != None or json_data == '':
            try:
                print(u'【Json参数】：')
                print("\t",json.dumps(json_data, indent=4, ensure_ascii=False))

            except Exception as e:
                err_msg += '参数json格式化异常：%s\n' % e
                print(json_data)
        for i in range(3):
            try:
                if method == "post":
                    order = 'requests.' + method + '(\'' + url + '\',json= json_data,data=params,headers=headers,cookies=cookies,timeout=10,verify = False)'
                else:
                    order = 'requests.' + method + '(\'' + url + '\',json= json_data,params=params,headers=headers,cookies=cookies,timeout=10,verify = False)'
                # print(order)
                response = eval(order)
                break
            except Exception as e:
                print("访问异常：%s\n" % e)
                continue
        try:
            print(u'【响应状态】： %s' % (response.status_code))
        except:
            raise Exception(u'接口访问异常信息：%s' % err_msg)
        try:
            responseValue = response.json()
        except Exception as e:
            err_msg += '响应结果提取json返回值异常：%s\n' % e
            responseValue = response.text
            print(u'【响应内容】：\n', responseValue)
        else:
            print(u'【响应内容】：')
            print("\t",json.dumps(responseValue, indent=4, ensure_ascii=False))
        if responseStatus != None and responseStatus != '':
            try:
                assert response.status_code == responseStatus
            except Exception as e:
                err_msg += '响应码校验异常：%s\n' % e
                raise Exception(u"响应状态码与预期不符,【预期】：%s,【实际】：%s" % (responseStatus, response.status_code))
            finally:
                print('执行期间抛出如下异常：%s' % err_msg)
        return responseValue
