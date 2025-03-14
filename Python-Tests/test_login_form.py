import pytest
import pyautogui
import time
import os
import json


class TestBase:

    @classmethod
    def setup_class(cls):
        # Load paths.json file once before all tests.
        with open('Python-Tests/paths.json','r') as file:
            cls.paths = json.load(file)

    def setup_method(self):
        # Open the application before each test
        relative_path = self.paths['Login-Form-App']
        absolute_path = os.path.abspath(relative_path)
        pyautogui.hotkey('win','r')
        pyautogui.write(f'python {absolute_path}')
        pyautogui.press('enter')
        time.sleep(2)   

    def enter_credentials(self, username, password):
        # Enter credentials to the app's corresponding input fields
        pyautogui.press('tab')
        pyautogui.write(username)
        pyautogui.press('tab')
        pyautogui.write(password)
        time.sleep(0.5)
        # Click the 'Login' button
        login_btn_path = self.paths['Assets']['login_button']
        login_button_location = pyautogui.locateOnScreen(f'{os.path.abspath(login_btn_path)}', confidence=0.8)
        if login_button_location is not None:
            pyautogui.click(login_button_location)

    def teardown_method(self):
        # Close the application after each test
        ok_btn_path = self.paths['Assets']['popup_ok_button']
        close_btn_path = self.paths['Assets']['form_exit_button']
        time.sleep(1)
        ok_button_location = pyautogui.locateOnScreen(f'{os.path.abspath(ok_btn_path)}', confidence=0.8)
        if ok_button_location is not None:
            pyautogui.click(ok_button_location)
        close_button_location = pyautogui.locateOnScreen(f'{os.path.abspath(close_btn_path)}', confidence=0.8)
        if close_button_location is not None:
            pyautogui.click(close_button_location)


class TestValidCred(TestBase):

    def test_valid_login(self):
        username = 'testuser'
        password = 'password'
        self.enter_credentials(username, password)
        # Verify successful login
        time.sleep(1)
        successful_login_img_path = self.paths['Expected-Results']['successful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(successful_login_img_path)}', confidence=0.8) is not None


class TestUsername(TestBase):

    def test_invalid_username(self):
        username = 'username'
        password = 'password'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}',confidence=0.8) is not None
        
    def test_empty_username(self):
        username = ''
        password = 'password'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None

    def test_case_sensitivity_username(self):
        username = 'Testuser'
        password = 'password'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None

    def test_special_characters_username(self):
        username = 'test@user'
        password = 'password'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None


class TestPassword(TestBase):
    
    def test_invalid_password(self):
        username = 'testuser'
        password = 'testpass'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None

    def test_empty_password(self):
        username = 'testuser'
        password = ''
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None

    def test_case_sensitivity_password(self):
        username = 'testuser'
        password = 'passworD'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None

    def test_special_characters_password(self):
        username = 'testuser'
        password = ' password '
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None


if __name__=='__main__':
    pytest.main()
