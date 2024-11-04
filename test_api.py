import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.API import API


api = API("https://web-gate.chitai-gorod.ru/api")

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
# Позитивные тесты

def test_search(driver):
    # поик книг по названию
    product = api.search()
    assert product.status_code == 200

def test_add_product_to_cart(driver):
    # добавить книгу в корзину
    id = 2471823
    product = api.add_product_to_cart(id)
    assert product.status_code == 200

def test_look(driver):
    #  просмотреть корзину
    product = api.look()
    assert product.status_code == 200


def test_change(driver):
    # добавить книгу в корзину
    id = 2471823
    product = api.add_product_to_cart(id)
    assert product.status_code == 200
    # изменить количество одной книги
    id_tovara = 152435896
    quantity = 4
    product = api.change(id_tovara, quantity)
    assert product.status_code == 200

def test_delete(driver):
    # добавить книгу в корзину
    id = 2471823
    product = api.add_product_to_cart(id)
    assert product.status_code == 200
    # удалить книгу из корзины
    id_tovara = 152435896
    product = api.delete(id_tovara)
    assert product.status_code == 204

# Негативные тест 
# указать отрицательное число одной книги
def test_change_negativ(driver):
    # добавить книгу в корзину
    id = 2471823
    product = api.add_product_to_cart(id)
    assert product.status_code == 200
    # изменить количество одной книги = -1
    id_tovara = 152435896
    quantity = -1
    product = api.change(id_tovara, quantity)
    assert product.status_code == 422


    
    
  
