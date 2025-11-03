from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    # 前置处理类
    def setup_class(self):
        # 打开浏览器，和基础设置
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000")
        self.driver.maximize_window()  # 打开浏览器窗口最大化
        self.driver.implicitly_wait(10)  # 隐式等待10秒

    # 后置处理类
    def teardown_class(self):
        self.driver.close()

    # 登录成功用例
    @pytest.mark.parametrize("username, password, result", [
        ("test123", "test123", "欢迎您：test123 | 退出"),
        ("test", "test123", "用户名错误"),
        ("test123", "test", "密码错误")
    ], ids=('test_login_case_01', 'test_login_case_02', 'test_login_case_03'))
    def test_login_case(self, username, password, result):
        self.driver.get("http://127.0.0.1:8000")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/a[1]").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[2]").send_keys(username)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[3]").send_keys(password)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[4]").click()
        sleep(2)
        if "欢迎您" in result:
            text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]").text
            assert text == result
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/em[2]/a").click()
        elif "用户名错误" in result:
            text = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/div[1]").text
            assert text == result
        elif "密码错误" in result:
            text = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/div[2]").text
            assert text == result

