import allure
from playwright.sync_api import expect
from pages.Base_page import BasePage


class Blog(BasePage):
    @allure.step('Нажать на кнопку Блог')
    def click_blog(self):
        (self.page.get_by_role('link', name = 'Блог', exact = True).click())

    @allure.step('Проверить отображение кнопки "На главную"')
    def check_button_main(self):
        expect(self.page.get_by_text('На главную')).to_be_enabled()

    @allure.step('Нажать кнопку "На главную"')
    def check_click_main(self):
        (self.page.get_by_text('На главную')).click()
        expect(self.page).to_have_url('https://launch-base.online/')