import allure
import requests
from data import URL_COURIER, URL_LOGIN, URL_MAIN


class LoginMethods:
    @allure.step('залогинились')
    def login_courier(self, params):
        response = requests.post(f"{URL_MAIN}{URL_COURIER}{URL_LOGIN}", json=params)
        return response.status_code, response.json()
