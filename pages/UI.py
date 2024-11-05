from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class UI:

    def __init__(self, driver):
      self._driver = driver
      self._driver.get("https://www.chitai-gorod.ru")
      self._driver.find_element(
         By.CSS_SELECTOR, "div[class='button change-city__button change-city__button--accept blue']").click()
      self._driver.find_element(
         By.CSS_SELECTOR, "div[class='button change-city__button change-city__button--accept blue']").click()
      self._driver.find_element(
         By.CSS_SELECTOR, "div[class='popmechanic-close']").click()
      self._driver.find_element(
          By.XPATH, '//button[text()="Понятно, закрыть"]').click()
      self._driver.maximize_window()
      self._driver.implicitly_wait(4)


    @allure.step("АПИ-метод. Берет с главной страницы сайта номер телефона")
    def proverka_nomera(self) -> str:
      """
        Проверяет номер телефона горячей линии на главной станице сайта.
        :test: Поиск элемента по локатору - номер телефона.
        :return: Возвращает номер телефона (текстом).
      """
      test = WebDriverWait(self._driver, 4, 0.1)
      test.until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 
                                        ("a[class='header-phone__number']")), '8 (495) 424-84-44')
      )
      result_test = self._driver.find_element(By.CSS_SELECTOR, 
                                              ("a[class='header-phone__number']")).text
      return result_test


    @allure.step("АПИ-метод. Выполнить поиск книги по названию {name} на русском языке")
    def search(self, name: str):
      """
        Ввести в поисковую строку название кники и нажать кнопку поиска.

        Нужно указать локато поисковой строки и кнопки поиска
      """
      self._driver.find_element(By.CSS_SELECTOR, 
                                  "input[enterkeyhint='search']").clear()
      self._driver.find_element(By.CSS_SELECTOR, 
                                  "input[enterkeyhint='search']").send_keys(name)
      self._driver.find_element(By.CSS_SELECTOR, 
                                "button[class='header-search__button']").click()


    @allure.step("АПИ-метод. Берет название первой книги")
    def proverka_knigi(self) -> str:
      """
        Проверяет номер название первой найденной книги.
        :test: Поиск элемента по локатору - название книги
        :return: Возвращает название книги (текстом).
      """
      test = WebDriverWait(self._driver, 4, 0.1)
      test.until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 
                                        ("div[class='product-title__head']")),
                                        'Анжелика - маркиза ангелов')
      )
      result_test = self._driver.find_element(By.CSS_SELECTOR, 
                                              ("div[class='product-title__head']")).text
      return result_test


    @allure.step("АПИ-метод. Берет с главной страницы сайта цвет кнопки 'Каталог'")
    def color_katalog(self) -> str:
      """
        Проверяет цвет кнопки "Каталог".
        :test: Поиск элемента по локатору - цвет кнопки "Каталог".
        :return: Возвращает цвет кнопки (текстом).
      """
      color = self._driver.find_element(By.CSS_SELECTOR, 
                                        "button[class='catalog__button']").value_of_css_property("background-color")
      return color


    @allure.step("АПИ-метод. Нажать на иконку 'Личный кабинет''")
    def knopka_kabinet(self):
      """
        Нажать на иконку "Личный кабинет".
        Нужно указать локато иконки "личный кабинет" и нажать на него
      """
      self._driver.find_element(By.CSS_SELECTOR, 
                                "svg[class='header-profile__icon header-profile__icon--desktop']").click()


    @allure.step("АПИ-метод. Берет название 'Вход и регистрация'")
    def proverka_kabinet(self) -> str:
      """
        Проверяет переход на вкладку "Личный кабинет".
        :test: Поиск элемента по локатору - название вкладки "Вход и регистрация"
        :return: Возвращает название вкладки (текстом).
      """
      test = WebDriverWait(self._driver, 4, 0.1)
      test.until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 
                                        ("h4[class='auth-modal__header']")), 'Вход и регистрация')
      )
      result_test = self._driver.find_element(By.CSS_SELECTOR, 
                                              ("h4[class='auth-modal__header']")).text
      return result_test


    @allure.step("АПИ-метод. Нажать на кнопку 'Акции''")
    def aktsii(self):
      """
        Нажать на кнопку "Акции".
        Нужно указать локато кнопки "Акции" и нажать на него
      """
      self._driver.find_element(By.CSS_SELECTOR, "a[href='/promotions']").click()
      self._driver.find_element(
         By.CSS_SELECTOR, "div[class='popmechanic-close']").click()


    @allure.step("АПИ-метод. Берет название 'СКИДКИ И АКЦИИ''")
    def proverka_aktsii(self) -> str:
      """
        Проверяет переход на страницу "СКИДКИ И АКЦИИ".
        :test: Поиск элемента по локатору - название страницы "СКИДКИ И АКЦИИ"
        :return: Возвращает название страницы (текстом).
      """
      div = self._driver.find_element(By.CSS_SELECTOR, 
                                      ("div[class='constructor-promotions-page__container']"))
      h1 = div.find_element(By.CSS_SELECTOR, ("h1"))
      return h1.text
