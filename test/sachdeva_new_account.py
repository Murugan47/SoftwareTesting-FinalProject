import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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


if __name__ == "__main__":
    unittest.main(verbosity=2)