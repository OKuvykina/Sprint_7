import pytest
from methods.create_courier import CourierMethods
from methods.login_courier import LoginMethods
from data import DATA_FULL, LOGIN


@pytest.fixture #создание и удаление курьера
def courier():
    responce = CourierMethods().create_courier(DATA_FULL)
    yield responce.json()['id']
    CourierMethods.delete_courier(responce.json()['id'])

@pytest.fixture #залогиниться и получить id
def login():
    responce = LoginMethods().login_courier(LOGIN)
    yield responce[1]['id']
