
URL_MAIN = 'https://qa-scooter.praktikum-services.ru/api/v1/'
URL_COURIER = 'courier/'
URL_LOGIN = 'login/'
URL_ORDER = 'orders/'
LOGIN = {'login': 'OlgaLely', 'password': '123456'}
UNCORRECT_LOGIN1 = {'login': 'OlgaLel', 'password': '123456'}
UNCORRECT_LOGIN2 = {'login': 'OlgaLely', 'password': '12345'}
UNCORRECT_LOGIN3 = {'login': 'OlgaLely', 'password': ''}
UNCORRECT_LOGIN4 = {'login': '', 'password': '123456'}
WITHOUT_LOGIN = {
        "password": "123456",
        "firstName": "lely"}
WITHOUT_PASSWORD = {
    "login": 'OlgaLely',
    "firstName": "lely"}

DATA_FULL = {
        "login": "OlgaLely",
        "password": "123456",
        "firstName": "lely"
    }

DATA_FULL_SAME_LOGIN = {
        "login": "OlgaLely",
        "password": "654321",
        "firstName": "FET"
    }

ORDER_DATA_1 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

ORDER_DATA_2 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        ""
    ]
}
ORDER_DATA_3 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK", "GREY"
    ]
}