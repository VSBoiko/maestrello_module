import requests

from classes.MaestrelloBasic import MaestrelloBasic
from classes.MaestrelloShipping import MaestrelloShipping
from classes.MaestrelloBasket import MaestrelloBasket
from classes.MaestrelloUser import MaestrelloUser


class MaestrelloOrder (MaestrelloBasic):
    def __init__(self):
        super().__init__()
        self.__all_statuses = self.get_via_api_order_statuses()
        setts = self._get_order_settings()
        self.__all_payments = setts["payment"] if "payment" in setts else []
        self.__all_shipments = setts["shipping"] if "shipping" in setts else []

    def create_order_by_user(self, token: str, user_id: int, basket: list,
                             order_params: dict, comment: str = ""):
        """
        Создание заказа для зарегистрированного пользователя

        GET https://pizzamaestrello.com/api.php/p/v1/create-order?
            access_token=6468ebad4ffd727212661f412552edc2ee3

        BODY
        {
            "contact_id": "20992",
            "comment": "TEST TEST TEST TEST",
            "params": {
                "payment_id": "1",
                "restaurant_id": "1",
                "payment_params_change": "3333",
                "shipping_address.city": "Москва",
                "shipping_address.country": "rus",
                "shipping_address.dom": "31",
                "shipping_address.etazh": "3",
                "shipping_address.kod-domofona": "3",
                "shipping_address.kvartira": "3",
                "shipping_address.podezd": "3",
                "shipping_address.region": "77",
                "shipping_address.street": "Ос",
                "shipping_id": "37",
                //"shipping_params_desired_delivery_variant": "Ближайшее время",
                    // если выбрать Дата и время, нужно передать еще дату и интервал
                "shipping_params_desired_delivery_variant": "Дата и время",
                "shipping_params_desired_delivery.date": "2021-07-13",
                //"shipping_params_desired_delivery.interval": "12:00-12:30",
                "shipping_params_person_count": "5"
            },
            "items": [
                {
                    "sku_id": "63",
                    "quantity": "3",
                    "services": [
                        {
                            "service_variant_id": "15"
                        }
                    ]
                }
            ]
        }

        :param token: токен пользователя для работы с API (использовать MaestrelloUser.get_token())
        :param user_id: ID пользователя
        :param basket: корзина (передать результат из MaestrelloBasket.get_basket_for_order())
        :param order_params: параметры заказа (передать результат из MaestrelloBasket.create_order_params())
        :param (не обязаельный) comment: комментарий к заказу

        :return:
        {
            "order_id": 24127,
            "contact_id": 20992,
            "is_new_contact": false
        }
        """

        api_url = f'{self.api}create-order'
        params = {
            "access_token": token,
        }

        data = {
            "contact_id": str(user_id),
            "comment": comment,
            "items": basket,
            "params": {},
        }
        data["params"].update(order_params)

        response = requests.get(url=api_url, headers=self.headers, params=params, json=data)
        return self._validate(response=response, params=(params, data))

    def create_order_by_guest(self, token: str, user_name: str, user_phone: str,
                              user_email: str, basket: list, order_params: dict,
                              comment: str = ""):
        """
        Создание заказа для гостя (незарегестрированного пользователя)

        GET https://pizzamaestrello.com/api.php/p/v1/create-order?
            access_token=6468ebad4ffd727212661f412552edc2ee3

        BODY
        {
            "contact": {
                "name": "Алексей Тест",
                "phone": "+79299082303",
                "email": "a.volkov@maestrello.ru"
            },
            "comment": "TEST TEST TEST TEST",
            "coupon_code": "QJX4A30B",
            "params": {
                "payment_id": "39",
                "payment_params_change": "3333",
                "shipping_address.city": "Москва",
                "shipping_address.country": "rus",
                "shipping_address.etazh": "3",
                "shipping_address.kod-domofona": "3",
                "shipping_address.kvartira": "3",
                "shipping_address.podezd": "3",
                "shipping_address.region": "77",
                "shipping_address.street": "Хромова 40",
                "shipping_id": "37",
                "shipping_params_desired_delivery_variant": "Дата и время",
                "shipping_params_desired_delivery.date": "2021-07-13",
                "shipping_params_desired_delivery.date_str": "13.07.2021",
                "shipping_params_desired_delivery.interval": "12:00-12:30",
                "shipping_params_person_count": "5"
            },
            "items": [
                {
                    "sku_id": "63",
                    "quantity": "3",
                    "services": [
                        {
                            "service_variant_id": "15"
                        },
                        {
                            "service_variant_id": "20"
                        }
                    ]
                }
            ]
        }

        :param token: токен пользователя для работы с API (можно
            использовать MaestrelloUser.get_token())
        :param user_name: ФИО пользователя
        :param user_phone: номер телефона пользователя
        :param user_email: e-mail пользователя
        :param basket: корзина (передать результат
            из MaestrelloBasket.get_basket_for_order())
        :param order_params: параметры заказа (передать результат
            из MaestrelloBasket.create_order_params())
        :param (не обязаельный) comment: комментарий к заказу


        :return:
        {
            "order_id": 24127,
            "contact_id": 21796,
            "is_new_contact": true
        }
        """

        api_url = f'{self.api}create-order'
        params = {
            "access_token": token,
        }

        data = {
            "contact": {
                "name": user_name,
                "phone": user_phone,
                "email": user_email
            },
            "comment": comment,
            "items": basket,
            "params": {},
            # "coupon_code": "QJX4A30B",            # так применяется купон
        }

        data["params"].update(order_params)

        response = requests.get(url=api_url, headers=self.headers, params=params, json=data)
        return self._validate(response=response, params=(params, data))

    def create_order_params(self, payment_id: int, shipping_id: int, shipping_address: dict,
                            person_count: int = 1, change_with: int = 0):
        """
        Создать словарь с параметрами для создания заказа

        :param payment_id: ID способа оплаты
        :param shipping_id: ID способа доставки
        :param shipping_address: словарь с данными для доставки (передать результат
            из MaestrelloShipping.create_shipping_address())
        :param (не обязательный) person_count: количество приборов для еды
        :param (не обязательный) change_with: с какой суммы подготовить сдачу

        :return:
        {
            "payment_id": "1",
            "restaurant_id": "1",
            "payment_params_change": "3333",
            "shipping_address.city": "Москва",
            "shipping_address.country": "rus",
            "shipping_address.dom": "31",
            "shipping_address.etazh": "3",
            "shipping_address.kod-domofona": "3",
            "shipping_address.kvartira": "3",
            "shipping_address.podezd": "3",
            "shipping_address.region": "77",
            "shipping_address.street": "Ос",
            "shipping_id": "37",
            //"shipping_params_desired_delivery_variant": "Ближайшее время",
                // если выбрать Дата и время, нужно передать еще дату и интервал
            "shipping_params_desired_delivery_variant": "Дата и время",
            "shipping_params_desired_delivery.date": "2021-07-13",
            //"shipping_params_desired_delivery.interval": "12:00-12:30",
            "shipping_params_person_count": "5"
        }
        """

        data = {
            "payment_id": str(payment_id),
            "restaurant_id": "",  # id ресторана, его можно не передавать
            "payment_params_change": str(change_with),  # с какой суммы нужна сдача
            "shipping_id": str(shipping_id),
            "shipping_params_person_count": str(person_count),

            # реализовать работу со временем через MaestrelloShipping
            "shipping_params_desired_delivery_variant": "Ближайшее время",
            # если выбрать Дата и время, нужно передать еще дату и интервал
            # "shipping_params_desired_delivery_variant": "Дата и время",
            # "shipping_params_desired_delivery.date": "2021-07-13",
            # "shipping_params_desired_delivery.interval": "12:00-12:30",
        }
        data.update(shipping_address)
        return data

    def get_all_payments(self):
        """
        Получить список всех возможных способов оплаты

        :return:
        [
            {
                "id": "13",
                "plugin": "paykeeper",
                "name": "Банковской картой на сайте"
            },
            {
                "id": "1",
                "plugin": "cash",
                "name": "Наличными"
            }
        ]
        """
        return self.__all_payments

    def get_all_shipments(self):
        """
        Получить список всех возможных способов доставки

        :return:
        [
            {
                "id": "11",
                "plugin": "sd",
                "name": "Самовывоз, Покровка, 16"
            },
            {
                "id": "15",
                "plugin": "sd",
                "name": "Самовывоз, Мытная, 74"
            },
            {
                "id": "37",
                "plugin": "pro",
                "name": "Курьером"
            }
        ]
        """
        return self.__all_shipments

    def get_all_statuses(self):
        """
        Получить список всех возможных статусов заказа

        :return:
        [
            {
                "id": "new",
                "name": "Новый"
            },
            {
                "id": "processing",
                "name": "Подтвержден"
            },
            {
                "id": "auth",
                "name": "Средства заблокированы"
            },
            {
                "id": "paid",
                "name": "Оплачен"
            },
            {
                "id": "otpravlen-v-rest",
                "name": "Отправлен в ресторан"
            },
            {
                "id": "prinyat-restoran",
                "name": "Принят рестораном"
            },
            {
                "id": "prigotovlen-rest",
                "name": "Приготовлен рестораном"
            },
            {
                "id": "shipped",
                "name": "Доставляется"
            },
            {
                "id": "completed",
                "name": "Выполнен"
            },
            {
                "id": "refunded",
                "name": "Возврат"
            },
            {
                "id": "deleted",
                "name": "Аннулирован"
            }
        ]
        """
        return self.__all_statuses

    def get_order(self, token: str, order_id: int):
        """
        Получить заказ по ID

        GET https://pizzamaestrello.com/api.php/p/v1/get-order?
            id=23997&
            access_token=6468ebad4ffd727212661f412552edc2ee3

        :param token: токен пользователя для работы с API (см. MaestrelloUser.get_token())
        :param order_id: ID заказа

        :return:
        {
            "id": "23997",
            "contact_id": "21266",
            "create_datetime": "2021-07-22 14:11:28",
            "update_datetime": "2021-07-22 15:01:34",
            "state_id": "otpravlen-v-rest",
            "total": "2205.0000",
            "currency": "RUB",
            "rate": "1.00000000",
            "tax": "0.0000",
            "shipping": "300.0000",
            "discount": "0.0000",
            "assigned_contact_id": null,
            "paid_year": null,
            "paid_quarter": null,
            "paid_month": null,
            "paid_date": null,
            "auth_date": null,
            "is_first": "0",
            "unsettled": "0",
            "comment": "TEST TEST TEST TEST",
            "shipping_datetime": null,
            "params": {
                "auth_code": "483b303952aff41a239978873d4171f85ac57",
                "auth_pin": "1246",
                "ip": "85.62.84.35",
                "payment_id": "39",
                "payment_params_change": "3333",
                "reduced": "1",
                "reduce_times": "1",
                "restaurant_id": "1",
                "sales_channel": "storefront:pizzamaestrello.com",
                "shipping_address.city": "Москва",
                "shipping_address.country": "rus",
                "shipping_address.etazh": "3",
                "shipping_address.kod-domofona": "3",
                "shipping_address.kvartira": "3",
                "shipping_address.podezd": "3",
                "shipping_address.region": "77",
                "shipping_address.street": "Хромова 40",
                "shipping_currency": "RUB",
                "shipping_currency_rate": "1",
                "shipping_id": "37",
                "shipping_params_desired_delivery.date": "2021-07-13",
                "shipping_params_desired_delivery.date_str": "13.07.2021",
                "shipping_params_desired_delivery.interval": "12:00-12:30",
                "shipping_params_desired_delivery_variant": "Дата и время",
                "shipping_params_person_count": "5",
                "signup_url": "",
                "storefront": "pizzamaestrello.com",
                "user_agent": "PostmanRuntime/7.28.2"
            },
            "contact": {
                "id": "21266",
                "name": "Ivan Petrovich",
                "email": "a.volkov@maestrello.ru",
                "phone": "89299082303",
                "registered": true,
                "photo_50x50": "//www.gravatar.com/avatar/1841b8d777b15bdc78951a54e5b59646?
                    size=50&
                    default=https%3A%2F%2Fpizzamaestrello.com%2F%2Fwa-content%2Fimg%2Fuserpic50.jpg"
            },
            "items": {
                "97488": {
                    "id": "97488",
                    "order_id": "23997",
                    "name": "Салмон спэшл",
                    "product_id": "60",
                    "sku_id": "63",
                    "sku_code": "",
                    "type": "product",
                    "service_id": null,
                    "service_variant_id": null,
                    "price": "495.0000",
                    "quantity": "3",
                    "parent_id": null,
                    "stock_id": null,
                    "virtualstock_id": null,
                    "purchase_price": "0.0000",
                    "total_discount": "0.0000",
                    "tax_percent": null,
                    "tax_included": "0",
                    "image_id": "60",
                    "image_filename": "",
                    "sku_image_id": null,
                    "ext": "jpg",
                    "file_name": "",
                    "file_size": "0"
                },
                "97489": {
                    "id": "97489",
                    ...
                }
            },
            "items_total_discount": 0
        }
        """

        api_url = f'{self.api}get-order'
        params = {
            "access_token": token,
            "id": order_id
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)
        return self._validate(response=response, params=params)

    def get_order_status(self, token: str, order_id: int):
        """
        Получить статус заказа

        https://pizzamaestrello.com/api.php/p/v1/get-order-status?
            id=23997&
            access_token=6468ebad4ffd727212661f412552edc2ee3

        :param token: токен пользователя для работы с API (см. MaestrelloUser.get_token())
        :param order_id: ID заказа

        :return:
        {
            "order_status": "Отправлен в ресторан"
        }
        """

        api_url = f'{self.api}get-order-status'
        params = {
            "access_token": token,
            "id": order_id
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)
        return self._validate(response=response, params=params)

    def get_orders(self, token, limit: int = 1000):
        """
        Массив заказов покупателя

        GET https://pizzamaestrello.com/api.php/p/v1/get-orders?
            access_token=6468ebad4ffd727212661f412552edc2ee3&
            limit=3

        :param token: токен пользователя для работы с API (см. MaestrelloUser.get_token())
        :param limit: лимит записей, сортировка - последние в начале

        :return:
        {
            "orders_total": "1",
            "orders": [
                {
                    "id": "23616",
                    "contact_id": "21266",
                    "create_datetime": "2021-07-15 15:47:43",
                    "update_datetime": null,
                    "state_id": "processing",
                    "total": "1135.0000",
                    "currency": "RUB",
                    "rate": "1.00000000",
                    "tax": "0.0000",
                    "shipping": "300.0000",
                    "discount": "0.0000",
                    "assigned_contact_id": null,
                    "paid_year": null,
                    "paid_quarter": null,
                    "paid_month": null,
                    "paid_date": null,
                    "auth_date": null,
                    "is_first": "0",
                    "unsettled": "0",
                    "comment": "ТЕСТ ТЕСТ ТЕСТ",
                    "shipping_datetime": null,
                    "params": {
                        "auth_code": "61d1531562469afa23616a07b598c0e240095",
                        "auth_pin": "7748",
                        "billing_address.city": "",
                        "billing_address.country": "rus",
                        "billing_address.dom": "",
                        "billing_address.etazh": "",
                        "billing_address.kod-domofona": "",
                        "billing_address.kolichestvo-per": "",
                        "billing_address.kvartira": "",
                        "billing_address.lat": "",
                        "billing_address.lng": "",
                        "billing_address.podezd": "",
                        "billing_address.prigotovit-k": "",
                        "billing_address.region": "",
                        "billing_address.street": "",
                        "billing_address.svoe-vremya-dos": "",
                        "billing_address.vremya-dostavki": "",
                        "billing_address.zip": "",
                        "coupon_id": "0",
                        "departure_datetime": "2021-07-15 16:47:43",
                        "payment_id": "1",
                        "payment_name": "Наличными",
                        "payment_plugin": "cash",
                        "referer_host": "",
                        "sales_channel": "backend:",
                        "shipping_address.city": "Москва",
                        "shipping_address.country": "rus",
                        "shipping_address.dom": "30",
                        "shipping_address.etazh": "1",
                        "shipping_address.kod-domofona": "",
                        "shipping_address.kolichestvo-per": "",
                        "shipping_address.kvartira": "2",
                        "shipping_address.lat": "",
                        "shipping_address.lng": "",
                        "shipping_address.podezd": "",
                        "shipping_address.prigotovit-k": "",
                        "shipping_address.region": "77",
                        "shipping_address.street": "8е Марта",
                        "shipping_address.svoe-vremya-dos": "",
                        "shipping_address.vremya-dostavki": "",
                        "shipping_address.zip": "",
                        "shipping_currency": "RUB",
                        "shipping_currency_rate": "1",
                        "shipping_id": "37",
                        "shipping_name": "Курьером",
                        "shipping_params_data": "",
                        "shipping_params_desired_delivery.date": "",
                        "shipping_params_desired_delivery.date_str": "",
                        "shipping_params_desired_delivery.interval": "",
                        "shipping_params_desired_delivery_variant": "Дата и время",
                        "shipping_params_person_count": "5",
                        "shipping_plugin": "pro",
                        "shipping_rate_id": "0"
                    },
                    "contact": {
                        "id": "21266",
                        "name": "Ivan Petrovich",
                        "email": "a.volkov@maestrello.ru",
                        "phone": "89299082303",
                        "registered": true,
                        "photo_50x50": "//www.gravatar.com/avatar/1841b8d777b15bdc78951a54e5b59646?size=50&default=https%3A%2F%2Fpizzamaestrello.com%2F%2Fwa-content%2Fimg%2Fuserpic50.jpg"
                    },
                    "items": {
                        "95800": {
                            "id": "95800",
                            "order_id": "23616",
                            "name": "Вегана",
                            "product_id": "21",
                            "sku_id": "13",
                            "sku_code": "",
                            "type": "product",
                            "service_id": null,
                            "service_variant_id": null,
                            "price": "545.0000",
                            "quantity": "1",
                            "parent_id": null,
                            "stock_id": null,
                            "virtualstock_id": null,
                            "purchase_price": "0.0000",
                            "total_discount": "0.0000",
                            "tax_percent": null,
                            "tax_included": "0",
                            "image_id": "19",
                            "image_filename": "",
                            "sku_image_id": null,
                            "ext": "jpeg",
                            "file_name": "",
                            "file_size": "0"
                        },
                        "95801": {
                            "id": "95801",
                            "order_id": "23616",
                            "name": "Анчоусы (13г)",
                            "product_id": "21",
                            "quantity": "1",
                            ...
                        },
                        "95802": {
                            "id": "95802",
                            "order_id": "23616",
                            "name": "Артишоки (35г)",
                            "product_id": "21",
                            "quantity": "1",
                            ...
                        },
                        "95803": {
                            "id": "95803",
                            "order_id": "23616",
                            "name": "Грецкие орехи (5г)",
                            "product_id": "21",
                            "quantity": "1",
                            ...
                        }
                    },
                    "items_total_discount": 0
                }
            ]
        }
        """

        api_url = f'{self.api}get-orders'
        params = {
            "access_token": token,
            "limit": limit
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)
        return self._validate(response=response, params=params)

    def get_via_api_order_statuses(self):
        """
        Получить список возможных статусов заказа

        GET https://pizzamaestrello.com/api.php/p/v1/get-order-statuses

        :return:
        [
            {
                "id": "new",
                "name": "Новый"
            },
            {
                "id": "processing",
                "name": "Подтвержден"
            },
            {
                "id": "auth",
                "name": "Средства заблокированы"
            },
            {
                "id": "paid",
                "name": "Оплачен"
            },
            {
                "id": "otpravlen-v-rest",
                "name": "Отправлен в ресторан"
            },
            {
                "id": "prinyat-restoran",
                "name": "Принят рестораном"
            },
            {
                "id": "prigotovlen-rest",
                "name": "Приготовлен рестораном"
            },
            {
                "id": "shipped",
                "name": "Доставляется"
            },
            {
                "id": "completed",
                "name": "Выполнен"
            },
            {
                "id": "refunded",
                "name": "Возврат"
            },
            {
                "id": "deleted",
                "name": "Аннулирован"
            }
        ]
        """

        api_url = f'{self.api}get-order-statuses'

        response = requests.get(url=api_url, headers=self.headers)
        return self._validate(response=response, params=None)

    def _get_order_settings(self):
        """
        Возвращает словарь с возможными способами оплаты и доставки

        GET https://pizzamaestrello.com/api.php/p/v1/order-settings
        Accept: application/json

        :return:
        {
            "shipping": [
                {
                    "id": "11",
                    "plugin": "sd",
                    "name": "Самовывоз, Покровка, 16"
                },
                {
                    "id": "15",
                    "plugin": "sd",
                    "name": "Самовывоз, Мытная, 74"
                },
                {
                    "id": "37",
                    "plugin": "pro",
                    "name": "Курьером"
                }
            ],
            "payment": [
                {
                    "id": "13",
                    "plugin": "paykeeper",
                    "name": "Банковской картой на сайте"
                },
                {
                    "id": "1",
                    "plugin": "cash",
                    "name": "Наличными"
                }
            ]
        }
        """

        api_url = f'{self.api}order-settings'
        response = requests.get(url=api_url, headers=self.headers)
        return self._validate(response=response, params=None)


