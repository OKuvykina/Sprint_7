import allure
import requests
from data import URL_COURIER, URL_MAIN


class CourierMethods:
    @allure.step('создание курьера')
    def create_courier(self, params):
        response = requests.post(f"{URL_MAIN}{URL_COURIER}", json=params)
        return response.status_code, response.json()

    @allure.step('удаление курьера')
    def delete_courier(self, login):
        response = requests.delete(f"{URL_MAIN}{URL_COURIER}/:{login}", data=login)
        return response.status_code
