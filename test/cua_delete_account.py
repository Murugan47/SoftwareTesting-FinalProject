import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDeleteAccountwithAssert():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1AccountNoCannotBeEmpty(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message2\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message2\']")
        assert len(elements) > 0

    def test_test2AccountNoMustBeNumeric(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message2\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message2\']")
        assert len(elements) > 0

    def test_test3AccountNoCantHaveSpecialCharacter(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message2\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message2\']")
        assert len(elements) > 0

    def test_test4AccountNoCantHaveBlankSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message2\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message2\']")
        assert len(elements) > 0

    def test_test5FirstCharacterCannotBeSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message2\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message2\']")
        assert len(elements) > 0

    def test_test6ValidAccount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("143932")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        assert self.driver.switch_to.alert.text == "Do you really want to delete this Account?"
        self.driver.switch_to.alert.accept()

    def test_test7InvalidAccountNo(self):
        # Fill wrong data in account number
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        account_no = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "accountno")))
        account_no.clear()  # To clear input from previous tests
        account_no.send_keys("3453453453535345")
        # Click on submit button
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, "AccSubmit"))).click()
        # Accepting the "Do you really want to delete this Account?" alert
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        # Catch the alert
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        # Assert
        assert alert.text == "Account does not exist"

    def test_test8ResetButton(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer 1234")
        self.driver.find_element(By.NAME, "res").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message2\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message2\']")
        assert len(elements) > 0

