import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.UI import UI


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_proverka_nomera(driver):
    chitai_gorod = UI(driver)
    chitai_gorod.proverka_nomera()
    number = chitai_gorod.proverka_nomera()
    assert number == "8 (495) 424-84-44"

def test_poisk_knigi(driver):
    chitai_gorod = UI(driver)
    chitai_gorod.search("анжелика маркиза ангелов")
    chitai_gorod.proverka_knigi()
    kniga = chitai_gorod.proverka_knigi()
    assert kniga == "Анжелика - маркиза ангелов"

def test_color_katalog(driver):
    chitai_gorod = UI(driver)
    chitai_gorod.color_katalog()
    color = chitai_gorod.color_katalog()
    assert color == "rgba(0, 73, 156, 1)"

def test_aktsii(driver):
    chitai_gorod = UI(driver)
    chitai_gorod.knopka_kabinet()
    chitai_gorod.proverka_kabinet()
    kabinet = chitai_gorod.proverka_kabinet()
    assert kabinet == "Вход и регистрация"

def test_rasprodazha(driver):
    chitai_gorod = UI(driver)
    chitai_gorod.rasp()
    chitai_gorod.proverka_rasp()
    rasprodazha = chitai_gorod.proverka_rasp()
    assert rasprodazha == "СКИДКИ И АКЦИИ"
