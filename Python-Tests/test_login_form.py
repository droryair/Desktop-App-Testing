import pytest
import pyautogui
import time
import os
import json

class Test:

    def setUp(self):
        # Load paths.json file
        with open('Python-Tests/paths.json','r') as file:
            self.paths = json.load(file)

    def setup(self):
        # Open the application
        relative_path = self.paths['Login-Form-App']
        absolute_path = os.path.abspath(relative_path)

        pyautogui.hotkey('win','r')
        pyautogui.write(f'python {absolute_path}')
        pyautogui.press('enter')
        time.sleep(2)   

    def enter_credentials(self, username, password):
        # Enter credentials to the corresponding input fields
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


    def test_valid_login(self):
        username = 'testuser'
        password = 'password'
        self.enter_credentials(username, password)
        # Verify successful login
        time.sleep(1)
        successful_login_img_path = self.paths['Expected-Results']['successful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(successful_login_img_path)}', confidence=0.8) is not None

    def test_invalid_username(self):
        username = 'username'
        password = 'password'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}',confidence=0.8) is not None

    def test_invalid_password(self):
        username = 'testuser'
        password = 'testpass'
        self.enter_credentials(username, password)
        # Verify unsuccessful login
        unsuccessful_login_img_path = self.paths['Expected-Results']['unsuccessful_login']
        assert pyautogui.locateOnScreen(f'{os.path.abspath(unsuccessful_login_img_path)}', confidence=0.8) is not None

    def teardown(self):
        # Close the app
        ok_btn_path = self.paths['Assets']['popup_ok_button']
        close_btn_path = self.paths['Assets']['form_exit_button']
        time.sleep(1)
        ok_button_location = pyautogui.locateOnScreen(f'{os.path.abspath(ok_btn_path)}', confidence=0.8)
        if ok_button_location is not None:
            pyautogui.click(ok_button_location)
        close_button_location = pyautogui.locateOnScreen(f'{os.path.abspath(close_btn_path)}', confidence=0.8)
        if close_button_location is not None:
            pyautogui.click(close_button_location)


if __name__=='__main__':
    app_test = Test()

    app_test.setUp()
    
    # app_test.setup()
    # app_test.test_valid_login()
    # app_test.teardown()
    
    app_test.setup()
    app_test.test_invalid_username()
    app_test.teardown()
    
    app_test.setup()
    app_test.test_invalid_password()
    app_test.teardown()