# importing the tools I need from Selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestDefaultSuite():

    # runs before each test case — launches the browser
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    # runs after each test case — closes the browser
    def teardown_method(self, method):
        self.driver.quit()

    # test 1 — checking if the account number field shows an error when left empty
    def test_test1AccountNoCannotBeEmpty(self):
        # go to the Balance Enquiry page
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        # just resizing the window
        self.driver.set_window_size(744, 668)
        # clicking on the account number input field
        self.driver.find_element(By.NAME, "accountno").click()
        # pressing TAB key without typing anything (simulates leaving it blank)
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        # wait for the validation message to show up
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id='message2']")))
        # find the label element that shows the error message
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        # check that the error message actually appeared
        assert len(elements) > 0

    # test 2 — checking if letters + numbers are rejected
    def test_test2AccountNoMustBeNumeric(self):
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        self.driver.set_window_size(744, 648)
        self.driver.find_element(By.NAME, "accountno").click()
        # this time I'm entering letters and numbers (should be invalid)
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 3 — checking if special characters are not allowed
    def test_test3AccountNoCantHaveSpecialCharacter(self):
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        self.driver.set_window_size(844, 720)
        self.driver.find_element(By.NAME, "accountno").click()
        # typing in special characters
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 4 — checking if a space as the first character is rejected
    def test_test4FirstCharacterCannotBeBlank(self):
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        self.driver.set_window_size(844, 720)
        self.driver.find_element(By.NAME, "accountno").click()
        # entering just a space
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 5 — valid input (should not show any validation errors)
    def test_test5ValidAccount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        self.driver.set_window_size(844, 720)
        self.driver.find_element(By.NAME, "accountno").click()
        # entering a valid account number
        self.driver.find_element(By.NAME, "accountno").send_keys("143932")
        # submit the form
        self.driver.find_element(By.NAME, "AccSubmit").click()

    # test 6 — invalid account should trigger an alert
    def test_test6InValidAccount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        self.driver.set_window_size(741, 731)
        # wait until the input field is ready
        account_no = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "accountno")))
        # just making sure the field is empty before typing
        account_no.clear()
        # entering a fake/invalid account number
        account_no.send_keys("36363636")
        # submitting the form
        self.driver.find_element(By.NAME, "AccSubmit").click()
        # wait for the browser alert to show up
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        # switch to the alert popup
        alert = self.driver.switch_to.alert
        # checking if the message inside the alert is correct
        assert alert.text == "Account does not exist"

    # test 7 — clicking reset should clear the input and bring back the validation
    def test_test7ResetButton(self):
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")
        self.driver.set_window_size(844, 720)
        self.driver.find_element(By.NAME, "accountno").click()
        # typing something invalid first
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer 12345")
        # now clicking the reset button
        self.driver.find_element(By.NAME, "res").click()
        # wait to see if the validation message appears again
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0
