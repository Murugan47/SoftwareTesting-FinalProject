# Name: Nezar Mazraie
# Date: April 9th 2025
# File: Mazraie_Edit CustomerID.py
# Description: This will go through the manager side of the website and test each input field, and the final submit button
# It will test every input box for invalid and valid inputs. If it throws a valid error the program succeeds, if not the
# website will need some adjustments

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver_path = r"C:\Users\Nezar\Downloads\driveredge\msedgedriver.exe"

class TestEditCustomer:
    @classmethod
    def setup_class(cls):
        cls.service = Service(driver_path)
        cls.driver = webdriver.Edge(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://demo.guru99.com/V4/index.php")
        cls.driver.set_window_size(1536, 920)
        cls.driver.find_element(By.NAME, "uid").send_keys("mngr619279")
        cls.driver.find_element(By.NAME, "password").send_keys("yzatyva")
        cls.driver.find_element(By.NAME, "btnLogin").click()
        cls.driver.find_element(By.LINK_TEXT, "Edit Customer").click()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # This tests each input box for a blank input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_blank_customer_id(self):
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(11) > td:nth-child(2)").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message14"]').text
        assert message == "Customer ID is required"

    # This tests each input box for a special character input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_special_char_customer_id(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#abc")
        self.driver.find_element(By.CSS_SELECTOR, "td > p:nth-child(2)").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message14"]').text
        assert message == "Special characters are not allowed"

    # This tests each input box for a valid input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_valid_customer_id_loads_page(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").send_keys("76694")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        message = self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p').text
        assert message == "Edit Customer"

    # This tests each input box for a blank inputs and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_blank_fields_throw_errors(self):
        fields = ["addr", "city", "state", "pinno", "telephoneno", "emailid"]
        for field in fields:
            self.driver.find_element(By.NAME, field).clear()
            self.driver.find_element(By.NAME, field).click()
            self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        assert self.driver.find_element(By.XPATH, '//*[@id="message3"]').text == "Address Field must not be blank"
        assert self.driver.find_element(By.XPATH, '//*[@id="message4"]').text == "City Field must not be blank"
        assert self.driver.find_element(By.XPATH, '//*[@id="message5"]').text == "State must not be blank"
        assert self.driver.find_element(By.XPATH, '//*[@id="message6"]').text == "PIN Code must not be blank"
        assert self.driver.find_element(By.XPATH, '//*[@id="message7"]').text == "Mobile no must not be blank"
        assert self.driver.find_element(By.XPATH, '//*[@id="message9"]').text == "Email-ID must not be blank"

    # This tests each input box for a non-numeric inputs and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_non_numeric_values(self):
        self.driver.find_element(By.NAME, "addr").clear()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "emailid").clear()

        self.driver.find_element(By.NAME, "addr").send_keys("address")
        self.driver.find_element(By.NAME, "city").send_keys("address")
        self.driver.find_element(By.NAME, "state").send_keys("address")
        self.driver.find_element(By.NAME, "pinno").send_keys("addres")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("address")
        self.driver.find_element(By.NAME, "emailid").send_keys("address")

        assert self.driver.find_element(By.XPATH, '//*[@id="message6"]').text == "Characters are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message7"]').text == "Characters are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message9"]').text == "Email-ID is not valid"

    # This tests each input box for a numeric inputs and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_numeric_values(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "addr").clear()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "emailid").clear()

        self.driver.find_element(By.NAME, "addr").send_keys("12345")
        self.driver.find_element(By.NAME, "city").send_keys("12345")
        self.driver.find_element(By.NAME, "state").send_keys("12345")
        self.driver.find_element(By.NAME, "pinno").send_keys("12345")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("12345")
        self.driver.find_element(By.NAME, "emailid").send_keys("12345")

        assert self.driver.find_element(By.XPATH, '//*[@id="message4"]').text == "Numbers are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message5"]').text == "Numbers are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message6"]').text == "PIN Code must have 6 Digits"
        assert self.driver.find_element(By.XPATH, '//*[@id="message9"]').text == "Email-ID is not valid"

    # This tests each input box for a special characters input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_special_characters(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "addr").clear()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "emailid").clear()

        self.driver.find_element(By.NAME, "addr").send_keys("!")
        self.driver.find_element(By.NAME, "city").send_keys("!")
        self.driver.find_element(By.NAME, "state").send_keys("!")
        self.driver.find_element(By.NAME, "pinno").send_keys("!")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("!")
        self.driver.find_element(By.NAME, "emailid").send_keys("!")

        assert self.driver.find_element(By.XPATH, '//*[@id="message3"]').text == "Special characters are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message4"]').text == "Special characters are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message5"]').text == "Special characters are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message6"]').text == "Special characters are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message7"]').text == "Special characters are not allowed"
        assert self.driver.find_element(By.XPATH, '//*[@id="message9"]').text == "Email-ID is not valid"

    # This tests each input box for a valid input and checks if it throws an error message
    # If it does it will succeed, if it does not the test will fail
    def test_valid_submit(self):
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "addr").clear()
        self.driver.find_element(By.NAME, "city").clear()
        self.driver.find_element(By.NAME, "state").clear()
        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "telephoneno").clear()
        self.driver.find_element(By.NAME, "emailid").clear()

        self.driver.find_element(By.NAME, "addr").send_keys("address")
        self.driver.find_element(By.NAME, "city").send_keys("oshawa")
        self.driver.find_element(By.NAME, "state").send_keys("ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("1234567890")
        self.driver.find_element(By.NAME, "emailid").send_keys("nezar.mazraie@dcmail.ca")
        self.driver.find_element(By.NAME, "sub").click()

        try:
            message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
            assert message == "Update done successfully"
        except AssertionError as e:
            pytest.fail("Expected 'Update done successfully', but got blank or failed result.")
            raise e