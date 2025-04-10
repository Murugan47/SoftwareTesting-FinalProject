from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestV4DeleteAccount():
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

    def test_test2CustomerIDMustBeNumeric(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")

    def test_test3CustomerIDNoSpecialCharacter(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")

    def test_test4CustomerIDNoBlankSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")

    def test_test5FirstCharacterCannotBeSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("space ")
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")

    def test_test6IncorrectCustomerID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "AccSubmit").click()

    def test_test7CorrectCustomerID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("95820")
        self.driver.find_element(By.NAME, "AccSubmit").click()

    def test_test8ResetButton(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("qwerty 123")
        self.driver.find_element(By.NAME, "res").click()

