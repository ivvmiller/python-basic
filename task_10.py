# 1. Открыть страницу http://google.com/ncr
# 2. Выполнить поиск слова “selenide”
# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
# 4. Перейти в раздел поиска изображений
# 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
# 6. Вернуться в раздел поиска Все
# 7. Проверить, что первый результат такой же, как и на шаге 3.


import unittest
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Search(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        s = Service('chromedriver.exe')
        self.drv = webdriver.Chrome(service=s)

    def test_search(self):
        # Открыть страницу http://google.com/ncr
        self.drv.get('http://google.com/ncr')

        # Выполнить поиск слова “selenide”
        elm = self.drv.find_element(By.NAME, 'q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)

        # Проверить, что первый результат – ссылка на сайт selenide.org.
        elm = self.drv.find_elements(By.CSS_SELECTOR, 'div.yuRUbf > a')
        result = elm[0].text
        assert 'selenide.org' in result, 'Первая ссылка должна быть на сайт selenide.org'

        # Перейти в раздел поиска изображений
        elm = self.drv.find_element(By.CSS_SELECTOR, '#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a')
        elm.click()

        # Проверить, что первое изображение неким образом связано с сайтом selenide.org.
        elm = self.drv.find_element(By.CSS_SELECTOR, '#islrg > div.islrc > div:nth-child(2)')
        assert 'selenide' in elm.text, 'Неправильная картинка'

        # Вернуться в раздел поиска Все
        self.drv.back()

        # Проверить, что первый результат такой же, как и на шаге 3.
        elm = self.drv.find_elements(By.CSS_SELECTOR, 'div.yuRUbf > a')
        assert result == elm[0].text, 'Результаты различаются'

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
