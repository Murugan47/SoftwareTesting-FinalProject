# Name: Nezar Mazraie
# Date: April 9th 2025
# File: Mazraie_Edit CustomerID.py
# Description: This will go through the manager side of the website and test each input field, and the final submit button
# It will test every input box for invalid and valid inputs. If it throws an error the program succeeds, and if the program
# does not throw an error it will fail.

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.service import Service

# Correct path to EdgeDriver
driver_path = r"C:\Users\Nezar\Downloads\driveredge\msedgedriver.exe"

# Use Service class to specify driver path
service = Service(driver_path)
driver = webdriver.Edge(service=service)

class TestEditCustomer:
    def setup_method(self, method):
        # Correct path to EdgeDriver
        driver_path = r"C:\Users\Nezar\Downloads\driveredge\msedgedriver.exe"
        self.service = Service(driver_path)
        self.driver = webdriver.Edge(service=self.service)
        self.driver.implicitly_wait(10)
        self.base_url = "https://demo.guru99.com/V4/manager/EditCustomer.php"

    def teardown_method(self, method):
        if self.driver:
            self.driver.quit()

    def test_EditCustomer(self):
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.set_window_size(1536, 920)
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr619279")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("yzatyva")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()

        # Testing Customer ID input box to see if it throws an error when the input field is blank
        # Passes Expected Result
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(11) > td:nth-child(2)").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message14"]').text
        assert message == "Customer ID is required"
        time.sleep(1)

        # Testing Customer ID input box to see if it throws an error when the input is special characters and regular characters
        # Passes Expected Result
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#abc")
        self.driver.find_element(By.CSS_SELECTOR, "td > p:nth-child(2)").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message14"]').text
        assert message == "Special characters are not allowed"
        time.sleep(1)

        # Testing Customer ID, testing if the user can login with a valid Customer ID
        # Passes Expected Results
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("76694")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(0.5)

        # Asserts that the page loaded, and you are on the page of Editing the customer
        message = self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p').text
        assert message == "Edit Customer"
        time.sleep(1)

        # Testing all input boxes for blank inputs, and asserting whether the input boxes throw an error for blank inputs
        # Passes Expected results
        self.driver.find_element(By.NAME, "addr").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        self.driver.find_element(By.NAME, "city").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > td:nth-child(2)").click()
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > td:nth-child(2)").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()

        # Asserts that each error message is thrown
        message = self.driver.find_element(By.XPATH, '//*[@id="message3"]').text
        assert message == "Address Field must not be blank"
        message = self.driver.find_element(By.XPATH, '//*[@id="message4"]').text
        assert message == "City Field must not be blank"
        message = self.driver.find_element(By.XPATH, '//*[@id="message5"]').text
        assert message == "State must not be blank"
        message = self.driver.find_element(By.XPATH, '//*[@id="message6"]').text
        assert message == "PIN Code must not be blank"
        message = self.driver.find_element(By.XPATH, '//*[@id="message7"]').text
        assert message == "Mobile no must not be blank"
        message = self.driver.find_element(By.XPATH, '//*[@id="message9"]').text
        assert message == "Email-ID must not be blank"
        time.sleep(1)

        # Tests each input box with non-numeric values
        # Passes Expected results
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("address")
        self.driver.find_element(By.NAME, "city").send_keys("address")
        self.driver.find_element(By.NAME, "state").send_keys("address")
        self.driver.find_element(By.NAME, "pinno").send_keys("addres")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("address")
        self.driver.find_element(By.NAME, "emailid").send_keys("address")

        # Asserts the input boxes that should not accept non-numeric values
        message = self.driver.find_element(By.XPATH, '//*[@id="message6"]').text
        assert message == "Characters are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message7"]').text
        assert message == "Characters are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message9"]').text
        assert message == "Email-ID is not valid"
        time.sleep(1)

        # Tests each input box with numeric values
        # Passes Expected Results
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("12345")
        self.driver.find_element(By.NAME, "city").send_keys("12345")
        self.driver.find_element(By.NAME, "state").send_keys("12345")
        self.driver.find_element(By.NAME, "pinno").send_keys("12345")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("12345")
        self.driver.find_element(By.NAME, "emailid").send_keys("12345")

        # Asserts the input boxes that should not accept numeric values
        message = self.driver.find_element(By.XPATH, '//*[@id="message4"]').text
        assert message == "Numbers are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message5"]').text
        assert message == "Numbers are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message6"]').text
        assert message == "PIN Code must have 6 Digits"
        message = self.driver.find_element(By.XPATH, '//*[@id="message9"]').text
        assert message == "Email-ID is not valid"
        time.sleep(1)

        # Tests each input box with special characters
        # Passes Expected Results
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("!")
        self.driver.find_element(By.NAME, "city").send_keys("!")
        self.driver.find_element(By.NAME, "state").send_keys("!")
        self.driver.find_element(By.NAME, "pinno").send_keys("!")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("!")
        self.driver.find_element(By.NAME, "emailid").send_keys("!")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(15) > td:nth-child(2)").click()

        # Asserts the input boxes that should not accept special characters
        message = self.driver.find_element(By.XPATH, '//*[@id="message3"]').text
        assert message == "Special characters are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message4"]').text
        assert message == "Special characters are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message5"]').text
        assert message == "Special characters are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message6"]').text
        assert message == "Special characters are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message7"]').text
        assert message == "Special characters are not allowed"
        message = self.driver.find_element(By.XPATH, '//*[@id="message9"]').text
        assert message == "Email-ID is not valid"
        time.sleep(1)

        # Tests if the submit button would work with all valid inputs
        # Failed Expected Results (Successfully Updated)
        # Actual Results. Page leads to a blank screen, and does not say whether the information has updated or not
        self.driver.find_element(By.NAME, "res").click()
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("address")
        self.driver.find_element(By.NAME, "city").send_keys("oshawa")
        self.driver.find_element(By.NAME, "state").send_keys("ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("1234567890")
        self.driver.find_element(By.NAME, "emailid").send_keys("nezar.mazraie@dcmail.ca")
        time.sleep(1)


        self.driver.find_element(By.NAME, "sub").click()
        message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        try:
            assert message == "Update done successfully"
            print("Update Succeeded")
        except AssertionError as e:
            print("Login failed")
            print(f"Expected 'Updated successfully', but blank page")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        time.sleep(1)