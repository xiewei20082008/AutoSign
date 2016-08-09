# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import sys
log = open('SignTemplate.log','a+')

class Vrfans():
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://bbs.itouzi.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_vrfans(self):
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [deleteAllVisibleCookies |  | ]]
        driver.get(self.base_url + "forum.php")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(sys.argv[1])
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(sys.argv[2])
        driver.find_element_by_id("loginSubBtn").click()
        driver.find_element_by_id("mn_plink_sign").click()
        try:
            if (u"您今日已签到" == driver.find_element_by_css_selector("li.yiqiandao").text):
                return True
        except Exception as e:
            print >>log, 'first check expection'
            log.close()
        driver.find_element_by_id("qd_btn").click()
        if (u"您今日已签到" == driver.find_element_by_css_selector("li.yiqiandao").text):
            self.driver.close()
            self.driver.quit()
            return True
        self.driver.close()
        self.driver.quit()
        return False

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    a = Vrfans()
    a.setUp()
    try:
        status = a.test_vrfans()
        if status:
            print 'OK'
        else:
            print 'Wrong'
    except Exception as e:
        print 'Wrong'
