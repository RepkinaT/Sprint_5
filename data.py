def valid_login_credentials():
    # Данные для авторизации
    return {
        "email": "testtestov19999@yandex.ru",
        "password": "123456789"
    }


def invalid_registration_credentials():
    # Некорректные данные для регистрации
    return {
        "name": "Test Testov",
        "email": "invalid@example.com",
        "password": "89"
    }
