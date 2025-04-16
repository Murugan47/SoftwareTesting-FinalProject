import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
        print(f"Test Case 2: Customer ID containing letters - {SUCCESS_MESSAGE}")

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
        # Select customer_id field
        customer_id = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "cusid")))

        # Clear the customer_id field, so there's no text from previous testcase
        customer_id.clear()

        # Send input with a space in between
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

        # Send input where the first character is a space
        customer_id.send_keys(" name")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message14")))

        try:
            # Asserts the actual and expected message
            self.assertEqual("First character cannot have space", message.text)
            # Print successful message
            print(f"Test Case 5: Customer ID with first character blank - {SUCCESS_MESSAGE}")
        except AssertionError as e:
            print(f"Test Case 5: Customer ID with first character blank - {FAILURE_MESSAGE}")
            raise e

    def test6_empty_initial_deposit(self):
        # Select the initial_deposit field
        initial_deposit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "inideposit")))
        initial_deposit.clear()

        # Pressing TAB, to go the next field
        initial_deposit.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message19")))

        # Asserts the actual and expected message
        self.assertEqual("Initial Deposit must not be blank", message.text)

        # Print successful message
        print(f"Test Case 6: Empty initial deposit - {SUCCESS_MESSAGE}")

    def test7_string_initial_deposit(self):
        # Select the initial_deposit field
        initial_deposit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "inideposit")))

        # Clear the initial_deposit field, so there's no text from previous testcase
        initial_deposit.clear()

        # Send string value
        initial_deposit.send_keys("45six")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message19")))

        # Asserts the actual and expected message
        self.assertEqual("Characters are not allowed", message.text)

        # Print successful message
        print(f"Test Case 7: Initial Deposit containing letters - {SUCCESS_MESSAGE}")

    def test8_initial_deposit_with_special_characters(self):
        # Select the initial_deposit field
        initial_deposit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "inideposit")))

        # Clear the initial_deposit field, so there's no text from previous testcase
        initial_deposit.clear()

        # Send special character value
        initial_deposit.send_keys("!@#")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message19")))

        # Asserts the actual and expected message
        self.assertEqual("Special characters are not allowed", message.text)

        # Print successful message
        print(f"Test Case 8: Initial deposit with special characters - {SUCCESS_MESSAGE}")

    def test9_initial_deposit_with_space_in_between(self):
        # Click on the initial_deposit field
        initial_deposit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "inideposit")))

        # Clear the initial_deposit field, so there's no text from previous testcase
        initial_deposit.clear()

        # Send input with a space in between
        initial_deposit.send_keys("12 456")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message19")))

        try:
            # Asserts the actual and expected message
            self.assertEqual("Special characters are not allowed", message.text)
            # Print successful message
            print(f"Test Case 9: Initial deposit with any character as blank, except the first one - {SUCCESS_MESSAGE}")
        except AssertionError as e:
            print(f"Test Case 9: Initial deposit with any character as blank, except the first one - {FAILURE_MESSAGE}")
            raise e


    def test10_initial_deposit_with_first_character_blank(self):
        # Select the initial_deposit field
        initial_deposit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "inideposit")))

        # Clear the initial_deposit field, so there's no text from previous testcase
        initial_deposit.clear()

        # Send value with first character blank
        initial_deposit.send_keys(" 548")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message19")))

        try:
            # Asserts the actual and expected message
            self.assertEqual("First character cannot have space", message.text)
            # Print successful message
            print(f"Test Case 10: Initial Deposit with first character blank - {SUCCESS_MESSAGE}")
        except AssertionError as e:
            print(f"Test Case 10: Initial Deposit with first character blank - {FAILURE_MESSAGE}")
            raise e

    def test11_select_savings(self):
        # Selects the account type dropdown
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "selaccount")))

        # Click on the account type drop down
        dropdown_element.click()

        # Create an instance of Select class
        dropdown = Select(dropdown_element)

        # Now select savings by visible text
        dropdown.select_by_visible_text("Savings")

        # Get the selected option
        selected_value = dropdown.first_selected_option

        # Asserts the actual and expected message
        self.assertEqual("Savings", selected_value.text)

        # Print successful message
        print(f"Test Case 11: Selecting savings account type - {SUCCESS_MESSAGE}")

    def test12_select_current(self):
        # Selects the account type dropdown
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "selaccount")))

        # Click on the account type drop down
        dropdown_element.click()

        # Create an instance of Select class
        dropdown = Select(dropdown_element)

        # Now select savings by visible text
        dropdown.select_by_visible_text("Current")

        # Get the selected option
        selected_value = dropdown.first_selected_option

        # Asserts the actual and expected message
        self.assertEqual("Current", selected_value.text)

        # Print successful message
        print(f"Test Case 12: Selecting current account type - {SUCCESS_MESSAGE}")

    def test13_reset_button(self):
        # Fill sample data in customer id and initial deposit
        customer_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "cusid")))
        customer_id.clear()
        customer_id.send_keys("qwer")
        initial_deposit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "inideposit")))
        initial_deposit.clear()
        initial_deposit.send_keys("123456")

        # Click on reset button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "reset"))).click()

        # Assert if both customer_id and initial_deposit gets cleared out
        self.assertEqual("", customer_id.text)
        self.assertEqual("", initial_deposit.text)

        # Print successful message
        print(f"Test Case 13: Reset button - {SUCCESS_MESSAGE}")

    def test14_submit_with_wrong_cus_id(self):
        # Fill wrong data in customer id
        customer_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "cusid")))
        customer_id.clear() # To clear input from previous tests
        customer_id.send_keys("123456")

        # Click on submit button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "button2"))).click()

        # Catch the alert
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert


        try:
            # Assert the alert text
            self.assertEqual("Customer does not exist!!", alert.text)
            print(f"Test Case 14: Submit with wrong customer id - {SUCCESS_MESSAGE}")
        except AssertionError as e:
            print(f"Test Case 14: Submit with wrong customer id - {FAILURE_MESSAGE}")
            raise e

    def test15_submit_with_right_data(self):
        # Fill correct customer id
        customer_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "cusid")))
        customer_id.clear() # To clear input from previous tests
        customer_id.send_keys("36868")
        # Fill correct initial deposit
        initial_deposit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "inideposit")))
        initial_deposit.clear() # To clear input from previous tests
        initial_deposit.send_keys("1000")

        # Click on submit button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "button2"))).click()

        # Get the result
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "heading3")))

        # Asserts the actual and expected message
        self.assertEqual("Account Generated Successfully!!!", message.text)

        print(f"Test Case 15: Creating a new account - {SUCCESS_MESSAGE}")

