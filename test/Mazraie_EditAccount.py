# Name: Nezar Mazraie
# Date: April 9th 2025
# File: test_edit_account.py
# Description: Tests each input field and the submit button on the Edit Account page

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

class TestEditAccount:
    @classmethod

    # This is just the initial login, if this fails everything else fails
    # This is not a test case
    def setup_class(cls):
        driver_path = r"C:\Users\Nezar\Downloads\driveredge\msedgedriver.exe"
        service = Service(driver_path)
        cls.driver = webdriver.Edge(service=service)
        cls.driver.implicitly_wait(10)
        cls.driver.set_window_size(1536, 920)
        cls.driver.get("https://demo.guru99.com/V4/index.php")
        cls.driver.find_element(By.NAME, "uid").send_keys("mngr619279")
        cls.driver.find_element(By.NAME, "password").send_keys("yzatyva")
        cls.driver.find_element(By.NAME, "btnLogin").click()
        cls.driver.find_element(By.LINK_TEXT, "Edit Account").click()

    @classmethod
    def teardown_class(cls):
        pass  # Don't close the driver unless you want to; remove this line to allow manual browser inspection

    # This tests each input box for a blank input and checks if it throws an error message
    # If it does, it will succeed, if it does not the test will fail
    def test_blank_input(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert message == "Account Number must not be blank"

    # This tests each input box for a non-numeric input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_non_numeric_input(self):
        self.driver.find_element(By.NAME, "accountno").clear()
        self.driver.find_element(By.NAME, "accountno").send_keys("abc123")
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert message == "Characters are not allowed"

    # This tests each input box for a special characters input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_special_characters(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("!@#$")
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert message == "Special characters are not allowed"

    # This tests each input box for a leading space input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_leading_space(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        self.driver.find_element(By.CSS_SELECTOR, "td > p:nth-child(2)").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert message in ["First character cannot have a space", "Characters are not allowed"]

    # This tests each input box for a space in the middle input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_internal_space(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("123 123")
        self.driver.find_element(By.CSS_SELECTOR, "td > p:nth-child(2)").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert message == "Characters are not allowed"

    # This tests each input box for a valid account number input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_valid_account_number(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("143849")
        message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        self.driver.find_element(By.NAME, "AccSubmit").click()
        try:
            assert message == "Login done successfully"
        except AssertionError:
            print("Login failed - Expected 'Login done successfully', but got:", message)
            raise

    # This tests each input box for a invalid input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_invalid_account_number_alert(self):
        self.driver.get("https://demo.guru99.com/V4/manager/editAccount.php")
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("4444444")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)