if __name__ == "__main__":
    def show_title(text):
        print(f"\n\n{text}\n")

    mt_order = MaestrelloOrder()

    # Получить все способы оплаты
    show_title("Все способы оплаты")
    print(mt_order.get_all_payments())

    # Получить все способы доставки
    show_title("Все способы доставки")
    print(mt_order.get_all_shipments())

    # Получить все возможные статусы заказа
    show_title("Все возможные статусы заказа")
    print(mt_order.get_all_statuses())

    # Создать заказ
    show_title("Создать заказ")

    mt_user = MaestrelloUser()
    login = "vlad2010-1996@mail.ru"
    password = "-7b8Ouisb!j"

    token = mt_user.get_token(
        login=login,
        password=password
    )
    print("Токен", token)

    auth_user = mt_user.auth(
        login=login,
        password=password
    )
    print("Авторизованный пользователь", auth_user)

    mt_shipping = MaestrelloShipping()
    ad = mt_shipping.create_shipping_address(
        city="Краснодар",
        street="Красная",
        house_number="197/1",
        flat="203",
        entrance="1",
        region="23",
        country="rus",
        floor="16",
        intercom_code="B203",
    )

    params = mt_order.create_order_params(
        payment_id=1,
        shipping_id=11,
        shipping_address=ad,
        person_count=2,
        change_with=5000,
    )
    print("Параметры заказа:", params)

    mt_basket = MaestrelloBasket()
    mt_basket.add_product(21, 7)
    mt_basket.add_product(25, 10)
    # mt_basket.add_product_mod(21, 17)
    # mt_basket.add_product_mod(21, 18)
    # mt_basket.add_product_mod(25, 19)

    basket = mt_basket.get_basket_for_order()
    print("Корзина:", basket)

    # new_order = mt_order.create_order_by_user(
    #    token=token,
    #    user_id=auth_user["id"],
    #    basket=basket,
    #    order_params=params,
    #    comment="Тестовый заказ, не принимайте"
    # )
    # print("Новый заказ:", new_order)

    # Получить заказ по ID
    show_title("Получить заказ по его ID")
    print(mt_order.get_order(
        token=token,
        order_id=40457
    ))

    # Получить заказ по ID
    show_title("Получить все заказы пользователя")
    print(mt_order.get_orders(
        token=token,
    ))

    # Получить статус заказа по ID
    show_title("Получить статус заказа по ID")
    print(mt_order.get_order_status(
        token=token,
        order_id=40458
    ))

