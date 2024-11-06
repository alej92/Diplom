import allure
import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzEwNjI2NjcsImlhdCI6MTczMDg5NDY2NywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjZjMzliZTRhMDc2NGNjNzhiNjJiODViNGFkNDE2MDZjMmQ4OWQwMjk3YjE3ZDcxNzJiMmEzMWJkNzUwMTJlOTYiLCJ0eXBlIjoxMH0.BHbY-nyDDZqQ9FUGVWmqMbhpQCyrcRaZ13mnIsd0LDs"

my_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

class API:

    def __init__(self, url):
        self.url = url

    @allure.step("АПИ.Поиск книги по названию")
    def search(self) -> list:
        """
        Поиск книги по названию.
        :my_params: Данные о товаре, который нужно искать, указать phrase.
        :return: Возвращается список книг.
        """
        my_params = {
            "customerCityId": "213",
            "phrase": "%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0%20%D0%B8%20%D0%BC%D0%B8%D1%80",
            "products%5Bpage%5D": "1",
            "products%5Bper-page%5D": "48",
            "sortPreset": "relevance"
        }
        resp = requests.get(self.url + '/v2/search/product', headers=my_headers, params=my_params)
        return resp
    

    @allure.step("АПИ.Добавление книги в корзину по id={id}")
    def add_product_to_cart(self, id: int):
        """
        Добавление товара в корзину.
        :id_book: Данные о товаре, который нужно добавить в корзину.
        :return: Товар добавлен в корзину.
        """
        id_book = {
            "id": id,
            "adData": {
                "item_list_name": "search",
                "product_shelf": ""
            }
        }
        resp = requests.post(self.url + '/v1/cart/product', headers=my_headers, json=id_book)
        return resp
    
    @allure.step("АПИ.Просмотреть корзину")
    def look(self) -> list:
        """
        Просмотр корзины.
        :return: Возвращается список товаров, которые есть в корзине.
        """
        list = requests.get(self.url + '/v1/cart', headers=my_headers)
        return list

    @allure.step("АПИ.Изменить количество товара по id={id_tovara} на количество {quantity}")
    def change(self, id_tovara: int, quantity: int) -> list:
        """
        Изменение количества товара.
        :id_book: Ввести данные о книге: id товара и quantity
        :return: Возвращается список товаров с изменненым количеством.
        """
        id_book = [{
            "id": id_tovara,
            "quantity": quantity
            }]
        resp = requests.put(self.url + '/v1/cart', headers=my_headers, json=id_book)
        return resp

    @allure.step("АПИ.Удалить книгу из корзины по {id_tovara}")
    def delete(self, id_tovara: int) -> list:
        """
        Удаление товара.
        Для удаления книги нужно передать id товара
        :return: Возвращается пустой список
        """
        resp = requests.delete(self.url + '/v1/cart/product/' + str(id_tovara), headers=my_headers)
        return resp
