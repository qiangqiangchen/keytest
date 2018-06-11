# -*- coding:utf-8 -*-

# Author : 陈强强

import helper
from xlsModel import readXls,readCase
from test_case import appium_test
'''
    1.读取excel ,逐行读取
    2.获取用例编号，按照编号构造执行函数
    3.用例管理
    3.获取结果写入测试用例
'''
def case_manage2():
    readexcel=readCase(r'F:\testcase.xlsx','Sheet2')
    step=readexcel.readDate()
    for i in step:
        print 'run %s'%i['case_name']
        app=appium_test()
        for s in i['case_step']:
            if app.test_run(s):
               pass
            else:
               print "%s test fail"%i['case_name']
               break
        app.tearDown()
        print "###########"


if __name__=='__main__':
    case_manage2()
    print 'done'