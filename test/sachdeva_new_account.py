import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SUCCESS_MESSAGE = "Passed successfully"
FAILURE_MESSAGE = "Failed"

class TestNewAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver instance before running any tests."""
        cls.driver = webdriver.Firefox() # Creating a firefox driver object
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/index.php") # Tells the browser to go specific website
        # Logs in the manager
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.NAME, "uid"))).send_keys("mngr619292")
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys("emadymA")
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin"))).click()

        # Clicks on new account
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".menusubnav > li:nth-child(5) > a:nth-child(1)"))).click()

    @classmethod
    def tearDownClass(cls):
        """Quit the WebDriver instance after all tests."""
        cls.driver.quit()

    def test1_empty_customer_id(self):
        # Select the customer_id field
        customer_id = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "cusid")))
        customer_id.clear()

        # Pressing TAB, to go the next field
        customer_id.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message14")))

        # Asserts the actual and expected message
        self.assertEqual("Customer ID is required", message.text)

        # Print successful message
        print(f"Test Case 1: Empty Customer ID - {SUCCESS_MESSAGE}")

    def test2_string_customer_id(self):
        # Select the customer_id field
        customer_id = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "cusid")))

        # Clear the customer_id field, so there's no text from previous testcase
        customer_id.clear()

        # Send string value
        customer_id.send_keys("12345six7890")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message14")))

        # Asserts the actual and expected message
        self.assertEqual("Characters are not allowed", message.text)

        # Print successful message
        print(f"Test Case 2: Customer ID with string - {SUCCESS_MESSAGE}")

    def test3_customer_id_with_special_characters(self):
        # Select the customer_id field
        customer_id = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "cusid")))

        # Clear the customer_id field, so there's no text from previous testcase
        customer_id.clear()

        # Send special character value
        customer_id.send_keys("!@#")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message14")))

        # Asserts the actual and expected message
        self.assertEqual("Special characters are not allowed", message.text)

        # Print successful message
        print(f"Test Case 3: Customer ID with special characters - {SUCCESS_MESSAGE}")

    def test4_customer_id_with_blank_expect_in_between(self):
        # Click on the customer_id field
        customer_id = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "cusid")))

        # Clear the customer_id field, so there's no text from previous testcase
        customer_id.clear()

        # Send input with first character blank
        customer_id.send_keys("12 456")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message14")))

        # Asserts the actual and expected message
        self.assertEqual("Characters are not allowed", message.text)

        # Print successful message
        print(f"Test Case 4: Customer ID with any character as blank, except the first one - {SUCCESS_MESSAGE}")

    def test5_customer_id_with_first_character_blank(self):
        # Select the customer_id field
        customer_id = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "cusid")))

        # Clear the customer_id field, so there's no text from previous testcase
        customer_id.clear()

        # Send value with first character blank
        customer_id.send_keys(" name")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message14")))

        # Asserts the actual and expected message
        self.assertEqual("First character cannot have space", message.text)

        try:
            # Print successful message
            print(f"Test Case 5: Customer ID with first character blank - {SUCCESS_MESSAGE}")
        except AssertionError as e:
            print(f"Test Case 5: Customer ID with first character blank - {FAILURE_MESSAGE}")
            raise e


if __name__ == "__main__":
    unittest.main(verbosity=2)