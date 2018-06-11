# -*- coding:utf-8 -*-

import unittest
from appium import webdriver
from time import sleep
import os
import helper

'''
    功能：
    初始化driver
    通过case_name来循环运行
    输出结果
    
'''

class appium_test(object):
    def __init__(self):
        os.popen("adb uninstall io.appium.android.ime") 
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'MXF0215826004374'
        #desired_caps['app'] = 'C:\\Users\\root\\Downloads\\app-release.apk'
        desired_caps['appPackage'] = 'tech.yunjing.biconlife'
        desired_caps['appActivity'] = 'tech.yunjing.biconlife.LaunchActivity'
        
        #启动appium的输入法
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    
    def test_run(self,step):
        try:
            return helper.runcase(self.driver,step)
        except:
            print 'test error,break'
            return False
    def tearDown(self):
        self.driver.quit()
        #卸载appium输入法
        os.popen("adb uninstall io.appium.android.ime")
        
        
if __name__=='__main__':
    app=appium_test()
    step_script1='XW_001,text,发现,click,2,contain,美食,,'
    step_script2='XW_001,text,新闻,click,2,id,tech.yunjing.biconlife:id/tv_ljtb_title,text:aaa,'
    try:
        app.test_run(step_script1)
        app.test_run(step_script2)
    finally:
        app.tearDown()
    print 'done'
