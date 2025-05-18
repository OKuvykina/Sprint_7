import allure
import pytest
from data import DATA_FULL, WITHOUT_PASSWORD, DATA_FULL_SAME_LOGIN, WITHOUT_LOGIN
from methods.create_courier import CourierMethods
from helpers import RandomGenerateCourierData


class TestCreateCourier:
    @allure.title('Тест на проверку создания курьера')
    @allure.description('успешное создание курьера \
    код = 201')
    def test_create_courier_success(self):
        create_courier = CourierMethods()
        data_courier = RandomGenerateCourierData.register_new_courier_and_return_login_password()
        status_code,  response_context = create_courier.create_courier(data_courier)
        assert status_code == 201 and response_context == {'ok': True}, \
            (f'Status is {status_code} and context is {response_context}')

    @allure.title('Тест на проверку ошибки при создании курьера,одинаковые параметры')
    @allure.description('курьер не создан \
    код ошибки = 409, \
    сообщение "code": 409,\
    "message": "Этот логин уже используется. Попробуйте другой." \
    нельзя создать 2ух одинаковых курьеров, совпадают ВСЕ параметры')
    def test_create_courier_two_same_failed(self):
        create_courier = CourierMethods()
        _,  response_context = create_courier.create_courier(DATA_FULL)
        assert response_context == {"code": 409,
    "message": "Этот логин уже используется. Попробуйте другой."} , \
            (f'context is {response_context}')


    @pytest.mark.parametrize(
        'data',
        [
            WITHOUT_PASSWORD,
            WITHOUT_LOGIN
        ]
    )
    @allure.title('Тест на проверку ошибки при создании курьера,нет данных')
    @allure.description('курьер не создан \
    не передан один из обязательных параметров \
    код ошибки = 400')
    def test_create_courier_miss_field_failed(self, data):
        create_courier = CourierMethods()
        _,  response_context = create_courier.create_courier(data)
        assert response_context == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}, \
            (f'context is {response_context}')

    @allure.title('Тест на проверку ошибки при создании курьера,повтор логина')
    @allure.description('курьер не создан \
        код ошибки = 409 \
        сообщение {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."} \
        совпадает ТОЛЬКО логин')
    def test_create_courier_same_login_failed(self):
        create_courier = CourierMethods()
        _, response_context = create_courier.create_courier(DATA_FULL_SAME_LOGIN)
        assert response_context == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}, \
            (f'context is {response_context}')


