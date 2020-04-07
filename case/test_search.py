#!/usr/bin/env python
# encoding: utf-8
'''
@author:mikigo
@software:SeleniumTest
@file:test_register.py
@time:2020/1/15  16:18
@desc
'''
import os

import requests
import unittest
import ddt

from lib.util import hash_code, set_res_data
from model.setting import *


@ddt.ddt
class SearchTest(unittest.TestCase):

    @ddt.file_data(os.path.join(DATA_PATH,'search.yaml'))
    def test_search(self, **kwargs):
        # 获取参数值
        global resp
        url = kwargs.get("url")
        data = kwargs.get("data")
        check = kwargs.get("check")
        method = kwargs.get('method')
        jiami = kwargs.get('jiami')
        self._testMethodDoc = kwargs.get("detail")
        method = kwargs.get('method')
        jiami = kwargs.get('jiami')
        if jiami == True:
            if 'password' in data:
                data['password'] = hash_code(str(data['password']))
        if method.lower() == 'post':
            res = requests.post(url, data=data)
            resp = res.text
        elif method.lower() == 'get':
            res = requests.get(url, params=data)
            resp = res.text
        resp = set_res_data(resp)
        # 断言
        for i in check:
            self.assertIn(i, resp)


if __name__ == '__main__':
    unittest.main()
