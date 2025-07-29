from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:

    # 登录成功用例
    def test_login_OK_01(self):
        # 打开浏览器，和基础设置
        driver = webdriver.Edge()
        driver.get("http://127.0.0.1:8000")
        driver.maximize_window()  # 打开浏览器窗口最大化
        driver.implicitly_wait(10)  # 隐式等待10秒
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/a[1]").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[2]").send_keys("test123")
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[3]").send_keys("test123")
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[4]").click()
        driver.close()

        # 登录失败，用户名不存在

    def test_login_OK_02(self):
        # 打开浏览器，和基础设置
        driver = webdriver.Edge()
        driver.get("http://127.0.0.1:8000")
        driver.maximize_window()  # 打开浏览器窗口最大化
        driver.implicitly_wait(10)  # 隐式等待10秒
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/a[1]").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[2]").send_keys("test")
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[3]").send_keys("test123")
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[4]").click()
        sleep(1)
        text = driver.find_element(By.XPATH, "//div[@class='user_error']").text
        assert text == "用户名错误"
