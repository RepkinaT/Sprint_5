class LocatorRegistration:
    # Форма регистрации
    FORM = "//form[contains(@class, 'Auth_form__3qKeq')]"

    # Поля Input формы регистрации
    NAME_INPUT = FORM + "//label[text()='Имя']/../input"  # name
    EMAIL_INPUT = FORM + "//label[text()='Email']/../input"  # email
    PASSWORD_INPUT = FORM + "//label[text()='Пароль']/../input"  # password

    # Кнопка submit в форме регистрации
    SUBMIT_BUTTON = FORM + "//button"

    # тег p в котором выводится ошибка пароля
    ERROR_MESSAGE = "//p[contains(@class, 'input__error')]"


class LocatorAuthorization:
    # Форма авторизации
    FORM = "//form[contains(@class, 'Auth_form__3qKeq')]"

    # Поля Input формы авторизации
    EMAIL_INPUT = FORM + "//label[text()='Email']/../input"  # email
    PASSWORD_INPUT = FORM + "//label[text()='Пароль']/../input"  # password

    # Кнопка отправки формы
    SUBMIT_BUTTON = FORM + "//button"

    # Кнопка Войти на странице регистрации
    REGISTER_BUTTON = "//a[contains(@class, 'Auth_link__1fOlj')]"
    # Кнопка Войти на странице восстановления пароля
    FORGOT_PASSWORD_BUTTON = "//a[contains(@class, 'Auth_link__1fOlj')]"
    # Кнопка Личный кабинет на главной станице
    PROFILE_BUTTON = "//button[contains(@class, 'button_button__33qZ0')]"


class LocatorNavigation:
    # Кнопка Конструктор в navbar
    CONSTRUCTOR_BUTTON = "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Конструктор']]"
    # Кнопка Личный кабинет в navbar
    PROFILE_BUTTON = "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Личный Кабинет']]"
    # Кнопка с лого в navbar
    LOGO_BUTTON = "//div[@class='AppHeader_header__logo__2D0X2']/a"

    # Секция с ингредиентами и меню
    SECTION_INGREDIENTS = "//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]"

    # Кнопки с категориями ингредиентов
    BUTTON_CATEGORIES_BUNS = SECTION_INGREDIENTS + "//span[text()='Булки']/parent::div"
    BUTTON_CATEGORIES_SAUCES = SECTION_INGREDIENTS + "//span[text()='Соусы']/parent::div"
    BUTTON_CATEGORIES_FILLINGS = SECTION_INGREDIENTS + "//span[text()='Начинки']/parent::div"

    # Название ингредиентов в самом меню
    H2_MENU_BUNS = SECTION_INGREDIENTS + "//h2[text()='Булки']"
    H2_MENU_SAUCES = SECTION_INGREDIENTS + "//h2[text()='Соусы']"
    H2_MENU_FILLINGS = SECTION_INGREDIENTS + "//h2[text()='Начинки']"


class LocatorProfile:
    # Кнопка выхода из профиля
    BUTTON_EXIT = "//button[contains(@class, 'Account_button__14Yp3')]"

    UL = "//ul[contains(@class, 'Profile_profileList__3vTor')]"
    # Поле input в личном кабинете, который соответствует имени
    NAME_PROFILE = UL + "//label[text()='Имя']/../input"
    # Поле input в личном кабинете, который соответствует логину/email
    LOGIN_PROFILE = UL + "//label[text()='Логин']/../input"


class LocatorGeneral:
    MODAL_WINDOW = "//div[contains(@class, 'Modal_modal__P3_V5')]//div"
