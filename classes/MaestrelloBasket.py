from copy import deepcopy

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
            if quan > 0:
                item["quantity"] = quan
                self._basket_update(str(sku_id), item)
            else:
                self.delete_product(sku_id)

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
        self.__basket.pop(key, False)


if __name__ == "__main__":

    def show_title(text):
        print(f"\n\n{text}\n")

    mt_basket = MaestrelloBasket()
    mt_basket.add_product(21, 7)
    mt_basket.add_product(25, 10)
    mt_basket.add_product_mod(21, 17)
    mt_basket.add_product_mod(21, 18)
    mt_basket.add_product_mod(25, 19)

    # Добавить товар с ID 21 в корзину в количестве 5 единиц
    show_title("Добавить товар в корзину в количестве 5 единиц")
    basket = deepcopy(mt_basket)
    product_id = 10
    quantity = 3
    print("Корзина", basket.get_basket())
    basket.add_product(product_id, quantity)
    print(f"Добавлен товара (id = {product_id}) в количестве {quantity} единиц")
    print("Корзина", basket.get_basket())

    # Добавить модификатор товару с ID 21 в корзине
    show_title("Добавить модификатор товару в корзине")
    basket = deepcopy(mt_basket)
    product_id = 21
    mod_id = 15
    print("Корзина", basket.get_basket())
    basket.add_product_mod(product_id, mod_id)
    print(f"Добавлен модификатор (id = {mod_id}) для товара (id = {product_id})")
    print("Корзина", basket.get_basket())

    # Добавить количество товара в корзине
    show_title("Добавить количество товару в корзине")
    basket = deepcopy(mt_basket)
    product_id = 21
    add = 7
    print("Корзина", basket.get_basket())
    basket.add_quantity(product_id, add)
    print(f"Добавлено {add} единиц товара (id = {product_id})")
    print("Корзина", basket.get_basket())

    # Убрать количество товара с ID 21 в корзине
    show_title("Убрать количество товара в корзине")
    basket = deepcopy(mt_basket)
    product_id = 21
    remove = 2
    print("Корзина", basket.get_basket())
    basket.remove_quantity(product_id, remove)
    print(f"Убрано {remove} единиц товара (id = {product_id})")
    print("Корзина", basket.get_basket())

    # Убрать модификатор товара в корзине
    show_title("Убрать модификатор товара в корзине")
    basket = deepcopy(mt_basket)
    product_id = 21
    mod_id = 17
    print("Корзина", basket.get_basket())
    basket.delete_product_mod(product_id, mod_id)
    print(f"Удален модификатов (id = {mod_id}) товара (id = {product_id})")
    print("Корзина", basket.get_basket())

    # Убрать все модификаторы товара в корзине
    show_title("Убрать все модификаторы товара в корзине")
    basket = deepcopy(mt_basket)
    product_id = 21
    print("Корзина", basket.get_basket())
    basket.delete_product_mods(product_id)
    print(f"Удалены все модификаторы товара (id = {product_id})")
    print("Корзина", basket.get_basket())

    # Получить корзину в формате для заказа
    show_title("Получить корзину в формате для заказа")
    basket = deepcopy(mt_basket)
    print(basket.get_basket_for_order())

    # Удалить товар из корзины
    show_title("Удалить товар из корзины")
    basket = deepcopy(mt_basket)
    product_id = 25
    print("Корзина", basket.get_basket())
    basket.delete_product(product_id)
    print(f"Удален товар (id = {product_id})")
    print("Корзина", basket.get_basket())

    # Убрать заведомо большое количество одного товара (будет удален из корзины)
    show_title("Убрать заведомо большое количество одного товара (будет удален из корзины)")
    basket = deepcopy(mt_basket)
    product_id = 21
    quantity = 1000
    print("Корзина", basket.get_basket())
    basket.remove_quantity(product_id, quantity)
    print(f"Убрано {quantity} единиц товара (id = {product_id})")
    print("Корзина", basket.get_basket())

    # Очистить корзину
    show_title("Очистить корзину")
    basket = deepcopy(mt_basket)
    print("Корзина", basket.get_basket())
    basket.clear_basket()
    print(f"Корзина очищена")
    print("Корзина", basket.get_basket())
