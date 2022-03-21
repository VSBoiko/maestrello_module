import requests

from classes.MaestrelloBasic import MaestrelloBasic


class MaestrelloSDK (MaestrelloBasic):
    def create_order_payment(self, token: str, order_id: int):
        """
        Оплата заказа

        https://pizzamaestrello.com/api.php/p/v1/pay-order?
            access_token=6468ebad4ffd727212661f412552edc2ee3&
            id=23956

        :return:
        """
        pass


    # Расчет скидок
    def calc_discount(self):
        pass
