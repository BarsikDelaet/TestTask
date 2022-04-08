from PageObject.locators import Locator
from PageObject.Page.driver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Home(WebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_line = driver.find_element(By.CSS_SELECTOR, Locator.search_line)
        self.link_img = driver.find_element(By.CSS_SELECTOR, Locator.img_button)

    def input_text(self, text: str):#Вводим в строку поиска text
        assert self.search_line, "Поисковая строка не найдена."
        print('Поисковая строка найдена.\n')
        self.search_line.send_keys(text)

    def search_text(self):#Нажимаем Enter в поисковой строке
        self.search_line.send_keys(Keys.ENTER)

    def open_img(self):#Открываем Яндекс Картинки
        link_img = self.link_img
        assert link_img, 'Ссылка на "Картирки", не найдена.'
        print('Ссылка на "Картинки" найдена.\n')
        link_img.click()
