from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatorRegistration, LocatorAuthorization, LocatorGeneral


def registration(browser, name, email, password):
    """ Вносим переданные данные в форму регистрации """

    # Получаем тег input для ввода имени
    name_input = browser.find_element(By.XPATH, LocatorRegistration.NAME_INPUT)
    # Получаем тег input для ввода email
    email_input = browser.find_element(By.XPATH, LocatorRegistration.EMAIL_INPUT)
    # Получаем тег input для ввода пароля
    pass_input = browser.find_element(By.XPATH, LocatorRegistration.PASSWORD_INPUT)

    # Вносим данные в форму
    for _input, data in zip((name_input, email_input, pass_input), (name, email, password)):
        _input.send_keys(data)  # Вставляем данные в поле input

    # Кликаем кнопку submit в форме
    submit_button = browser.find_element(By.XPATH, LocatorRegistration.SUBMIT_BUTTON)
    submit_button.click()


def authorization(browser, email, password):
    """ Авторизация """

    # Получаем тег input для ввода email
    email_input = browser.find_element(By.XPATH, LocatorAuthorization.EMAIL_INPUT)
    # Получаем тег input для ввода пароля
    pass_input = browser.find_element(By.XPATH, LocatorAuthorization.PASSWORD_INPUT)

    # Вносим данные в форму
    for _input, data in zip((email_input, pass_input), (email, password)):
        _input.send_keys(data)  # Вставляем данные в поле input

    # Нажимаем кнопку войти
    submit_button = browser.find_element(By.XPATH, LocatorAuthorization.SUBMIT_BUTTON)
    submit_button.click()

    WebDriverWait(browser, 30).until(
        EC.staleness_of(submit_button)
    )  # Ждём перехода на другую страницу


def wait_modal(browser):
    modal_window = browser.find_element(By.XPATH, LocatorGeneral.MODAL_WINDOW)
    WebDriverWait(browser, 30).until(EC.invisibility_of_element_located(modal_window))
