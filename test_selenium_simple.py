import time

from selenium.webdriver.common.by import By

base_url = "https://petfriends.skillfactory.ru"


def test_petfriends(driver):
    # Открыть домашнюю страницу PetFriends:
    driver.get(base_url)

    time.sleep(5)  # небольшая задержка, чисто ради эксперимента

    # Находим кнопку "Зарегистрироваться" и нажимаем на нее
    btn_newuser = driver.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # Ищем надпись "У меня уже есть аккаунт" и нажимаем на нее
    btn_exist_acc = driver.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # Ищем поле ввода электронной почты, очищаем его , а затем вводим свой email,
    # подставить вместо "<your_email>" свой email.
    field_email = driver.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("<your_email>")

    # То же самое для поля с паролем
    field_pass = driver.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("<your_password>")

    # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # небольшая задержка, чисто ради эксперимента

    if driver.current_url == f'{base_url}/all_pets':
        # Если мы на странице отображения моих питомцев, то сделать скриншот
        driver.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")