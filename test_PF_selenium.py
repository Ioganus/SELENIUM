from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestShowMyPets:

    def setup(self):
        self.user = "Vachencko.TV@yandex.ru"
        self.password = "12341234"
        self.open()


    def open(self):
        self.driver = webdriver.Chrome('/Users/79132/webdriver/ChromeDriver_114')
        self.driver.get("https://petfriends.skillfactory.ru/login")
        time.sleep(2)

    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()

    def login(self):
        self.driver.find_element(By.XPATH, "//input[@id='email']" ).send_keys(self.user)
        self.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(self.password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.find_element(By.XPATH, "//button[contains(text(),'Выйти')]")
        time.sleep(2)

    def test_show_my_pets(self):
        self.driver.find_element(By.ID, "email").send_keys(self.user)
        self.driver.find_element(By.ID, "pass").send_keys(self.password)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "PetFriends"
        
        # ОЖИДАНИЯ
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Мои питомцы')]")))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Выйти')]")))


        images = self.driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-img-top'))
        names = self.driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-title'))
        descriptions = self.driver.find_elements(By.CSS_SELECTOR, ('.card-deck .card-text'))

        for i in range(len(names)):
            assert images[i].get_attribute('src') != ' '
            assert names[i].text != ' '
            assert descriptions[i].text != ' '
            assert ', ' in descriptions[i].text
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0