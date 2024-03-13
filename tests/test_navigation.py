import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatorNavigation
from utils import wait_modal


class TestNavigation:
    @pytest.mark.parametrize("locator, link, required_url", [
        (LocatorNavigation.PROFILE_BUTTON, "", "login"),
        (LocatorNavigation.CONSTRUCTOR_BUTTON, "login", ""),
        (LocatorNavigation.LOGO_BUTTON, "login", ""),
    ])
    def test_navigate_navbar_button(self, browser, locator, link, required_url):
        """Проверяем переход кнопки Личный кабинет с главной страницы и
        переход кнопки Конструктор и кнопки с лого со страницы Личного кабинета"""

        # Открытие веб-сайта на странице
        browser.get(f"https://stellarburgers.nomoreparties.site/{link}")
        wait_modal(browser)  # Ожидаем окончание анимации модального окна

        # Нажимаем на соответствующую кнопку (Конструктор / лого / личный кабинет)
        browser.find_element(By.XPATH, locator).click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, LocatorNavigation.LOGO_BUTTON))
        )  # Ожидаем перехода на новую страницу

        # получаем текущую ссылку на страницу
        url = browser.current_url

        # Проверяем полученный url страницы с required_url
        assert url == f"https://stellarburgers.nomoreparties.site/{required_url}"

    def test_navigate_to_constructor_from_menu_homepage(self, browser):
        """Проверяем переходы по категориям из меню в разделе Конструктор"""

        # Открытие веб-сайта на главной страницы
        browser.get("https://stellarburgers.nomoreparties.site/")
        wait_modal(browser)  # Ожидаем пока закроется модальное окно

        # Получаем кнопки категорий
        button_categories_ingredient = [
            browser.find_element(By.XPATH, path) for path in (LocatorNavigation.BUTTON_CATEGORIES_FILLINGS,
                                                              LocatorNavigation.BUTTON_CATEGORIES_SAUCES,
                                                              LocatorNavigation.BUTTON_CATEGORIES_BUNS)
        ]
        # Получаем название категорий в самом меню
        names_ingredient_menu = [
            browser.find_element(By.XPATH, path) for path in (LocatorNavigation.H2_MENU_FILLINGS,
                                                              LocatorNavigation.H2_MENU_SAUCES,
                                                              LocatorNavigation.H2_MENU_BUNS)
        ]

        # Итерируемся по категориям и названием меню
        for button, name_ingredient in zip(button_categories_ingredient, names_ingredient_menu):
            button.click()  # Нажимаем на одну из категорий [Начинки, Соусы, Булки]

            # видимость элемента в меню
            element = WebDriverWait(browser, 10).until(EC.visibility_of(name_ingredient))

            # Проверяем название элемента из меню и сравниваем с названием нажатой кнопки из категорий
            assert element.text == button.text
