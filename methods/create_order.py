import allure
import requests
from data import URL_ORDER, URL_MAIN


class OrderMethods:
    @allure.step('создание заказа')
    def create_order(self, params):
        response = requests.post(f"{URL_MAIN}{URL_ORDER}", json=params)
        return response.status_code, response.json()

    @allure.step('удаление заказа')
    def delete_order(self, login):
        response = requests.delete(f"{URL_MAIN}{URL_ORDER}/:{login}", data=login)
        return response.status_code

    @allure.step('список заказов курьера')
    def get_courier(self):
        response = requests.get(f"{URL_MAIN}{URL_ORDER}")
        return response.status_code, response.json()