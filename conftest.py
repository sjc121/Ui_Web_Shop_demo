import pytest
from selenium import webdriver

from common.log import log


@pytest.fixture(scope='class', autouse=True)
def login():
    # 打开浏览器，和基础设置
    driver = webdriver.Chrome()
    log.debug('打开浏览器')
    driver.get("http://127.0.0.1:8000")
    driver.maximize_window()
    log.debug('最大化窗口')# 打开浏览器窗口最大化
    driver.implicitly_wait(10)  # 隐式等待10秒
    yield driver
    driver.quit()
    log.debug('关闭浏览器')
