from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Credkart_login():
    def test_pageTitle_001(self, setup):
        self.driver = setup
        if self.driver.title == "Credkart":
            self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_pass.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShot\\test_pageTitle_001_fail.PNG")
            assert False

    def test_Credkart_Login_002(self, setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@credence.in")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test@123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("login testcase is pased")
            self.driver.save_screenshot(".\\ScreenShots\\test_Credkart_Login_002_pass.PNG")
            assert True
        except:
            print("login testcase is failed ")
            self.driver.save_screenshot(".\\ScreenShots\\test_Credkart_Login_002_fail.PNG")
            self.driver.close()
            assert False
