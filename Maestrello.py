import requests


class MaestrelloSDK:
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    api = "https://pizzamaestrello.com/api.php/p/v1/"

    def __init__(self):
        pass

    # Авторизация и восстановление пароля
    def user_registration(self, firstname: str, lastname: str, email: str, phone: str):
        """
        Регистрация

        POST https://pizzamaestrello.com/api.php/p/v1/register
        Accept: application/json
        Body:
        {
            "name": "Ivan Petrov",
            "firstname": "Ivan",
            "lastname": "Petrov",
            "email": "9@ew.ru",
            "phone": "892839289832"
        }

        :return:
        {
            "id": "20992",
            "name": "Ivan Petrov",
            "login": "9@eew.ru",
            "is_user": "0",
            "password": "3Y5EdaC@Xx1"
        }
        or
        {
            "error": "invalid_method",
            "error_description": "User exist!"
        }
        """

        api_url = f'{self.api}register'
        data = {
            "name": f'{firstname} {lastname}',
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone
        }

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    def user_auth(self, login: str, password: str):
        """
        Авторизация

        GET https://pizzamaestrello.com/api.php/p/v1/auth?
            login={user_login}&
            password={user_password}
        Accept: application/json

        :return:
        {
            "id": "21266",
            "name": "Petrov Ivan",
            "login": "a.volkov@maestrello.ru",
            "is_user": "0",
            "token": "6468ebad4ffd727212661f412552edc2ee3"
        }
        or
        {
            "error": "invalid_request",
            "error_description": "Login or Password incorrect"
        }

        При успешной авторизации возвращаются данные о пользователе и токен для общения с API.
        При не успешной авторизации вернется ошибка с описанием.
        """

        api_url = f'{self.api}auth'
        params = {
            "login": login,
            "password": password,
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    def pass_recovery_link_request(self, login: str):
        """
        Восстановление пароля стадия запроса ссылки

        GET https://pizzamaestrello.com/api.php/p/v1/recover?
            login=email@pizzamaestrello.com&
            channel_type=email
        Accept: application/json

        :return:
        {
            "channel_type": "email",
            "sent_message": "Проверьте новую почту для адреса
                <strong>email@pizzamaestrello.com</strong> —
                мы отправили вам сообщение со ссылкой для восстановления пароля.",
            "timeout_message": "",
            "timeout": 0,
            "address": "email@pizzamaestrello.com",
            "contact_id": 30003,
            "login": "email@pizzamaestrello.com"
        }
        """

        api_url = f'{self.api}recover'
        params = {
            "login": login,
            "channel_type": "email",
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    def pass_recovery_new_pass(self, login: str, token: str):
        """
        Восстановление пароля стадия генерации нового пароля

        GET https://pizzamaestrello.com/api.php/p/v1/recover?
            login=email@pizzamaestrello.com&
            key=de37c5e85aad9b2726b224b0ba4e88a38&
            channel_type=email
        Accept: application/json
        :return:
        {
            "generated_password_sent": true,
            "used_address": "email@pizzamaestrello.com",
            "generated_password_sent_message": "Готово!
                На email-адрес <strong>email@pizzamaestrello.com</strong>
                отправлено письмо с новым паролем для входа."
        }
        """

        api_url = f'{self.api}recover'
        params = {
            "login": login,
            "key": token,
            "channel_type": "email",
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    # Профиль
    def get_user_profile(self, token: str):
        """
        Загрузка профиля пользователя

        GET https://pizzamaestrello.com/api.php/p/v1/get-profile?
            access_token=6468ebad4ffd727212661f412552edc2ee3

        :return:
        {
            "id": "21266",
            "name": "Ivan Petrov",
            "login": "a.volkov@maestrello.ru",
            "email": [
                {
                    "value": "a.volkov@maestrello.ru",
                    "ext": "",
                    "status": "unknown"
                }
            ],
            "address": [
                {
                    "data": {
                        "kvartira": "22",
                        "podezd": "2",
                        "dom": "3",
                        "street": "Ленинский проспект",
                        "city": "Москва",
                        "region": "77",
                        "country": "rus"
                    },
                    "ext": "shipping"
                },
                {
                    "data": {
                        "street": "8е Марта",
                        "dom": "30",
                        "kvartira": "2",
                        "city": "Москва",
                        "region": "77",
                        "country": "rus",
                        "etazh": "1"
                    },
                    "ext": "shipping"
                }
            ],
            "phone": [
                {
                    "value": "89299082303",
                    "ext": "",
                    "status": null
                }
            ]
        }
        """

        api_url = f'{self.api}get-profile'
        params = {
            "access_token": token,
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    def upd_user_name(self, token: str, firstname: str, lastname: str):
        """
        Обновление имени

        POST https://pizzamaestrello.com/api.php/p/v1/update-profile?
            access_token=6468ebad4ffd727212661f412552edc2ee3
        Body:
        {
            "name": "Ivan Petrovi",
        }

        :return:
        Успешный Ответ

        {
            "success": true
        }

        Ошибка
        {
            "success": false,
            "errors": [ @массив строк с ошибками ]
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_user_profile(token)
        data["name"] = f'{firstname} {lastname}'

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)

        return self.__validate(response=response, params={"params": params, "json": data})

    def upd_user_email(self, token: str, email: str, ext: str = "", status: str = None):
        """
        Обновление почты (он же логин)

        POST https://pizzamaestrello.com/api.php/p/v1/update-profile?
            access_token=6468ebad4ffd727212661f412552edc2ee3
        Body:
        {
            "login": "a.volkov@maestrello.ru",
            "email": [
                {
                    "value": "a.volkov@maestrello.ru",
                    "ext": "",
                    "status": "unknown"
                }
            ]
        }

        :return:
        Успешный Ответ

        {
            "success": true
        }

        Ошибка
        {
            "success": false,
            "errors": [ @массив строк с ошибками ]
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_user_profile(token)
        data["email"] = [
            {
                "value": email,
                "ext": ext,
                "status": status
            }
        ]

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)

        return self.__validate(response=response, params={"params": params, "json": data})

    def upd_user_phone(self, token: str, phone: str, ext: str = "", status: str = None):
        """
        Обновление номера телефона

        POST https://pizzamaestrello.com/api.php/p/v1/update-profile?
            access_token=6468ebad4ffd727212661f412552edc2ee3
        Body:
        {
            "phone": [
                {
                    "value": "89299082303",
                    "ext": "",
                    "status": null
                }
            ]
        }

        :return:
        Успешный Ответ

        {
            "success": true
        }

        Ошибка
        {
            "success": false,
            "errors": [ @массив строк с ошибками ]
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_user_profile(token)
        data["phone"] = [
            {
                "value": phone,
                "ext": ext,
                "status": status
            }
        ]

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)

        return self.__validate(response=response, params={"params": params, "json": data})

    def add_user_address(self, token: str, city: str, street: str,
                         house_number: str, flat: str = "", entrance: str = "",
                         region: str = "", country: str = "rus"):
        """
        Добавления адреса

        POST https://pizzamaestrello.com/api.php/p/v1/add-address?
            access_token=6468ebad4ffd727212661f412552edc2ee3
        Body:
        [
            {
                "data": {
                    "kvartira": "104",
                    "podezd": "2",
                    "dom": "32",
                    "street": "Ленинский проспект",
                    "city": "Москва",
                    "region": "77",
                    "country": "rus"
                },
                "ext": "shipping"
            }
        ]
        :return:
        {
            "success": true,
            "address": [
                {
                    "data": {
                        "kvartira": "22",
                        ***
                    },
                    "ext": "shipping"
                },
                {
                    "data": {
                        "street": "8е Марта",
                        ***
                    },
                    "ext": "shipping"
                }
            ]
        }
        """

        api_url = f'{self.api}add-address'
        params = {
            "access_token": token,
        }

        data = [
            {
                "data": {
                    "kvartira": flat,
                    "podezd": entrance,
                    "dom": house_number,
                    "street": street,
                    "city": city,
                    "region": region,
                    "country": country
                },
                "ext": "shipping"
            }
        ]

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)

        return self.__validate(response=response, params={"params": params, "json": data})

    def upd_user_address(self, token: str, address_id: int, city: str = "",
                         street: str = "", house_number: str = "", flat: str = "",
                         entrance: str = "", region: str = "", country: str = "rus"):
        """
        Обновление адреса

        POST https://pizzamaestrello.com/api.php/p/v1/update-profile?
            access_token=6468ebad4ffd727212661f412552edc2ee3
        Body:
        [
            {
                "data": {
                    "kvartira": "104",
                    "podezd": "2",
                    "dom": "32",
                    "street": "Ленинский проспект",
                    "city": "Москва",
                    "region": "77",
                    "country": "rus"
                },
                "ext": "shipping"
                "id": 1
            }
        ]
        :return:
        {
            "success": true,
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_user_profile(token)
        addresses = data["address"]
        for i, adr in enumerate(addresses):
            if adr["id"] == address_id:
                adr_data = adr["data"]
                data["address"][i] = {
                    "data": {
                        "kvartira": flat if flat != "" else adr_data["kvartira"],
                        "podezd": entrance if entrance != "" else adr_data["podezd"],
                        "dom": house_number if house_number != "" else adr_data["dom"],
                        "street": street if street != "" else adr_data["street"],
                        "city": city if city != "" else adr_data["city"],
                        "region": region if region != "" else adr_data["region"],
                        "country": country if country != "" else adr_data["country"]
                    },
                    "ext": adr["ext"],
                    "id": adr["id"]
                }
                break

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)

        return self.__validate(response=response, params={"params": params, "json": data})

    def del_user_address(self, token: str, address_id: int):
        """
        Удаление адреса

        GET https://pizzamaestrello.com/api.php/p/v1/delete-address?
            access_token=6468ebad4ffd727212661f412552edc2ee3&
            id=0

        id - индекс в массиве адресов

        :return:
        {
            "success": true,
            "address": [
                {
                    "data": {
                        "kvartira": "22",
                        ***
                    },
                    "ext": "shipping"
                },
                {
                    "data": {
                        "street": "8е Марта",
                        ***
                    },
                    "ext": "shipping"
                }
            ]
        }
        """

        api_url = f'{self.api}delete-address'
        params = {
            "access_token": token,
            "id": address_id
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    # Категории
    def get_categories(self, parent_id: int = 0, depth: int = None):
        """
        Категории

        GET https://pizzamaestrello.com/api.php/p/v1/categories?
            parent_id=0&
            depth=1

        :param parent_id: Id категории, которая должна считаться корнем дерева.
        :param depth: Количество уровней дерева, которые необходимо получить.
            Если не указано, то метод возвращает все дерево категорий

        :return:
        [
          {
            "id": "8",
            "left_key": "1",
            "right_key": "2",
            "depth": "0",
            "parent_id": "0",
            "name": "Санта пицца",
            "meta_title": "",
            "meta_keywords": "",
            "meta_description": "",
            "type": "0",
            "url": "santa-pizza",
            "full_url": "santa-pizza",
            "count": "5",
            "description": "<p>Стань добрым Сантой - подари пиццу тем,
                кто не может себе её позволить.<br>\r\n\r\nОплати только
                половину пиццы, об остальном позаботимся мы -<br>\r\n\r\n
                вместе сможем больше!</p>",
            "conditions": null,
            "create_datetime": "2020-12-18 03:09:26",
            "edit_datetime": "2020-12-19 02:46:14",
            "filter": null,
            "sort_products": null,
            "include_sub_categories": "0",
            "status": "0",
            "categories": []
          },
          ...
        ]
        """

        api_url = f'{self.api}categories'
        params = {
            "parent_id": parent_id,
        }
        if depth:
            params["depth"] = depth

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    # Статусы заказов
    def get_statuses(self):
        """
        Получить список статусов заказа

        GET https://pizzamaestrello.com/api.php/p/v1/get-order-statuses

        :return:
        """

        api_url = f'{self.api}get-order-statuses'
        response = requests.get(url=api_url, headers=self.headers)

        return self.__validate(response=response, params=None)

    # Создание пользователя после гостевого заказа
    def guest_registation(self, order_id: int):
        """
        Создание пользователя после гостевого заказа

        GET https://pizzamaestrello.com/api.php/p/v1/join?
            id=21799

        :param order_id:

        :return:
        """

        api_url = f'{self.api}join'
        params = {
            "id": order_id,
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)



    # Заказы
    def get_order(self, token: str, order_id: int):
        """
        Заказ по его ID

        GET https://pizzamaestrello.com/api.php/p/v1/get-order?
            id=23997&
            access_token=6468ebad4ffd727212661f412552edc2ee3

        :param token:
        :param order_id:
        :return:
        """

        api_url = f'{self.api}get-order'
        params = {
            "access_token": token,
            "id": order_id
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    def get_orders(self, token, limit: int = 0):
        """
        Массив заказов покупателя

        GET https://pizzamaestrello.com/api.php/p/v1/get-orders?
            access_token=6468ebad4ffd727212661f412552edc2ee3&
            limit=3

        :param token:
        :param limit: лимит записей, сортировка - последние в начале

        :return:
        """

        api_url = f'{self.api}get-orders'
        params = {
            "access_token": token,
            "limit": limit
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    def get_order_status(self, token: str, order_id: int):
        """
        Статус заказа

        https://pizzamaestrello.com/api.php/p/v1/get-order-status?
            id=23997&
            access_token=6468ebad4ffd727212661f412552edc2ee3

        :param token:
        :param order_id:

        :return:
        """

        api_url = f'{self.api}get-order-status'
        params = {
            "access_token": token,
            "id": order_id
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)

        return self.__validate(response=response, params=params)

    # Создание заказа
    def get_order_settings(self):
        """
        Настройки заказа

        GET https://pizzamaestrello.com/api.php/p/v1/order-settings

        :return:
        """

        api_url = f'{self.api}order-settings'
        response = requests.get(url=api_url, headers=self.headers)

        return self.__validate(response=response, params=None)

    def create_order(self, token: str):
        """
        Настройки заказа

        GET https://pizzamaestrello.com/api.php/p/v1/create-order?
            access_token=6468ebad4ffd727212661f412552edc2ee3

        :return:
        """
        pass

    def create_order_payment(self, token: str, order_id: int):
        """
        Оплата заказа

        https://pizzamaestrello.com/api.php/p/v1/pay-order?
            access_token=6468ebad4ffd727212661f412552edc2ee3&
            id=23956

        :return:
        """
        pass

    # Расчет стоимости доставки
    def calc_shipping(self):
        pass

    # Расчет скидок
    def calc_discount(self):
        pass



    def __validate(self, response, params):
        if response.status_code == 200:
            return response.json()

            # data = response.json()
            # if data.get('errors'):
            #     print("status_code", response.status_code)
            #     print("headers", self.headers)
            #     print("params", params)
            #     print("response", data)
            # else:
            #     return data

        else:
            print(response.status_code, response.text)
