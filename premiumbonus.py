import requests

class PremiumBonusSDK:

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    api = "https://site-v2.apipb.ru/"

    def __init__(self, token, design_id="431a12a7-eefb-4407-bbde-17ee6d115cf7"):

        self.headers.update({"Authorization": token})
        self.design_id = design_id

    # Получить ссылку на карту лояльности
    def card_get_info(self, phone_number):

        api_url = self.api + "card-get-info"
        data = {
            "phone": phone_number,
            "design_id": self.design_id
        }

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Информация о покупателе
    def buyer_info(self, phone_number):
        """
        {
            "identificator": "79251234567",
            "sale_point_id": "02c7b11f-4924-4719-9325-39fbdcd49be4"
        }
        :return
        {
            "success": true,
            "is_registered": true,
            "blocked": false,
            "phone": "79251234567",
            "card_number": "1234567890",
            "name": "Андрей",
            "birth_date": "2000-05-06",
            "gender": "male",
            "email": "buyer@mail.ru",
            "child1_birth_date": "2010-05-06",
            "child1_name": "Андрей",
            "child1_gender": "male",
            "child2_birth_date": "2010-05-06",
            "child2_name": "Андрей",
            "child2_gender": "male",
            "child3_birth_date": "2010-05-06",
            "child3_name": "Андрей",
            "child3_gender": "male",
            "child4_birth_date": "2010-05-06",
            "child4_name": "Андрей",
            "child4_gender": "male",
            "group_id": "b1c9f881-77f8-e8cc-3afe-fe15f0bea1a5",
            "group_name": "Карта 5%",
            "balance": 1000.25,
            "balance_bonus_accumulated": 0,
            "balance_bonus_present": 1000.25,
            "balance_bonus_action": 0,
            "bonus_inactive": 0,
            "bonus_next_activation_text": null,
            "phone_checked": false,
            "is_refused_receive_messages": false,
            "is_refused_receive_emails": false,
            "additional_info": null,
            "init_purchase_count": 10,
            "init_payment_amount": 10000,
            "external_id": "00000000-0000-0000-0000-000000000001",
            "identificator_type": "phone",
            "registration_confirmation_required": false,
            "is_allowed_change_card": true,
            "write_off_confirmation_required": false,
            "logger": "TS7gquUS"
        }
        """

        api_url = self.api + "buyer-info"

        data = {
            "identificator": phone_number,
        }

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Информация о покупателе
    def buyer_info_detail(self, phone_number):
        """
        {
            "identificator": "79251234567",
            "sale_point_id": "02c7b11f-4924-4719-9325-39fbdcd49be4"
        }
        :return
        {
            "success": true,
            "is_registered": true,
            "blocked": false,
            "phone": "79251234567",
            "card_number": "1234567890",
            "name": "Андрей",
            "birth_date": "2000-05-06",
            "gender": "male",
            "email": "buyer@mail.ru",
            "child1_birth_date": "2010-05-06",
            "child1_name": "Андрей",
            "child1_gender": "male",
            "child2_birth_date": "2010-05-06",
            "child2_name": "Андрей",
            "child2_gender": "male",
            "child3_birth_date": "2010-05-06",
            "child3_name": "Андрей",
            "child3_gender": "male",
            "child4_birth_date": "2010-05-06",
            "child4_name": "Андрей",
            "child4_gender": "male",
            "group_id": "b1c9f881-77f8-e8cc-3afe-fe15f0bea1a5",
            "group_name": "Карта 5%",
            "balance": 1000.25,
            "balance_bonus_accumulated": 0,
            "balance_bonus_present": 1000.25,
            "balance_bonus_action": 0,
            "bonus_inactive": 0,
            "bonus_next_activation_text": null,
            "phone_checked": false,
            "is_refused_receive_messages": false,
            "is_refused_receive_emails": false,
            "additional_info": null,
            "init_purchase_count": 10,
            "init_payment_amount": 10000,
            "external_id": "00000000-0000-0000-0000-000000000001",
            "identificator_type": "phone",
            "registration_confirmation_required": false,
            "is_allowed_change_card": true,
            "write_off_confirmation_required": false,
            "logger": "TS7gquUS"
        }
        """

        api_url = self.api + "buyer-info-detail"

        data = {
            "identificator": phone_number,
        }

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)


    # Регистрация покупателя
    def buyer_register(self, phone_number, name, cashier_name="telegram", **kwargs):

        """
        {
          "phone": "79251234567",
          "sale_point_id": "cf969328-0792-a523-16ca-3100816fcce1",
          "group_id": "b1c9f881-77f8-e8cc-3afe-fe15f0bea1a5",
          "referrer_phone": "79001234567",
          "name": "Андрей",
          "registration_channel": "facebook",
          "gender": "male",
          "email": "buyer@mail.ru",
          "birth_date": "2000-05-06",
          "card_number": "1234567890",
          "cashier_name": "Иван Иванов",
          "is_refused_receive_messages": "0",
          "init_payment_amount": "10000",
          "init_purchase_count": "10",
          "child1_birth_date": "2010-05-06",
          "child1_name": "Андрей",
          "child1_gender": "male",
          "child2_birth_date": "2010-05-06",
          "child2_name": "Андрей",
          "child2_gender": "male",
          "child3_birth_date": "2010-05-06",
          "child3_name": "Андрей",
          "child3_gender": "male",
          "child4_birth_date": "2010-05-06",
          "child4_name": "Андрей",
          "child4_gender": "male",
          "external_id": "00000000-0000-0000-0000-000000000001"
        }
        """

        api_url = self.api + "buyer-register"

        data = {
            "phone": phone_number,
            "name": name,
            "cashier_name": cashier_name,
        }

        if bool(kwargs):
            if 'referrer_phone' in kwargs and kwargs['referrer_phone'] is None:
                del kwargs['referrer_phone']

            data.update(**kwargs)

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Изменение покупателя
    def buyer_edit(self, phone_number, **kwargs):

        api_url = self.api + "buyer-edit"

        """
        {
            "phone": "79251234567",
            "group_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "name": "Мария",
            "birth_date": "2000-05-06",
            "gender": "male",
            "email": "buyer@mail.ru",
            "card_number": "1234567890",
            "child1_birth_date": "2010-06-06",
            "child1_name": "Мария",
            "child1_gender": "female",
            "child2_birth_date": "2010-06-06",
            "child2_name": "Мария",
            "child2_gender": "female",
            "child3_birth_date": "2010-06-06",
            "child3_name": "Мария",
            "child3_gender": "female",
            "child4_birth_date": "2010-06-06",
            "child4_name": "Мария",
            "child4_gender": "female",
            "change_phone": "79001234567",
            "phone_checked": true,
            "is_refused_receive_messages": true,
            "is_refused_receive_emails": true
        }
        """

        data = {
            "phone": phone_number,
        }

        if bool(kwargs):
            data.update(kwargs)

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Информация по резерву
    def reserve_info(self, order_guid):
        """
        {
            "external_purchase_id": "1234567890"
        }
        :param order_guid:
        :return:
        {
            "success": true,
            "external_purchase_id": "1234567890",
            "reserve_bonus": 100.5,
            "reserve_expire_at": "2015-01-01 12:00:00+00"
        }
        """

        api_url = self.api + "reserve-info"

        data = {
            "external_purchase_id": order_guid,
        }

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Получение максимального количества бонусов доступного для списания
    def write_off_request(self, phone_number, items, **kwargs):

        api_url = self.api + "write-off-request"

        """
        {
            "phone": "79251234567",
            "sale_point_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff", # Точка продаж
            "discount": 300, # Скидка на покупку (дополнительно к скидкам указанным в товарных позициях)
            "items": [
                {
                    "amount": 1000,
                    "quantity": 1,
                    "external_item_id": "item12345678",
                    "discount": 100, ??? - не понятно зачем
                    "name": "Модельная стрижка", ??? - пока не добавляем
                },
                {
                    "amount": 3000,
                    "barcode": 12345,
                    "quantity": 2,
                    "external_item_id": "item12345679",
                    "discount": 0,
                    "name": "Краска для волос Palette",
                }
            ]
        }

        :return:
        {
            "success": true,
            "balance": 1000, # Бонусный баланс
            "write_off_available": 100, # Максимальное количество бонусов, доступное для списания
            "card_payment_available": 2000, # Максимальная сумма оплаты покупки банковской картой
            "total_discount_external": 70,
            "total_discount_premiumbonus": 20,
            "items": [
                {
                    "amount":1000,
                    "discount_external": 35,
                    "discount_premiumbonus": 10,
                    "write_off_available": 50
                },
                {
                    "amount":1000,
                    "discount_external": 35,
                    "discount_premiumbonus": 10,
                    "write_off_available": 50
                }
            ]
        }
        """

        data = {
            "phone": phone_number,
            "items": self.__items(items)
        }

        if 'poi_guid' in kwargs:
            data.update({"sale_point_id": kwargs.get('poi_guid')})
            del kwargs['poi_guid']

        if bool(kwargs):
            data.update(kwargs)

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Эмуляция проведения покупки
    def purchase_dry_run(self, phone_number, order_guid, items, sale_channel=None, write_off_bonus=None, **kwargs):
        """
        {
            "phone": "79251234567",
            "sale_point_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "external_purchase_id": "1234567890",
            "discount": 300,
            "write_off_bonus": 300.5,
            "reserve_hours": 4,
            "card_payment_amount": 500.75,
            "sale_channel": "facebook",
            "items": [
                {
                    "amount": 1000,
                    "quantity": 1,
                    "discount": 100,
                    "name": "Модельная стрижка",
                    "type": "service",
                    "groups": ["Услуги", "Парикмахерская", "Стрижка"]
                },
                {
                    "amount": 3000,
                    "quantity": 2,
                    "discount": 0,
                    "name": "Краска для волос Palette",
                    "type": "product",
                    "groups": ["Сопутствующие товары", "Краски для волос"]
                }
            ]
        }
        :param phone_number:
        :param sale_point_id:
        :param external_purchase_id:
        :param write_off_bonus:
        :param items:
        :param kwargs:
        :return:
        {
            "success": true,
            "external_purchase_id": "1234567890",
            "total_write_off_bonus": 90.4,
            "total_write_on_bonus": 100.5,
            "total_card_payment": 500.75,
            "total_discount_external": 70,
            "total_discount_premiumbonus": 20,
            "balance": 1000.25,
            "order_code": 123456,
            "items": [
                {
                    "write_off_bonus": 30.5
                    "discount_external": 35,
                    "discount_premiumbonus": 10
                },
                {
                    "write_off_bonus": 60.5
                    "discount_external": 35,
                    "discount_premiumbonus": 10
                }
            ]
        }
        """

        data = {
            "phone": phone_number,
            "external_purchase_id": order_guid,
            "items": self.__items(data=items)
        }

        if sale_channel is not None:
            data.update({"sale_channel": sale_channel})

        if 'poi_guid' in kwargs:
            data.update({"sale_point_id": kwargs.get('poi_guid')})
            del kwargs['poi_guid']

        if write_off_bonus is not None:
            data.update({"write_off_bonus": write_off_bonus})

        if bool(kwargs):
            data.update(kwargs)

        api_url = self.api + "purchase-dry-run"
        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Покупка
    def purchase(self, phone_number, order_guid, items, sale_channel=None, write_off_bonus=None, purchase_status="not_approved", **kwargs):
        """
        {
            "phone": "79251234567",
            "sale_point_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "external_purchase_id": "1234567890",
            "cashier_name": "Кассир 1",
            "waiters_names": ["Официант 1"],
            "discount": 300,
            "write_off_bonus": 300.25,
            "card_payment_amount": 500.75,
            "sale_channel": "facebook",
            "items": [
                {
                    "amount": 1000,
                    "quantity": 1,
                    "discount": 100,
                    "name": "Модельная стрижка",
                    "type": "service",
                    "groups": ["Услуги", "Парикмахерская", "Стрижка"],ccg
                    "tags": ["xxx", "yyy"],
                    "external_item_id": "2176299374986968_0"
                },
                {
                    "amount": 3000,
                    "quantity": 2,
                    "discount": 0,
                    "name": "Краска для волос Palette",
                    "type": "product",
                    "groups": ["Сопутствующие товары", "Краски для волос"],
                    "tags": ["xxx", "yyy"],
                    "external_item_id": "2176299374986968_1"
                }
            ]
        }
        :return:
        {
            "success": true,
            "purchase_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "external_purchase_id": "1234567890",
            "total_write_off_bonus": 90.4,
            "total_write_on_bonus": 100.5,
            "total_card_payment": 500.75,
            "total_discount_external": 70,
            "total_discount_premiumbonus": 20,
            "balance": 1000.25,
            "items": [
                {
                    "write_off_bonus": 30.5,
                    "discount_external": 35,
                    "discount_premiumbonus": 10
                },
                {
                    "write_off_bonus": 60.5,
                    "discount_external": 35,
                    "discount_premiumbonus": 10
                }
            ],
            "print_on_check": "Бонусный баланс:\nНачислено: 198 бон.\nСписано: 20 бон.\nУ вас: 973 бон."
        }
        """

        data = {
            "phone": phone_number,
            "external_purchase_id": order_guid,
            "purchase_status": purchase_status,
            "items": self.__items(data=items)
        }

        if sale_channel is not None:
            data.update({"sale_channel": sale_channel})

        if 'poi_guid' in kwargs:
            data.update({"sale_point_id": kwargs.get('poi_guid')})
            del kwargs['poi_guid']

        if write_off_bonus is not None:
            data.update({"write_off_bonus": write_off_bonus})

        api_url = self.api + "purchase"
        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Изменение покупки
    def edit_purchase(self, order_guid, purchase_status, items):

        """
        {
            "external_purchase_id": "1234567890",
            "sale_point_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "discount": 300,
            "write_off_bonus": 300.5,
            "card_payment_amount": 405.20,
            "items": [
                {
                    "amount": 1000,
                    "quantity": 1,
                    "discount": 100,
                    "name": "Модельная стрижка",
                    "type": "service",
                    "groups": ["Услуги", "Парикмахерская", "Стрижка"]
                },
                {
                    "amount": 3000,
                    "quantity": 2,
                    "discount": 0,
                    "name": "Краска для волос Palette",
                    "type": "product",
                    "groups": ["Сопутствующие товары", "Краски для волос"]
                }
            ]
        }

        :return:
        {
            "success": true,
            "purchase_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "external_purchase_id": "1234567890",
            "total_write_off_bonus": 90.4,
            "total_write_on_bonus": 100.5,
            "total_card_payment": 405.20,
            "balance": 1000.25,
            "items": [
                {
                    "write_off_bonus": 30.5
                },
                {
                    "write_off_bonus": 60.5
                }
            ]
        }

        """

        data = {
            "external_purchase_id": order_guid,
            "purchase_status": purchase_status,
            "items": self.__items(data=items)
        }

        api_url = self.api + "edit-purchase"
        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Отмена покупки
    def cancel_purchase(self, order_guid):
        """
        {
            "external_purchase_id": "1234567890" # Идентификатор покупки в вашей системе
        }
        :param order_guid:
        :return:
        {
            "success": true
        }
        """

        api_url = self.api + "cancel-purchase"

        data = {
            "external_purchase_id": order_guid
        }

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    # Изменение статуса покупки
    def confirm_order(self, order_guid):
        """
        {
            "external_purchase_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "purchase_status": "approved"
        }
        :param order_guid:
        :return:
        {
            "success": true,
            "purchase_id": "3f04c71b-fbd7-4310-a84b-6fd34f0bd8ff",
            "external_purchase_id": null,
            "total_write_on_bonus": 100,
            "purchase_status": "approved"
        }
        """

        api_url = self.api + "change-purchase-status"

        data = {
            "external_purchase_id": order_guid,
            "purchase_status": "approved",
        }

        response = requests.post(url=api_url, headers=self.headers, json=data)

        return self.__validate(response=response, params=data)

    def __items(self, data):

        result = []
        for row in data:
            result.append({
                "amount": float(row['product_price']) * int(row['value']),
                "quantity": row['value'],
                "external_item_id": str(row['product_id']),
            })

        return result

    def __validate(self, response, params):

        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                return data
            else:
                print("status_code", response.status_code)
                print("headers", self.headers)
                print("params", params)
                print("response", data)
        else:
            print(response.status_code, response.text)