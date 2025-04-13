from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestV4DeleteCustomer():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1CustomerIDCannotBeEmpty(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        element = self.driver.find_element(By.NAME, "AccSubmit")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id=\'message14\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message14\']")
        assert len(elements) > 0

    def test_test2CustomerIDMustBeNumeric(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id=\'message14\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message14\']")
        assert len(elements) > 0

    def test_test3CustomerIDNoSpecialCharacter(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id=\'message14\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message14\']")
        assert len(elements) > 0

    def test_test4CustomerIDNoBlankSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message14\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message14\']")
        assert len(elements) > 0

    def test_test5FirstCharacterCannotBeSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("space ")
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message14\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message14\']")
        assert len(elements) > 0

    def test_test6IncorrectCustomerID(self):

        # Fill wrong data in account number
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(741, 731)
        cusid = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "cusid")))
        cusid.clear()  # To clear input from previous tests
        cusid.send_keys("123456")
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
        assert alert.text == "Customer does not exist!!"


    def test_test7CorrectCustomerID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("95820")
        # self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(7) > div").click()
        self.driver.find_element(By.NAME, "AccSubmit").click()

    def test_test8ResetButton(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("qwerty 123")
        self.driver.find_element(By.NAME, "res").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id=\'message14\']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id=\'message14\']")
        assert len(elements) > 0

