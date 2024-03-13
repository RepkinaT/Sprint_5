import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import valid_login_credentials
from locators import LocatorAuthorization, LocatorProfile
from utils import authorization, wait_modal


class TestAuthorization:
    @pytest.mark.parametrize("css_selector, link", [
        (LocatorAuthorization.REGISTER_BUTTON, "register"),  # Переход со страницы регистрации
        (LocatorAuthorization.FORGOT_PASSWORD_BUTTON, "forgot-password"),  # Переход со страницы восстановления пароля
        (LocatorAuthorization.PROFILE_BUTTON, ""),  # Переход с главной страницы
    ])
    def test_successful_authorization(self, browser, css_selector, link):
        """Проверяем удачную авторизацию при переходе с разных страниц сайта"""

        # Открытие веб-сайта
        browser.get(f"https://stellarburgers.nomoreparties.site/{link}")
        # Ожидаем окончание анимации модального окна
        wait_modal(browser)

        # Нажимаем на кнопку Войти или Личный кабинет
        browser.find_element(By.XPATH, css_selector).click()

        data = valid_login_credentials()
        # Проходим авторизацию
        authorization(browser, data["email"], data["password"])

        # Открытие веб-сайта на странице профиля
        browser.get("https://stellarburgers.nomoreparties.site/account")
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, LocatorProfile.BUTTON_EXIT))
        )  # Ожидаем перехода на новую страницу

        # Проверяем удачную авторизацию. Текущий url страницы должен быть равен ../account/profile (страницы профиля)
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_successful_authorization_on_the_login_page(self, browser):
        """Проверяем удачную авторизацию на странице авторизации """

        # Открытие веб-сайта
        browser.get(f"https://stellarburgers.nomoreparties.site/login")
        # Ожидаем окончание анимации модального окна
        wait_modal(browser)

        data = valid_login_credentials()
        # Проходим авторизацию
        authorization(browser, data["email"], data["password"])

        # Открытие веб-сайта на странице профиля
        browser.get("https://stellarburgers.nomoreparties.site/account")

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, LocatorProfile.BUTTON_EXIT))
        )  # Ожидаем перехода на новую страницу

        # Проверяем удачную авторизацию. Текущий url страницы должен быть равен ../account/profile (страницы профиля)
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_logout_from_account_by_button(self, browser):
        """Проверяем выход по кнопке из личного кабинета"""

        # Открытие веб-сайта
        browser.get(f"https://stellarburgers.nomoreparties.site/login")

        data = valid_login_credentials()
        # Проходим авторизацию
        authorization(browser, data["email"], data["password"])

        # Переходим на страницу профиля
        browser.get("https://stellarburgers.nomoreparties.site/account")
        wait_modal(browser)  # Ожидаем окончание анимации модального окна

        # Нажимаем на кнопку выхода из профиля
        exit_profile_button = browser.find_element(By.XPATH, LocatorProfile.BUTTON_EXIT)
        exit_profile_button.click()

        WebDriverWait(browser, 10).until(
            EC.staleness_of(exit_profile_button)
        )  # Ждём перехода на главную страницу

        # Открытие веб-сайта на странице входа
        browser.get("https://stellarburgers.nomoreparties.site/account")

        # Проверяем выход из аккаунта. Url страницы должен быть равен ../login (страницы авторизации)
        assert browser.current_url == "https://stellarburgers.nomoreparties.site/login"
