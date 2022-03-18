import requests

from MaestrelloBasic import MaestrelloBasic


class MaestrelloCatalog (MaestrelloBasic):
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
