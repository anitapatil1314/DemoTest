from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_Credence_002:

    def test_Credkart_login_002(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        # go to url
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys("test@credence.in")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("test@123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        try:
            driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
            print("login test case is passed")
            driver.close()
            assert True
        except:
            print("login test case is failed")
            driver.close()
            assert False
    def test_amountverification(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.select import Select
        chrome_options = webdriver.Chrome()
        chrome_options.add_argument("headless")
        driver= webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys("test@credence.in")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("test@123")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
        driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
        driver.find_element(By.XPATH,"//h3[normalize-space()='Headphones']").click()
        driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
        driver.find_element(By.XPATH,"//h3[normalize-space()='Apple iPad Retina']").click()
        driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
        # product_quantity1 =Select(driver.find_element(By.XPATH,"//th[normalize-space()='Quantity']"))
        # product_quantity1.select_by_index(3)
