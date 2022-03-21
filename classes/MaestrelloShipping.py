import requests

from classes.MaestrelloBasic import MaestrelloBasic


class MaestrelloShipping (MaestrelloBasic):
    def __init__(self):
        super().__init__()
        pass

    def calc_shipping(self, token: str, user_id: int, basket: list,
                      payment_id: int, shipping_id: int, person_count: int = 1,
                      change_with: int = 0, comment: str = ""):
        """
        POST
        https://pizzamaestrello.com/api.php/p/v1/calc-shipping?
            access_token=6468ebad4ffd727212661f412552edc2ee3

        Body:
        {
            "contact_id": "21266",
            "comment": "TEST TEST TEST TEST",
            "shipping": "300.0000",             (можно не передавать)
            "params": {
                "payment_id": "13",
                "payment_params_change": "3333",
                "shipping_address.city": "Москва",
                "shipping_address.country": "rus",
                "shipping_address.dom": "38",
                "shipping_address.etazh": "3",
                "shipping_address.kod-domofona": "3",
                "shipping_address.kvartira": "3",
                "shipping_address.podezd": "3",
                "shipping_address.region": "77",
                "shipping_address.street": "Хромова",
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
                        }
                    ]
                }
            ]
        }
        """
        pass

    def create_shipping_address(self, city: str = "", street: str = "", house_number: str = "",
                                flat: str = "", entrance: str = "", region: str = "",
                                country: str = "rus", floor: str = "", intercom_code: str = ""):
        address = {
            "shipping_address.city": city,
            "shipping_address.street": street,
            "shipping_address.dom": house_number,
            "shipping_address.kvartira": flat,
            "shipping_address.podezd": entrance,
            "shipping_address.region": region,
            "shipping_address.country": country,
            "shipping_address.etazh": floor,
            "shipping_address.kod-domofona": intercom_code,
        }

        return address


if __name__ == "__main__":
    def show_title(text):
        print(f"\n\n{text}\n")

    mt_shipping = MaestrelloShipping()

    # Составить словарь с адресом для заказа
    show_title("Составить словарь с адресом для заказа")
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
    print(ad)
