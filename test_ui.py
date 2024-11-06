import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.UI import UI

@allure.suite("UI- тесты")
@allure.title("Проверка номера горячей линии на главной странице сайта")
@allure.feature("Соответсьвие цвету/тексту")
@allure.description("Тест проверяет соответствие номера горячей линии")
@allure.severity(allure.severity_level.NORMAL)
def test_proverka_nomera(driver):
    with allure.step("Создать экземпляр класс 'UI'"):
        chitai_gorod = UI(driver)
    chitai_gorod.proverka_nomera()
    with allure.step("Добавить номер в переменную"):
        number = chitai_gorod.proverka_nomera()
    with allure.step("Сравнить номер горячей линии"):
        assert number == "8 (495) 424-84-44"

@allure.suite("UI- тесты")
@allure.title("Поиск книги по названию")
@allure.feature("Поисковая строка")
@allure.description("Тест проверяет работу поисковой строки - ввод текста на русском")
@allure.severity(allure.severity_level.CRITICAL)
def test_poisk_knigi(driver):
    with allure.step("Создать экземпляр класс 'UI'"):
        chitai_gorod = UI(driver)
    chitai_gorod.search("анжелика маркиза ангелов")
    chitai_gorod.proverka_knigi()
    with allure.step("Добавить название в переменную"):
        kniga = chitai_gorod.proverka_knigi()
    with allure.step("Сравнить название книги"):
        assert kniga == "Анжелика - маркиза ангелов"

@allure.suite("UI- тесты")
@allure.title("Проверка цвета кнопки 'Каталог'")
@allure.feature("Соответсьвие цвету/тексту")
@allure.description("Тест проверяет соответствие цвета у кнопки 'Каталог'")
@allure.severity(allure.severity_level.MINOR)
def test_color_katalog(driver):
    with allure.step("Создать экземпляр класс 'UI'"):
        chitai_gorod = UI(driver)
    chitai_gorod.color_katalog()    
    with allure.step("Добавить цвет в переменную"):
        color = chitai_gorod.color_katalog()
    with allure.step("Сравнить цвет кнопки"):
        assert color == "rgba(0, 73, 156, 1)"

@allure.suite("UI- тесты")
@allure.title("Перехода на вкладку 'Личный кабинет - Вход и регистрация'")
@allure.feature("Переход на вкладку/страницу")
@allure.description("Тест проверяет переход на вкладку 'Личный кабинет - Вход и регистрация'")
@allure.severity(allure.severity_level.CRITICAL)
def test_personal_account(driver):
    with allure.step("Создать экземпляр класс 'UI'"):
        chitai_gorod = UI(driver)
    chitai_gorod.knopka_kabinet()
    chitai_gorod.proverka_kabinet()
    with allure.step("Добавить название в переменную"):
        kabinet = chitai_gorod.proverka_kabinet()
    with allure.step("Сравнить название вкладки"):
        assert kabinet == "Вход и регистрация"

@allure.suite("UI- тесты")
@allure.title("Перехода на страницу 'СКИДКИ И АКЦИИ'")
@allure.feature("Переход на вкладку/страницу")
@allure.description("Тест проверяет переход на страницу 'СКИДКИ И АКЦИИ'")
@allure.severity(allure.severity_level.CRITICAL)
def test_aktsii(driver):
    with allure.step("Создать экземпляр класс 'UI'"):
        chitai_gorod = UI(driver)
    chitai_gorod.aktsii()
    chitai_gorod.proverka_aktsii()
    with allure.step("Добавить название в переменную"):
        rasprodazha = chitai_gorod.proverka_aktsii()
    with allure.step("Сравнить название страницы"):
        assert rasprodazha == "СКИДКИ И АКЦИИ"
