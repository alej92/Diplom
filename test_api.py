import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.API import API

api = API("https://web-gate.chitai-gorod.ru/api")


# Позитивные тесты
@allure.suite("API - тесты")
@allure.title("Поиск товара по названию")
@allure.feature("Поисковая строка")
@allure.description("Тест проверяет работу поисковой строки - ввод текста на русском")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_book_success(driver):
    product = api.search()
    with allure.step("Сравнить статус код"):
        assert product.status_code == 200

@allure.suite("API - тесты")
@allure.title("Добавление товара в корзину")
@allure.feature("Корзина")
@allure.description("Тест проверяет возможность добавление товара в корзину")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_to_cart(driver):
    id = 2471823
    product = api.add_product_to_cart(id)
    with allure.step("Сравнить статус код"):
        assert product.status_code == 200

@allure.suite("API - тесты")
@allure.title("Просмотр корзины")
@allure.feature("Корзина")
@allure.severity(allure.severity_level.MINOR)
def test_view_cart(driver):
    product = api.look()
    with allure.step("Сравнить статус код"):
        assert product.status_code == 200

@allure.suite("API - тесты")
@allure.title("Изменение количества одной книги")
@allure.feature("Корзина")
@allure.description("Тест проверяет изменение количества товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_number_books(driver):
    id = 2471823
    product = api.add_product_to_cart(id)
    with allure.step("Сравнить статус код"):
        assert product.status_code == 200
    id_tovara = 152435896
    quantity = 4    
    product = api.change(id_tovara, quantity)
    with allure.step("Сравнить статус код"):
        assert product.status_code == 200

@allure.suite("API - тесты")
@allure.title("Удаление книги из корзины")
@allure.feature("Корзина")
@allure.description("Тест проверяет удаление товара из корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_book(driver):
    id = 2471823
    product = api.add_product_to_cart(id)
    with allure.step("Сравнить статус код"):
        assert product.status_code == 200
    id_tovara = 152435896    
    product = api.delete(id_tovara)
    with allure.step("Сравнить статус код"):
        assert product.status_code == 204

# Негативный тест

@allure.suite("API - тесты")
@allure.title("Ввод отрицательного значения количество книг(негативняй тест)")
@allure.feature("Корзина")
@allure.description("Тест проверяет изменение количества товара на отрицательное значение")
@allure.severity(allure.severity_level.CRITICAL)
def test_change_number_books_negative(driver):
    id = 2471823    
    product = api.add_product_to_cart(id)
    with allure.step("Сравнить статус код"):
        assert product.status_code == 200
    id_tovara = 152435896
    quantity = -1    
    product = api.change(id_tovara, quantity)
    with allure.step("Сравнить статус код"):
        assert product.status_code == 422


    
    
  