class TestNewAccountRedirection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver instance before running any tests."""
        cls.driver = webdriver.Firefox()  # Creating a firefox driver object
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/index.php")  # Tells the browser to go specific website
        # Logs in the manager
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.NAME, "uid"))).send_keys("mngr619292")
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys("emadymA")
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin"))).click()

        # Clicks on new account
        WebDriverWait(cls.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".menusubnav > li:nth-child(5) > a:nth-child(1)"))).click()

    @classmethod
    def tearDownClass(cls):
        """Quit the WebDriver instance after all tests."""
        cls.driver.quit()

    def test16_continue_after_account_creation(self):
        # Fill correct customer id
        customer_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "cusid")))
        customer_id.clear()  # To clear input from previous tests
        customer_id.send_keys("36868")
        # Fill correct initial deposit
        initial_deposit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "inideposit")))
        initial_deposit.clear()  # To clear input from previous tests
        initial_deposit.send_keys("1000")

        # Click on submit button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "button2"))).click()

        # Click on continue
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         "#account > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(1) > a:nth-child(1)"))).click()

        # To make suer it reaches the home page
        manager_id = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tr.heading3 > td:nth-child(1)")))
        self.assertEqual("Manger Id : mngr619292", manager_id.text)

        print(f"Test Case 16: Redirects to Home page - {SUCCESS_MESSAGE}")


if __name__ == "__main__":
    unittest.main(verbosity=2)