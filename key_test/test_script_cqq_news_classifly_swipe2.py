# -*- coding:utf-8 -*-
# Author : 陈强强
#TestCase: 新闻-新闻分类-查看未显示的新闻分类
#TestResult:1.可以看到未显示的新闻分类
#DateTime: 2018-3-14

import unittest
from appium import webdriver
from time import sleep
import os
import helper

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

#延时时间
T = 2

class test_script(unittest.TestCase):
    
    def setUp(self):    
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
        
        

    def tearDown(self):
        self.driver.quit()
        #卸载appium输入法
        os.popen("adb uninstall io.appium.android.ime")
        
        
        
    
    def test_script(self):
        print 'start test'
        #载入测试计划
        f=open(r"F:\test.csv",'r')
        case=f.readlines()
        f.close()
        #print len(case)
        sleep(10)
        for line in case:
            helper.runcase(self.driver,line)

            
     
        
def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(test_script)
    unittest.TextTestRunner(verbosity=2).run(suite) 
           
if __name__ == '__main__':
    run()
    