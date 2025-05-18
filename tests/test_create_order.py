import allure
import pytest
from data import ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3
from methods.create_order import OrderMethods


class TestCreateOrder:

    @allure.title('Тест на проверку создания заказа')
    @allure.description(
        'успешное создание заказа \
    код = 200 \
    можно указать один из цветов — BLACK или GREY; \
    можно указать оба цвета;\
    можно совсем не указывать цвет')
    @pytest.mark.parametrize('data',
        [
            ORDER_DATA_1,
            ORDER_DATA_2,
            ORDER_DATA_3
        ]
    )
    def test_create_order(self, data):
        create_courier = OrderMethods()
        status_code, response_context  = create_courier.create_order(data)
        assert status_code == 201 and 'track' in response_context

    @allure.title('Тест на проверку того, что возвращается список заказов')
    @allure.description('возвращается список заказов')
    def test_get_list_orders(self):
        create_courier = OrderMethods()
        status_code, response_context = create_courier.get_courier()
        print(response_context)
        assert status_code == 200 and 'orders' in response_context