from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import invalid_registration_credentials
from locators import LocatorRegistration
from utils import registration, wait_modal


class TestRegistration:
    def test_registration_correct_data(
            self, browser, generate_random_name, generate_random_email, generate_random_password):
        """ Проверка успешной регистрации с корректными данными """

        # Открытие веб-сайта на главной страницы
        browser.get("https://stellarburgers.nomoreparties.site/register")
        wait_modal(browser)  # Ожидаем окончание анимации модального окна

        # Вносим некорректные данные в форму регистрации
        registration(browser, generate_random_name, generate_random_email, generate_random_password)

        WebDriverWait(browser, 30).until(
            EC.staleness_of(browser.find_element(By.XPATH, LocatorRegistration.SUBMIT_BUTTON))
        )  # Ждём перехода на другую страницу

        # После успешной регистрации страница меняет url-адрес. Url страницы должен быть равен ../login
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_incorrect_password(self, browser):
        """ Проверка вывода ошибки "Некорректный пароль" """

        # Открытие веб-сайта на главной страницы
        browser.get("https://stellarburgers.nomoreparties.site/register")
        # Ожидаем окончание анимации модального окна
        wait_modal(browser)

        data = invalid_registration_credentials()

        # Вносим некорректные данные в форму регистрации
        registration(browser, data["name"], data["email"], data["password"])

        # Ждем когда загрузится ошибка
        error = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, LocatorRegistration.ERROR_MESSAGE))
        )

        # Проверка наличие ошибки при вводе некорректного пароля. error.text должен быть равен "Некорректный пароль"
        assert error is not None and error.text == "Некорректный пароль"
