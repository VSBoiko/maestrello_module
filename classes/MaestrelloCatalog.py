import requests

from MaestrelloBasic import MaestrelloBasic


class MaestrelloCatalog (MaestrelloBasic):
    def __init__(self):
        super().__init__()
        self.__all_categories = self.get_via_api_categories()
        self.__all_products = self.get_via_api_products()
        self.__all_modifiers = self.get_via_api_modifiers()

    def get_all_categories(self):
        """
        Получить список всех категорий

        :return:
        Возвращает список категорий:
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

        return self.__all_categories

    def get_all_modifiers(self):
        """
        Получить список всех модификаторов (дополнений) к товарам

        :return:
        Возвращает список модификаторов (дополнений) к товарам:
        [
            {
                "id": "2",
                "name": "Салями (30г)",
                "description": null,
                "price": "200.0000",
                "currency": "RUB",
                "variant_id": "2",
                "tax_id": "0",
                "sort": "15"
            },
            {
                "id": "3",
                "name": "Семга (45г)",
                "description": null,
                "price": "300.0000",
                "currency": "RUB",
                "variant_id": "4",
                "tax_id": "0",
                "sort": "16"
            },
            ...
        ]
        """

        mods = self.__all_modifiers
        return mods["services"] if "services" in mods else []

    def get_all_products(self):
        """
        Получить список всех товаров

        :return:
        Возвращает список товаров:
        [
            {
              "id": "62",
              "name": "Amore / Аморе",
              "summary": "моцарелла, соус из тунца, свежий тунец татаки с
                кунжутом, оливки, перчик из Перу, салат фризе, оливковое масло",
              "meta_title": "",
              "meta_keywords": "",
              "meta_description": "",
              "description": "",
              "contact_id": "1",
              "create_datetime": "2021-02-14 02:09:17",
              "edit_datetime": "2021-05-06 10:36:48",
              "status": "0",
              "type_id": "2",
              "image_id": "62",
              "image_filename": "",
              "video_url": null,
              "sku_id": "65",
              "ext": "jpeg",
              "url": "amore",
              "rating": 0,
              "price": 690,
              "compare_price": 0,
              "currency": "RUB",
              "min_price": 690,
              "max_price": 690,
              "tax_id": null,
              "count": "0",
              "cross_selling": null,
              "upselling": null,
              "rating_count": "0",
              "total_sales": 26910,
              "category_id": "1",
              "badge": "<div class=\"badge-gourmet\"></div>",
              "sku_type": "0",
              "base_price_selectable": 0,
              "compare_price_selectable": "0.0000",
              "purchase_price_selectable": "0.0000",
              "sku_count": "1",
              "total_sales_html": "<span class=\"nowrap\">26 910 <span class=\"ruble\">Р</span></span>",
              "rating_html": "<span class=\"rate nowrap\" title=\"Средняя оценка покупателей: 0 / 5\">
                <i class=\"icon10 star-empty\"></i><i class=\"icon10 star-empty\"></i>
                <i class=\"icon10 star-empty\"></i><i class=\"icon10 star-empty\"></i>
                <i class=\"icon10 star-empty\"></i></span>",
              "image_url": "https://pizzamaestrello.com/wa-data/public/shop/products/62/00/62/
                images/62/62.200x0.jpeg"
            },
            ...
        ]
        """

        prods = self.__all_products
        return prods["products"] if "products" in prods else []

    def get_category(self, category_id: int):
        """
        Получить категорию

        :param category_id: ID категории

        :return:
        Возвращает категорию:
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
        }
        """

        all_categories = self.get_all_categories()
        for category in all_categories:
            if category["id"] == str(category_id):
                return category
        return dict()

    def get_modifier(self, modifier_id: int):
        """
        Получить модификатор (дополнение) к товару

        :param modifier_id: ID модификатора

        :return:
        Возвращает модификатор (дополнение) к товару:
        {
            "id": "2",
            "name": "Салями (30г)",
            "description": null,
            "price": "200.0000",
            "currency": "RUB",
            "variant_id": "2",
            "tax_id": "0",
            "sort": "15"
        }
        """

        all_modifiers = self.get_all_modifiers()
        for modifier in all_modifiers:
            if modifier["id"] == str(modifier_id):
                return modifier
        return dict()

    def get_product(self, product_id: int):
        """
        Получить товар

        :param product_id: ID товара

        :return:
        Возвращает товар:
        {
          "id": "62",
          "name": "Amore / Аморе",
          "summary": "моцарелла, соус из тунца, свежий тунец татаки с
            кунжутом, оливки, перчик из Перу, салат фризе, оливковое масло",
          "meta_title": "",
          "meta_keywords": "",
          "meta_description": "",
          "description": "",
          "contact_id": "1",
          "create_datetime": "2021-02-14 02:09:17",
          "edit_datetime": "2021-05-06 10:36:48",
          "status": "0",
          "type_id": "2",
          "image_id": "62",
          "image_filename": "",
          "video_url": null,
          "sku_id": "65",
          "ext": "jpeg",
          "url": "amore",
          "rating": 0,
          "price": 690,
          "compare_price": 0,
          "currency": "RUB",
          "min_price": 690,
          "max_price": 690,
          "tax_id": null,
          "count": "0",
          "cross_selling": null,
          "upselling": null,
          "rating_count": "0",
          "total_sales": 26910,
          "category_id": "1",
          "badge": "<div class=\"badge-gourmet\"></div>",
          "sku_type": "0",
          "base_price_selectable": 0,
          "compare_price_selectable": "0.0000",
          "purchase_price_selectable": "0.0000",
          "sku_count": "1",
          "total_sales_html": "<span class=\"nowrap\">26 910 <span class=\"ruble\">Р</span></span>",
          "rating_html": "<span class=\"rate nowrap\" title=\"Средняя оценка покупателей: 0 / 5\">
            <i class=\"icon10 star-empty\"></i><i class=\"icon10 star-empty\"></i>
            <i class=\"icon10 star-empty\"></i><i class=\"icon10 star-empty\"></i>
            <i class=\"icon10 star-empty\"></i></span>",
          "image_url": "https://pizzamaestrello.com/wa-data/public/shop/products/62/00/62/
            images/62/62.200x0.jpeg"
        }
        """

        all_products = self.get_all_products()
        for product in all_products:
            if product["id"] == str(product_id):
                return product
        return dict()

    def get_via_api_categories(self, parent_id: int = 0, depth: int = None):
        """
        Получить список категорий через API

        GET https://pizzamaestrello.com/api.php/p/v1/categories?
            parent_id=0&
            depth=1

        :param (не обязательный) parent_id: ID категории, которая должна считаться корнем дерева.
        :param (не обязательный) depth: Количество уровней дерева, которые необходимо получить.
            Если не указано, то метод возвращает все дерево категорий

        :return:
        Возвращает список категорий:
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

    def get_via_api_modifiers(self):
        """
        Получить список модификаторов (дополнений) к товарам через API

        GET https://pizzamaestrello.com/api.php/p/v1/product-type-services?
            id=2
        Accept: application/json

        :return:
        Возвращает словарь со списоком модификаторов (дополнений) к товарам:
        {
            "services": [
                {
                    "id": "2",
                    "name": "Салями (30г)",
                    "description": null,
                    "price": "200.0000",
                    "currency": "RUB",
                    "variant_id": "2",
                    "tax_id": "0",
                    "sort": "15"
                },
                {
                    "id": "3",
                    "name": "Семга (45г)",
                    "description": null,
                    "price": "300.0000",
                    "currency": "RUB",
                    "variant_id": "4",
                    "tax_id": "0",
                    "sort": "16"
                },
                ...
            ]
        }
        """

        api_url = f'{self.api}product-type-services'

        response = requests.get(url=api_url, headers=self.headers, params=[])
        return self.__validate(response=response, params=[])

    def get_via_api_products(self):
        """
        Получить список товаров через API (параметры запроса не работают, поэтому
        пока все товары)

        GET https://pizzamaestrello.com/api.php/p/v1/products?
            offset=2&
            limit=1&
            hash=search/status=1
        Accept: application/json

        :return:
        Возвращает словарь с количеством товаров и списоком этих товаров:
        {
          "count": 40,
          "products": [
            {
              "id": "62",
              "name": "Amore / Аморе",
              "summary": "моцарелла, соус из тунца, свежий тунец татаки с
                кунжутом, оливки, перчик из Перу, салат фризе, оливковое масло",
              "meta_title": "",
              "meta_keywords": "",
              "meta_description": "",
              "description": "",
              "contact_id": "1",
              "create_datetime": "2021-02-14 02:09:17",
              "edit_datetime": "2021-05-06 10:36:48",
              "status": "0",
              "type_id": "2",
              "image_id": "62",
              "image_filename": "",
              "video_url": null,
              "sku_id": "65",
              "ext": "jpeg",
              "url": "amore",
              "rating": 0,
              "price": 690,
              "compare_price": 0,
              "currency": "RUB",
              "min_price": 690,
              "max_price": 690,
              "tax_id": null,
              "count": "0",
              "cross_selling": null,
              "upselling": null,
              "rating_count": "0",
              "total_sales": 26910,
              "category_id": "1",
              "badge": "<div class=\"badge-gourmet\"></div>",
              "sku_type": "0",
              "base_price_selectable": 0,
              "compare_price_selectable": "0.0000",
              "purchase_price_selectable": "0.0000",
              "sku_count": "1",
              "total_sales_html": "<span class=\"nowrap\">26 910 <span class=\"ruble\">Р</span></span>",
              "rating_html": "<span class=\"rate nowrap\" title=\"Средняя оценка покупателей: 0 / 5\">
                <i class=\"icon10 star-empty\"></i><i class=\"icon10 star-empty\"></i>
                <i class=\"icon10 star-empty\"></i><i class=\"icon10 star-empty\"></i>
                <i class=\"icon10 star-empty\"></i></span>",
              "image_url": "https://pizzamaestrello.com/wa-data/public/shop/products/62/00/62/
                images/62/62.200x0.jpeg"
            },
            ...
          ]
        }
        """

        api_url = f'{self.api}products'

        response = requests.get(url=api_url, headers=self.headers, params=[])
        return self.__validate(response=response, params=[])
