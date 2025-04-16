import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestCustomizedStatement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver instance before running any tests."""
        cls.driver = webdriver.Firefox() # Creating a firefox driver object
        cls.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php") # Tells the browser to go specific website
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        """Quit the WebDriver instance after all tests."""
        cls.driver.quit()

    def test_cS1(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).send_keys(Keys.TAB)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS2(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("1234acc123")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS3(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("123!@#!@#")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
        assert check == "Special characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS4(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("123 12")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".heading3"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS5(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody:nth-child(1) > tr:nth-child(1) > td"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys(" ")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message2"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("  ")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS6(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "fdate"))).click()
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message26"]'))).text
        assert check == "From Date Field must not be blank"

    def test_cS7(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "tdate"))).click()
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message27"]'))).text
        assert check == "From Date Field must not be blank"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS8(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).send_keys("1234Acc123")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message12"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS9(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).send_keys("123!@#")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message12"]'))).text
        assert check == "Special characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS10(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).send_keys("123 12")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message12"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS11(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).send_keys(" ")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message12"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS12(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).send_keys("1234Acc123")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message13"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS13(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).send_keys("123!@#")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message13"]'))).text
        assert check == "Number of Transaction cannot have special character"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS14(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).send_keys("123 12")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message13"]'))).text
        assert check == "Characters are not allowed"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS15(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).send_keys(" ")
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="message13"]'))).text
        assert check == "There is no error message"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"

    def test_cS16(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("12345")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody:nth-child(1) > tr:nth-child(1) > td"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "fdate"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "fdate"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "fdate"))).send_keys("2000-01-01")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "tdate"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "tdate"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "tdate"))).send_keys("2000-02-02")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).send_keys("2")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).send_keys("1")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "res"))).click()
        check = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).get_attribute("value")
        assert check == ""

    def test_CS17(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "accountno"))).send_keys("52793")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "fdate"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "fdate"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "fdate"))).send_keys("2025-05-12")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "tdate"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "tdate"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "tdate"))).send_keys("2026-01-02")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "amountlowerlimit"))).send_keys("34000")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "numtransaction"))).send_keys("1")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(2)"))).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "AccSubmit"))).click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Please fill all fields"
