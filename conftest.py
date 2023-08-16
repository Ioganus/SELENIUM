from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def set():
    driver = webdriver.Chrome('/Users/79132/webdriver/ChromeDriver_114')
    driver.get('http://petfriends.skillfactory.ru/login')

    yield

    driver.quit()