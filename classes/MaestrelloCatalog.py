import requests

from MaestrelloBasic import MaestrelloBasic


class MaestrelloCatalog (MaestrelloBasic):
    def __init__(self):
        super().__init__()
        self.__all_categories = self.get_via_api_categories()
        self.__all_products = self.get_via_api_products()
        self.__mods = dict()

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

    def get_category_products(self, category_id: int):
        """
        Возвращает товары определенной категории

        :param category_id: ID категории

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

        products = self.get_all_products()
        result = []
        for product in products:
            if product["category_id"] == str(category_id):
                result.append(product)

        return result

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

    def get_product_mods(self, product_id: int):
        """
        Получить список модификаторов (дополнений) к товару

        :param product_id: ID товара

        :return:
        Возвращает список модификаторов (дополнений) к товару:
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

        product = self.get_product(product_id)
        if "type_id" in product:
            return self.get_mods(product["type_id"])
        else:
            return []

    def get_product_sku_id(self, product_id: int):
        """
        Получить ID товарного предложения (SKU) по ID товара

        :param product_id: ID товара

        :return:
        SKU ID (например, 241) или None
        """

        prod = self.get_product(product_id)
        return int(prod["sku_id"]) if "sku_id" in prod else None

    def get_mods(self, product_type_id: int):
        """
        Получить список модификаторов (дополнений) к типу товаров

        :param product_type_id: ID типа товара

        :return:
        Возвращает список модификаторов (дополнений) к типу товаров:
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

        mods = self.__mods
        if str(product_type_id) not in mods:
            new_mods = self.get_via_api_mods(product_type_id)
            mods[str(product_type_id)] = new_mods["services"]

        return mods[str(product_type_id)]

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
        return self._validate(response=response, params=params)

    def get_via_api_mods(self, type_id: int):
        """
        Получить список модификаторов (дополнений) к товарам через API

        GET https://pizzamaestrello.com/api.php/p/v1/product-type-services?
            id=2
        Accept: application/json

        :param type_id: ID типа товара

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
        params = {
            "id": type_id
        }
        response = requests.get(url=api_url, headers=self.headers, params=params)
        return self._validate(response=response, params=params)

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
        return self._validate(response=response, params=[])


if __name__ == "__main__":

    def show_title(text):
        print(f"\n\n{text}\n")

    mt_catalog = MaestrelloCatalog()

    # Получить все категории
    show_title("Получить все категории")
    all_categories = mt_catalog.get_all_categories()
    for i in all_categories:
        print(i["id"], i["name"])

    # Получить категорию по ее ID
    show_title("Получить категорию по ее ID")
    category_id = 4
    category = mt_catalog.get_category(category_id)
    print(f"Категория с ID = {category_id}", category)

    # Получить все товары
    show_title("Получить все товары")
    all_products = mt_catalog.get_all_products()
    for prod in all_products:
        print(prod["type_id"], prod["id"], prod["name"])

    # Получить список товаров по ID категории
    show_title("Получить список товаров по ID категории")
    category_id = 4
    category = mt_catalog.get_category(category_id)
    category_prods = mt_catalog.get_category_products(category_id)
    print(f"Продукты из категории - {category['name']}")
    for prod in category_prods:
        print(prod["category_id"], prod["id"], prod["name"])

    # Получить список модификаторов по ID товара
    show_title("Получить список модификаторов по ID товара")
    product_id = 2
    product = mt_catalog.get_product(product_id)
    product_mods = mt_catalog.get_product_mods(product_id)
    print(f"Модификаторы для продукта - {product['name']}")
    for mod in product_mods:
        print(mod["id"], mod["name"])

    # Получить список модификаторов по типу товара
    show_title("Получить список модификаторов по типу товара")
    prod_type_id = 2
    prod_type_mods = mt_catalog.get_mods(prod_type_id)
    print(f"Модификаторы для типа (ID = {prod_type_id}) продуктов")
    for mod in prod_type_mods:
        print(mod["id"], mod["name"])

    # Получить SKU ID по ID товара
    show_title("Получить SKU ID по ID товара")
    product_id = 2
    prod_sku_id = mt_catalog.get_product_sku_id(product_id)
    print(f"Товар (ID = {product_id}) имеет SKU ID {prod_sku_id}")
