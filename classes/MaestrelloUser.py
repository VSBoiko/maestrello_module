import requests

from MaestrelloBasic import MaestrelloBasic


class MaestrelloUser(MaestrelloBasic):
    def add_address(self, token: str, city: str, street: str,
                    house_number: str, flat: str = "", entrance: str = "",
                    region: str = "", country: str = "rus"):
        """
        Добавление адреса доставки в профиль пользователя

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

        :param token: токен пользователя для работы с API
        :param city: город
        :param street: улица
        :param house_number: номер дома
        :param (не обязательный) flat: номер квартиры
        :param (не обязательный) entrance:   подъезд
        :param (не обязательный) region: регион
        :param (не обязательный) country: символьный код страны

        :return:
        В случае успеха:
        {
            "success": true,
            "address": [
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
                },
                {
                    "data": {
                        "kvartira": "79",
                        "podezd": "1",
                        "dom": "55",
                        "street": "Красный проспект",
                        "city": "Москва",
                        "region": "77",
                        "country": "rus"
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

    def auth(self, login: str, password: str):
        """
        Авторизация пользователя по логину и паролю

        GET https://pizzamaestrello.com/api.php/p/v1/auth?
            login={user_login}&
            password={user_password}
        Accept: application/json

        :param login: логин пользователя (обычно используется e-mail)
        :param password: пароль

        :return:
        При успешной авторизации возвращаются данные о пользователе и токен для общения с API:
        {
            "id": "21266",
            "name": "Petrov Ivan",
            "login": "a.volkov@maestrello.ru",
            "is_user": "0",
            "token": "6468ebad4ffd727212661f412552edc2ee3"
        }

        При неуспешной авторизации вернется ошибка с описанием:
        {
            "error": "invalid_request",
            "error_description": "Login or Password incorrect"
        }
        """

        api_url = f'{self.api}auth'
        params = {
            "login": login,
            "password": password,
        }

        response = requests.get(url=api_url, headers=self.headers, params=params)
        return self.__validate(response=response, params=params)

    def delete_address(self, token: str, address_id: int):
        """
        Удалить адрес доставки в профиле пользователя

        GET https://pizzamaestrello.com/api.php/p/v1/delete-address?
            access_token=6468ebad4ffd727212661f412552edc2ee3&
            id=0

        :param token: токен пользователя для работы с API
        :param address_id: ID адреса

        :return:
        В случае успеха возвращает доступные адреса:
        {
            "success": true,
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

    def get_profile(self, token: str):
        """
        Получение профиля пользователя

        GET https://pizzamaestrello.com/api.php/p/v1/get-profile?
            access_token=6468ebad4ffd727212661f412552edc2ee3

        :param token: токен пользователя для работы с API

        :return:
        В случае успеха:
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

    def get_token(self, login: str, password: str):
        """
        Получить токен пользователя для работы с API

        * Собственный метод на основе API

        :param login: логин пользователя (обычно используется e-mail)
        :param password: пароль

        :return:
        Токен:
        "6468ebad4ffd727212661f412552edc2ee3"

        В случае ошибки:
        {
            "error": "invalid_request",
            "error_description": "Login or Password incorrect"
        }
        """

        user = self.auth(login, password)
        return user["token"] if "token" in user else user

    def pass_recovery_new_pass(self, login: str, token: str):
        """
        Восстановление пароля, стадия генерации нового пароля

        GET https://pizzamaestrello.com/api.php/p/v1/recover?
            login=email@pizzamaestrello.com&
            key=de37c5e85aad9b2726b224b0ba4e88a38&
            channel_type=email
        Accept: application/json

        :param login: логин пользователя (обычно используется e-mail)
        :param token: токен пользователя для работы с API

        :return:
        В случае успеха:
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

    def pass_recovery_link_request(self, login: str):
        """
        Восстановление пароля, стадия запроса ссылки

        GET https://pizzamaestrello.com/api.php/p/v1/recover?
            login=email@pizzamaestrello.com&
            channel_type=email
        Accept: application/json

        :param login: логин пользователя (обычно используется e-mail)

        :return:
        В случае успеха:
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

    def registration(self, firstname: str, lastname: str, email: str, phone: str):
        """
        Регистрация нового пользователя

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

        :param firstname: имя пользователя
        :param lastname: фамилия пользователя
        :param email: e-mail пользователя (он же логин для входа)
        :param phone: номер телефона пользователя в формате "80000000000"

        :return:
        {
            "id": "20992",
            "name": "Ivan Petrov",
            "login": "9@eew.ru",
            "is_user": "0",
            "password": "3Y5EdaC@Xx1"
        }

        При неуспешной регистрации вернется ошибка с описанием::
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

    def update_address(self, token: str, address_id: int, city: str = "",
                       street: str = "", house_number: str = "", flat: str = "",
                       entrance: str = "", region: str = "", country: str = "rus"):
        """
        Изменить адреса доставки в профиле пользователя

        * Собственный метод на основе API

        :param token: токен пользователя для работы с API
        :param address_id: ID адреса
        :param (не обязательный) city: город
        :param (не обязательный) street: улица
        :param (не обязательный) house_number: номер дома
        :param (не обязательный) flat: номер квартиры
        :param (не обязательный) entrance:   подъезд
        :param (не обязательный) region: регион
        :param (не обязательный) country: символьный код страны

        :return:
        В случае успеха:
        {
            "success": true,
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_profile(token)
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

    def update_email(self, token: str, email: str, ext: str = "", status: str = None):
        """
        Изменение почты (и логина)

        * Собственный метод на основе API

        :param token: токен пользователя для работы с API
        :param email: новый e-mail пользователя
        :param (не обязательный) ext:
        :param (не обязательный) status:

        :return:
        В случае успеха:
        {
            "success": true
        }

        Ошибка:
        {
            "success": false,
            "errors": [ @массив строк с ошибками ]
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_profile(token)
        data["email"] = [
            {
                "value": email,
                "ext": ext,
                "status": status
            }
        ]

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)
        return self.__validate(response=response, params={"params": params, "json": data})

    def update_name(self, token: str, firstname: str, lastname: str):
        """
        Изменить имя пользователя

        * Собственный метод на основе API

        :param token: токен пользователя для работы с API
        :param firstname: новое имя пользователя
        :param lastname: новая фамилия пользователя

        :return:
        В случае успеха:
        {
            "success": true
        }

        Ошибка:
        {
            "success": false,
            "errors": [ @массив строк с ошибками ]
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_profile(token)
        data["name"] = f'{firstname} {lastname}'

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)
        return self.__validate(response=response, params={"params": params, "json": data})

    def update_phone(self, token: str, phone: str, ext: str = "", status: str = None):
        """
        Изменить номер телефона пользователя

        * Собственный метод на основе API

        :param token: токен пользователя для работы с API
        :param phone: новый номер телефона пользователя
        :param (не обязательный) ext:
        :param (не обязательный) status:

        :return:
        В случае успеха:
        {
            "success": true
        }

        Ошибка:
        {
            "success": false,
            "errors": [ @массив строк с ошибками ]
        }
        """

        api_url = f'{self.api}update-profile'
        params = {
            "access_token": token,
        }

        data = self.get_profile(token)
        data["phone"] = [
            {
                "value": phone,
                "ext": ext,
                "status": status
            }
        ]

        response = requests.post(url=api_url, headers=self.headers, params=params, json=data)
        return self.__validate(response=response, params={"params": params, "json": data})
