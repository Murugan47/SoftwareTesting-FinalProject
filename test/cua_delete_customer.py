from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestV4DeleteCustomer():

    # this runs before each test — launches Firefox browser
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    # this runs after each test — closes the browser
    def teardown_method(self, method):
        self.driver.quit()

    # test 1 — should show error if customer ID is empty
    def test_test1CustomerIDCannotBeEmpty(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        # simulate click and hold on the submit button (weird interaction but site expects it)
        element = self.driver.find_element(By.NAME, "AccSubmit")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        # move to the label area before releasing click
        element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)").click()
        # wait for the error message for empty input
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id='message14']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message14']")
        assert len(elements) > 0

    # test 2 — typing letters and numbers should be invalid
    def test_test2CustomerIDMustBeNumeric(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id='message14']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message14']")
        assert len(elements) > 0

    # test 3 — special characters should not be accepted
    def test_test3CustomerIDNoSpecialCharacter(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id='message14']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message14']")
        assert len(elements) > 0

    # test 4 — input with a blank space in the middle should trigger validation
    def test_test4CustomerIDNoBlankSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message14']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message14']")
        assert len(elements) > 0

    # test 5 — space as the first character is invalid
    def test_test5FirstCharacterCannotBeSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        # entering space before a valid ID
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message14']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message14']")
        assert len(elements) > 0

    # test 6 — trying to delete a customer ID that doesn't exist
    def test_test6IncorrectCustomerID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(741, 731)
        # wait until field is ready
        cusid = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "cusid")))
        cusid.clear()
        cusid.send_keys("123456")
        # click submit
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, "AccSubmit"))).click()
        # first alert: confirm delete
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        # second alert: customer doesn’t exist
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        # check if correct error message shows up
        assert alert.text == "Customer does not exist!!"

    # test 7 — successful path with a correct customer ID
    def test_test7CorrectCustomerID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("95820")
        # submit the form — confirmation alert expected here (no assertion needed for this test)
        self.driver.find_element(By.NAME, "AccSubmit").click()

    # test 8 — clicking reset should clear the invalid input
    def test_test8ResetButton(self):
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.NAME, "cusid").click()
        # enter invalid input
        self.driver.find_element(By.NAME, "cusid").send_keys("qwerty 123")
        # click reset to clear field
        self.driver.find_element(By.NAME, "res").click()
        # wait for validation to show again
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message14']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message14']")
        assert len(elements) > 0
