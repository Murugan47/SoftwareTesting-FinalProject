# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMiniStatement():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_mS1(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("")
    check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
    assert check == "Account Number must not be blank"
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "Please fill all fields"

  def test_mS2(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("1234Acc123")
    check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
    assert check == "Characters are not allowed"
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "Please fill all fields"

  def test_mS3(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("123!@#!@#")
    check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
    assert check == "Special characters are not allowed"
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "Please fill all fields"

  def test_mS4(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("123 12")
    check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
    assert check == "Special characters are not allowed"
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "Please fill all fields"

  def test_mS5(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys(" ")
    check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
    assert check == "First character cannot have space"
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "Please fill all fields"

  def test_mS6(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("52793")
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()

  def test_mS7(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("12345")
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "Account does not exist"

  def test_mS8(self):
    self.driver.get("https://demo.guru99.com/V4/manager/MiniStatementInput.php")
    self.driver.set_window_size(619, 695)
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("qwer 12345")
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "res"))).click()
    check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).get_attribute(
      "value")
    assert check == ""
    self.driver.close()
