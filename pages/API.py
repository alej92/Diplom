import allure
import requests

class API:

    def __init__(self, url):
        self.url = url

    @allure.step("АПИ.Поиск книги по названию")
    def search(self):
        """
        Поиск книги по названию.

        :my_headers: данные для авторизации
        :my_params: Данные о товаре, который нужно искать.
        :return: Объект Response от API с результатом операции.
        """
        my_headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA4OTMwNzEsImlhdCI6MTczMDcyNTA3MSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg4NTZlYjhhZDE1MGU1ODY4ZWIzYmJiZTAzNDY1NzdiMzYwNmQyMDJiOGVkNjk5MTY4MTIwMTc0M2RiMDE1MWEiLCJ0eXBlIjoxMH0.9rdEKk6g6BBNf7QrIsaEani2xfNGcPBhOYu2_9tvjeU",
            "Content-Type": "application/json"
        }
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

        :my_headers: данные для авторизации
        :id_book: Данные о товаре, который нужно добавить в корзину.
        :return: Объект Response от API с результатом операции.
        """
        my_headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA4OTMwNzEsImlhdCI6MTczMDcyNTA3MSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg4NTZlYjhhZDE1MGU1ODY4ZWIzYmJiZTAzNDY1NzdiMzYwNmQyMDJiOGVkNjk5MTY4MTIwMTc0M2RiMDE1MWEiLCJ0eXBlIjoxMH0.9rdEKk6g6BBNf7QrIsaEani2xfNGcPBhOYu2_9tvjeU",
            "Content-Type": "application/json"
            }
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
    def look(self):
        """
        Просмотр корзины.

        :my_headers: данные для авторизации
        :return: Объект Response от API с результатом операции.
        """
        my_headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA4OTMwNzEsImlhdCI6MTczMDcyNTA3MSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg4NTZlYjhhZDE1MGU1ODY4ZWIzYmJiZTAzNDY1NzdiMzYwNmQyMDJiOGVkNjk5MTY4MTIwMTc0M2RiMDE1MWEiLCJ0eXBlIjoxMH0.9rdEKk6g6BBNf7QrIsaEani2xfNGcPBhOYu2_9tvjeU",
            "Content-Type": "application/json"
            }
        list = requests.get(self.url + '/v1/cart', headers=my_headers)
        return list

    @allure.step("АПИ.Изменить количество товара по id={id_tovara} на количество {quantity}")
    def change(self, id_tovara: int, quantity: int):
        """
        Изменение количества товара.

        :my_headers: данные для авторизации
        :id_book: Данные о товаре, который нужно изменить.
        :return: Объект Response от API с результатом операции.
        """  
        my_headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA4OTMwNzEsImlhdCI6MTczMDcyNTA3MSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg4NTZlYjhhZDE1MGU1ODY4ZWIzYmJiZTAzNDY1NzdiMzYwNmQyMDJiOGVkNjk5MTY4MTIwMTc0M2RiMDE1MWEiLCJ0eXBlIjoxMH0.9rdEKk6g6BBNf7QrIsaEani2xfNGcPBhOYu2_9tvjeU",
            "Content-Type": "application/json"
            }
        id_book = [{
            "id": id_tovara,
            "quantity": quantity
            }]
        resp = requests.put(self.url + '/v1/cart', headers=my_headers, json=id_book)
        return resp
    
    @allure.step("АПИ.Удалить книгу из корзины по {id_tovara}")
    def delete(self, id_tovara: int):
        """
        Удаление товара.

        :my_headers: данные для авторизации
        :return: Объект Response от API с результатом операции.
        """
        my_headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA4OTMwNzEsImlhdCI6MTczMDcyNTA3MSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6Ijg4NTZlYjhhZDE1MGU1ODY4ZWIzYmJiZTAzNDY1NzdiMzYwNmQyMDJiOGVkNjk5MTY4MTIwMTc0M2RiMDE1MWEiLCJ0eXBlIjoxMH0.9rdEKk6g6BBNf7QrIsaEani2xfNGcPBhOYu2_9tvjeU",
            "Content-Type": "application/json"
            }
        resp = requests.delete(self.url + '/v1/cart/product/' + str(id_tovara), headers=my_headers)
        return resp

