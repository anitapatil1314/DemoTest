from selenium import webdriver
class Test_Credence_001:

    def test_credence_url_001(self):
        driver=webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            assert True
        else:
            assert False

    def test_sum_002(self):
        a = 10
        b = 20
        sum = a+b
        if sum == 30:
            assert True
        else:
            assert False