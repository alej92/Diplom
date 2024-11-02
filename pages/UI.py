from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


    # Тест №1. Проверка на главной странице номера телефона горячей линии
   def proverka_nomera(self):
      test = WebDriverWait(self._driver, 4, 0.1)
      test.until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 
                                        ("a[class='header-phone__number']")), '8 (495) 424-84-44')
      )
      result_test = self._driver.find_element(By.CSS_SELECTOR, 
                                              ("a[class='header-phone__number']")).text
      return result_test

    # Тест №2. Поиск книги
   def search(self, name):
      self._driver.find_element(By.CSS_SELECTOR, 
                                  "input[enterkeyhint='search']").clear()
      self._driver.find_element(By.CSS_SELECTOR, 
                                  "input[enterkeyhint='search']").send_keys(name)
      self._driver.find_element(By.CSS_SELECTOR, 
                                "button[class='header-search__button']").click()

    # проверка найденной книги
   def proverka_knigi(self):
      test = WebDriverWait(self._driver, 4, 0.1)
      test.until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 
                                        ("div[class='product-title__head']")),
                                        'Анжелика - маркиза ангелов')
      )
      result_test = self._driver.find_element(By.CSS_SELECTOR, 
                                              ("div[class='product-title__head']")).text
      return result_test 
    
    # Тест №3 проверка цвета кнопки "Каталог"
   def color_katalog(self):
      color = self._driver.find_element(By.CSS_SELECTOR, 
                                        "button[class='catalog__button']").value_of_css_property("background-color")
      return color
       

     # Тест №4. Иконка "Личный кабинет - Вход и регистрация"
   def knopka_kabinet(self):
      self._driver.find_element(By.CSS_SELECTOR, 
                                "svg[class='header-profile__icon header-profile__icon--desktop']").click()
    
   def proverka_kabinet(self):
      test = WebDriverWait(self._driver, 4, 0.1)
      test.until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, 
                                        ("h4[class='auth-modal__header']")), 'Вход и регистрация')
      )
      result_test = self._driver.find_element(By.CSS_SELECTOR, 
                                              ("h4[class='auth-modal__header']")).text
      return result_test
   
     # Тест №5. Проверка Распродажа
   def rasp(self):      
      self._driver.find_element(By.CSS_SELECTOR, "a[href='/promotions']").click()
      self._driver.find_element(
         By.CSS_SELECTOR, "div[class='popmechanic-close']").click()

   def proverka_rasp(self):
      div = self._driver.find_element(By.CSS_SELECTOR, 
                                      ("div[class='constructor-promotions-page__container']"))
      h1 = div.find_element(By.CSS_SELECTOR, ("h1"))
      return h1.text
