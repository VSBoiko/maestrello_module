import requests

from classes.MaestrelloBasic import MaestrelloBasic


class MaestrelloBasket (MaestrelloBasic):
    def __init__(self):
        super().__init__()
        self.__basket = dict()

    def add_product(self, sku_id: int, quantity: int = 1):
        new_item = {
            "sku_id": sku_id,
            "quantity": quantity,
            "services": []
        }

        self._basket_update(str(sku_id), new_item)

    def add_product_mod(self, sku_id: int, mod_id: int):
        basket = self.get_basket()
        if str(sku_id) in basket:
            item = basket.get(str(sku_id))
            new_service = {
                "service_variant_id": str(mod_id)
            }
            item["services"].append(new_service)
            self._basket_update(str(sku_id), item)

    def delete_product(self, sku_id: int):
        self._basket_delete(str(sku_id))

    def delete_product_mod(self, sku_id: int, mod_id: int):
        basket = self.get_basket()
        if str(sku_id) in basket:
            item = basket.get(str(sku_id))

            new_services = []
            for service in item["services"]:
                if service["service_variant_id"] != str(mod_id):
                    new_services.append(service)

            item["services"] = new_services
            self._basket_update(str(sku_id), item)

    def delete_product_mods(self, sku_id: int):
        basket = self.get_basket()
        if str(sku_id) in basket:
            item = basket.get(str(sku_id))
            item["services"] = []
            self._basket_update(str(sku_id), item)

    def add_quantity(self, sku_id: int, how_much_to_add: int = 0):
        basket = self.get_basket()

        if str(sku_id) in basket:
            item = basket.get(str(sku_id))
            item["quantity"] += how_much_to_add
            self._basket_update(str(sku_id), item)
        else:
            self.add_product(sku_id, how_much_to_add)

    def remove_quantity(self, sku_id: int, how_much_to_remove: int = 0):
        basket = self.get_basket()

        if str(sku_id) in basket:
            item = basket.get(str(sku_id))
            quan = item["quantity"] - how_much_to_remove
            item["quantity"] = quan if quan > 0 else 0
            self._basket_update(str(sku_id), item)

    def get_basket(self):
        return self.__basket

    def get_basket_for_order(self):
        basket = self.get_basket()
        order_basket = []
        for item in basket.values():
            order_basket.append(item)

        return order_basket

    def clear_basket(self):
        self.__basket.clear()

    def _basket_update(self, key: str, value):
        self.__basket.update({key: value})

    def _basket_delete(self, key: str):
        self.__basket.pop(key, default=None)


