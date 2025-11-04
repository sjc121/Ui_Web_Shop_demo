import os
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from settings import ENV


class TestLogin:
    # 登录成功用例
    @pytest.mark.parametrize("username, password, result", [
        ("test123", "test123", "欢迎您：test123 | 退出"),
        ("test", "test123", "用户名错误"),
        ("test123", "test", "密码错误")
    ], ids=('test_login_case_01', 'test_login_case_02', 'test_login_case_03'))
    def test_login_case(self, username, password, result, login):
        driver = login
        driver.get(ENV.url)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/a[1]").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[2]").send_keys(username)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[3]").send_keys(password)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/input[4]").click()
        sleep(2)
        if "欢迎您" in result:
            text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]").text
            assert text == result
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/em[2]/a").click()
        elif "用户名错误" in result:
            text = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/div[1]").text
            assert text == result
        elif "密码错误" in result:
            text = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/form/div[2]").text
            assert text == result
