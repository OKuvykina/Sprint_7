import allure
import pytest

from methods.login_courier import LoginMethods
from data import LOGIN, UNCORRECT_LOGIN1, UNCORRECT_LOGIN2,UNCORRECT_LOGIN3,UNCORRECT_LOGIN4


class TestLoginCourier:
    @allure.title('Тест на проверку успешной авторизации курьера')
    @allure.description('курьер может авторизоваться, код = 200')
    def test_login_success(self):
        login_courier = LoginMethods()
        status_code, _ = login_courier.login_courier(LOGIN)
        assert status_code == 200, (f'status_code is {status_code}')

    @allure.title('Тест на проверку неудачной авторизации курьера с неправ параметрами')
    @allure.description('проверка, что возвращается ошибка,если авторизоваться '
                    'под несуществующим пользователем,система вернёт ошибку, '
                    'если неправильно указать логин или пароль')
    @pytest.mark.parametrize('data',
    [
        UNCORRECT_LOGIN1,
        UNCORRECT_LOGIN2
    ])
    def test_login_uncorrect(self, data):
        login_courier = LoginMethods()
        status_code, response_context = login_courier.login_courier(data)
        assert status_code == 404, (f'status_code is {status_code}, {response_context}')

    @allure.title('Тест на проверку неудачной авторизации курьера без параметров')
    @allure.description('проверка, что возвращается ошибка, '
                        'если передать не все обязательные параметры')
    @pytest.mark.parametrize('data',
    [
        UNCORRECT_LOGIN3,
        UNCORRECT_LOGIN4
    ])
    def test_without_param(self, data):
        login_courier = LoginMethods()
        status_code, response_context = login_courier.login_courier(data)
        assert status_code == 400, (f'status_code is {status_code}, {response_context}')

    @allure.title('Тест на проверку того, что id вернулся не нулевым')
    @allure.description('проверка, что id вернулся не нулевым')
    def test_return_login(self, login):
        assert login != None