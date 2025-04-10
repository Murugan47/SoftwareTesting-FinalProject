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

        # Send special character value
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

        # Send value with first character blank
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

        # Send value with first character blank
        address.send_keys(" name")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message")))

        # Asserts the actual and expected message
        self.assertEqual("First character can not have space", message.text)

        # Print successful message
        print("Test Case 6: Address with first character blank")
        print("** Passed Successfully **")

    def test7_empty_city(self):
        # Clear the City field, so there's no text from previous testcase
        city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "city")))
        city.clear()

        # Pressing TAB, to go the next field
        city.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message4")))

        print("Test Case 7: Empty City")
        try:
            # Asserts the actual and expected message
            self.assertEqual("City Field must be not blank", message.text, )
            print("** Passed Successfully **")
        except AssertionError as e:
            print("** Failed **")
            raise e

    def test8_numerical_city(self):
        # Get the city field
        city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "city")))

        # Clear the city field, so there's no text from previous testcase
        city.clear()

        # Send numerical value
        city.send_keys("city123")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message4")))

        # Asserts the actual and expected message
        self.assertEqual("Numbers are not allowed", message.text)

        # Print successful message
        print("Test Case 8: City with numbers")
        print("** Passed Successfully **")

    def test9_city_with_special_characters(self):
        # Click on the Name field to select it
        city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "city")))

        # Clear the city field, so there's no text from previous testcase
        city.clear()

        # Send special character value
        city.send_keys("!@#")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message4")))

        # Asserts the actual and expected message
        self.assertEqual("Special characters are not allowed", message.text)

        # Print successful message
        print("Test Case 9: City with special characters")
        print("** Passed Successfully **")

    def test10_city_with_first_character_blank(self):
        # Click on the Name field to select it
        city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "city")))

        # Clear the city field, so there's no text from previous testcase
        city.clear()

        # Send input with first character blank
        city.send_keys(" city")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message4")))

        # Asserts the actual and expected message
        self.assertEqual("First character can not have space", message.text)

        # Print successful message
        print("Test Case 10: City with first character blank")
        print("** Passed Successfully **")

    def test11_empty_state(self):
        # Clear the State field, so there's no text from previous testcase
        state = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "state")))
        state.clear()

        # Pressing TAB, to go the next field
        state.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message5")))

        print("Test Case 11: Empty State")

        # Asserts the actual and expected message
        self.assertEqual("State must not be blank", message.text, )
        print("** Passed Successfully **")

    def test12_numerical_state(self):
        # Get the state field
        state = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "state")))

        # Clear the state field, so there's no text from previous testcase
        state.clear()

        # Send numerical value
        state.send_keys("state123")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message5")))

        # Asserts the actual and expected message
        self.assertEqual("Numbers are not allowed", message.text)

        # Print successful message
        print("Test Case 12: State with numbers")
        print("** Passed Successfully **")

    def test13_state_with_special_characters(self):
        # Click on the Name field to select it
        state = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "state")))

        # Clear the state field, so there's no text from previous testcase
        state.clear()

        # Send special character value
        state.send_keys("!@#")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message5")))

        # Asserts the actual and expected message
        self.assertEqual("Special characters are not allowed", message.text)

        # Print successful message
        print("Test Case 13: City with special characters")
        print("** Passed Successfully **")

    def test14_state_with_first_character_blank(self):
        # Select the state field
        state = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "state")))

        # Clear the city field, so there's no text from previous testcase
        state.clear()

        # Send input with first character blank
        state.send_keys(" city")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message5")))

        # Asserts the actual and expected message
        self.assertEqual("First character can not have space", message.text)

        # Print successful message
        print("Test Case 14: State with first character blank")
        print("** Passed Successfully **")

    def test15_pin_must_be_numeric(self):
        # Click on the pin field
        pin = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "pinno")))

        # Clear the pin field, so there's no text from previous testcase
        pin.clear()

        # Send input with characters
        pin.send_keys("1234PIN")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message6")))

        # Asserts the actual and expected message
        self.assertEqual("Characters are not allowed", message.text)

        # Print successful message
        print("Test Case 15: PIN with Non-numeric input")
        print("** Passed Successfully **")

    def test16_empty_pin(self):
        # Clear the pin field, so there's no text from previous testcase
        pin = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "pinno")))
        pin.clear()

        # Pressing TAB, to go the next field
        pin.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message6")))

        print("Test Case 16: Empty PIN")

        # Asserts the actual and expected message
        self.assertEqual("PIN code must not be blank", message.text, )
        print("** Passed Successfully **")

    def test17_pin_length_less_than_six(self):
        # Clear the pin field, so there's no text from previous testcase
        pin = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "pinno")))
        pin.clear()

        # Inputting PIN, which is less than six numbers
        pin.send_keys("123")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message6")))

        print("Test Case 17: PIN less than six numbers")

        # Asserts the actual and expected message
        self.assertEqual("PIN Code must have 6 Digits", message.text, )
        print("** Passed Successfully **")

    def test18_pin_with_special_characters(self):
        # Click on the Name field to select it
        pin = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "pinno")))

        # Clear the state field, so there's no text from previous testcase
        pin.clear()

        # Send special character value
        pin.send_keys("!@#")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message6")))

        # Asserts the actual and expected message
        self.assertEqual("Special characters are not allowed", message.text)

        # Print successful message
        print("Test Case 18: PIN with special characters")
        print("** Passed Successfully **")

    def test19_pin_with_first_character_blank(self):
        # Click on the city field to select it
        pin = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "pinno")))

        # Clear the pin field, so there's no text from previous testcase
        pin.clear()

        # Send input with first character blank
        pin.send_keys(" 123456")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message6")))

        # Asserts the actual and expected message
        self.assertEqual("First character can not have space", message.text)

        # Print successful message
        print("Test Case 19: PIN with first character as blank")
        print("** Passed Successfully **")

    def test20_pin_with_any_character_blank_other_than_first(self):
        # Click on the pin field
        pin = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "pinno")))

        # Clear the pin field, so there's no text from previous testcase
        pin.clear()

        # Send input with first character blank
        pin.send_keys("12 456")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message6")))

        # Asserts the actual and expected message
        self.assertEqual("Characters are not allowed", message.text)

        # Print successful message
        print("Test Case 20: PIN with any character as blank, except the first one")
        print("** Passed Successfully **")

    def test21_empty_mobile_number(self):
        # Clear the mobile_number field, so there's no text from previous testcase
        mobile_number = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "telephoneno")))
        mobile_number.clear()

        # Pressing TAB, to go the next field
        mobile_number.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message7")))

        print("Test Case 21: Empty Mobile Number")

        # Asserts the actual and expected message
        self.assertEqual("Mobile no must not be blank", message.text, )
        print("** Passed Successfully **")

    def test22_mobile_number_with_first_character_blank(self):
        # Click on the mobile_number field to select it
        mobile_number = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "telephoneno")))

        # Clear the mobile_number field, so there's no text from previous testcase
        mobile_number.clear()

        # Send input with first character blank
        mobile_number.send_keys(" 123456")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message7")))

        # Asserts the actual and expected message
        self.assertEqual("First character can not have space", message.text)

        # Print successful message
        print("Test Case 22: Mobile Number with first character as blank")
        print("** Passed Successfully **")

    def test23_mobile_number_with_blank_except_first(self):
        # Click on the mobile_number field
        mobile_number = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "telephoneno")))

        # Clear the mobile_number field, so there's no text from previous testcase
        mobile_number.clear()

        # Send input with any character blank
        mobile_number.send_keys("12 456")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message7")))

        # Asserts the actual and expected message
        self.assertEqual("Characters are not allowed", message.text)

        # Print successful message
        print("Test Case 23: Mobile Number with any character as blank, except the first one")
        print("** Passed Successfully **")

    def test24_mobile_number_with_special_characters(self):
        # Click on the mobile_number field to select it
        mobile_number = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "telephoneno")))

        # Clear the mobile_number field, so there's no text from previous testcase
        mobile_number.clear()

        # Send special character value
        mobile_number.send_keys("!@#")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message7")))

        # Asserts the actual and expected message
        self.assertEqual("Special characters are not allowed", message.text)

        # Print successful message
        print("Test Case 24: Mobile Number with special characters")
        print("** Passed Successfully **")

    def test25_empty_email(self):
        # Clear the email field, so there's no text from previous testcase
        email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "emailid")))
        email.clear()

        # Pressing TAB, to go the next field
        email.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message9")))

        print("Test Case 25: Empty Email ID")

        try:
            # Asserts the actual and expected message
            self.assertEqual("Email ID must not be blank", message.text)
            print("** Passed Successfully **")
        except AssertionError as e:
            print("** Failed **")
            raise e

    def test26_email_incorrect_format(self):
        # Clear the email field, so there's no text from previous testcase
        email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "emailid")))
        email.clear()

        # Sending uncorrected formatted email address
        email.send_keys("guru99@gmail.")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message9")))

        print("Test Case 26: Email ID incorrect format")

        # Asserts the actual and expected message
        self.assertEqual("Email-ID is not valid", message.text)
        print("** Passed Successfully **")

    def test27_email_with_empty_space(self):
        # Clear the email field, so there's no text from previous testcase
        email = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "emailid")))
        email.clear()

        # Sending input with space
        email.send_keys("guru99@gmail .com")

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message9")))

        print("Test Case 27: Email ID with empty space")

        try:
            # Asserts the actual and expected message
            self.assertEqual("Email-ID is not valid", message.text)
            print("** Passed Successfully **")
        except AssertionError as e:
            print("** Failed **")
            raise e

    def test28_empty_password(self):
        # Clear the password field, so there's no text from previous testcase
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
        password.clear()

        # Pressing TAB, to go the next field
        password.send_keys(Keys.TAB)

        # Stores the message
        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "message18")))

        print("Test Case 28: Empty password")

        # Asserts the actual and expected message
        self.assertEqual("Password must not be blank", message.text)
        print("** Passed Successfully **")


if __name__ == '__main__':
    unittest.main(verbosity=2)