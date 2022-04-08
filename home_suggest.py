from PageObject.locators import Locator
from PageObject.Page.driver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep


class HomeSuggest(WebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.suggest = driver.find_element(By.CSS_SELECTOR, Locator.suggest)

    def check_suggest(self):#Проверка появления suggest
        sleep(1.5)
        assert self.suggest, "Таблица с подсказками(suggest) не найдена."
        print('Таблица с подсказками найдена.\n')
