from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestDeleteAccountwithAssert():

    # this runs before every test — opens Firefox
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    # this runs after every test — closes the browser
    def teardown_method(self, method):
        self.driver.quit()

    # test 1 — check if account number field shows error when left empty
    def test_test1AccountNoCannotBeEmpty(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        # wait for validation message
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 2 — make sure non-numeric input gets rejected
    def test_test2AccountNoMustBeNumeric(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        # validation message check (same as test 1)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 3 — entering special characters should trigger validation
    def test_test3AccountNoCantHaveSpecialCharacter(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        # rest is same as before (check validation)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 4 — blank spaces inside input should be invalid
    def test_test4AccountNoCantHaveBlankSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 5 — if the first character is a space, should be rejected
    def test_test5FirstCharacterCannotBeSpace(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        # actually typing a space
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[@id='message2']")))
        elements = self.driver.find_elements(By.XPATH, "//label[@id='message2']")
        assert len(elements) > 0

    # test 6 — if the account number is valid, alert should ask to confirm deletion
    def test_test6ValidAccount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        # typing a valid account number
        self.driver.find_element(By.NAME, "accountno").send_keys("143932")
        # clicking submit
        self.driver.find_element(By.NAME, "AccSubmit").click()
        # assert that the correct alert message shows up
        assert self.driver.switch_to.alert.text == "Do you really want to delete this Account?"
        # accept the alert to proceed
        self.driver.switch_to.alert.accept()

    # test 7 — trying to delete an invalid account number
    def test_test7InvalidAccountNo(self):
        # open the delete account page
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        # wait for the field to load before interacting
        account_no = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "accountno")))
        # clear any leftover input
        account_no.clear()
        # typing a fake/invalid account number
        account_no.send_keys("3453453453535345")
        # clicking submit
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, "AccSubmit"))).click()
        # first alert asks for confirmation
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        # second alert tells us that the account doesn’t exist
        WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        # now we check if the alert message is correct
        assert alert.text == "Account does not exist"

    # test 8 — hitting reset should clear the invalid input
    def test_test8ResetButton(self):
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")
        self.driver.set_window_size(741, 731)
        self.driver.find_element(By.NAME, "accountno").click()
        # type some invalid text
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer 1234")
        # click the reset button
        self.driver.find_element(By.NAME, "res").click()
        # check if the validation message comes back
        WebDriverWait(self.driver, 30).until
