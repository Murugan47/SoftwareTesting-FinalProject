import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class TestNewCustomer(unittest.TestCase):

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

        # Clicks on new customer
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".menusubnav > li:nth-child(2) > a:nth-child(1)"))).click()

    @classmethod
    def tearDownClass(cls):
        """Quit the WebDriver instance after all tests."""
        cls.driver.quit()

    def test1_empty_name(self):
        # Clear the Name field, so there's no text from previous testcase
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "name")))
        name.clear()

        # Pressing TAB, to go the next field
        name.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message")))

        # Asserts the actual and expected message
        self.assertEqual("Customer name must not be blank", message.text)

        # Print successful message
        print("Test Case 1: Empty Name")
        print("** Passed Successfully **")

    def test2_numerical_name(self):
        # Click on the Name field to select it
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "name")))

        # Clear the Name field, so there's no text from previous testcase
        name.clear()

        # Send numerical value
        name.send_keys("name123")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message")))

        # Asserts the actual and expected message
        self.assertEqual("Numbers are not allowed", message.text)

        # Print successful message
        print("Test Case 2: Name with numbers")
        print("** Passed Successfully **")

    def test3_name_with_special_characters(self):
        # Click on the Name field to select it
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "name")))

        # Clear the Name field, so there's no text from previous testcase
        name.clear()

        # Send numerical value
        name.send_keys("!@#")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message")))

        # Asserts the actual and expected message
        self.assertEqual("Special characters are not allowed", message.text)

        # Print successful message
        print("Test Case 3: Name with special characters")
        print("** Passed Successfully **")

    def test4_name_with_first_character_blank(self):
        # Click on the Name field to select it
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "name")))

        # Clear the Name field, so there's no text from previous testcase
        name.clear()

        # Send numerical value
        name.send_keys(" name")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message")))

        # Asserts the actual and expected message
        self.assertEqual("First character can not have space", message.text)

        # Print successful message
        print("Test Case 4: Name with first character blank")
        print("** Passed Successfully **")

    def test5_empty_address(self):
        # Clear the Address field, so there's no text from previous testcase
        address = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "addr")))
        address.clear()

        # Pressing TAB, to go the next field
        address.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message3")))

        # Asserts the actual and expected message
        self.assertEqual("Address Field must not be blank", message.text)

        # Print successful message
        print("Test Case 5: Empty Address")
        print("** Passed Successfully **")

    def test6_address_with_first_character_blank(self):
        # Click on the Name field to select it
        address = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "addr")))

        # Clear the Name field, so there's no text from previous testcase
        address.clear()

        # Send numerical value
        address.send_keys(" name")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message")))

        # Asserts the actual and expected message
        self.assertEqual("First character can not have space", message.text)

        # Print successful message
        print("Test Case 6: Address with first character blank")
        print("** Passed Successfully **")

if __name__ == '__main__':
    unittest.main(verbosity=2)