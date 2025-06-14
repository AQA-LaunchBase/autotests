from playwright.sync_api import Page
from pages.Blog import Blog
import allure


@allure.feature('[Hero] Кликнуть на кнопку "Блог" на главной странице')
def test_blog(page: Page):
    blog = Blog(page)
    blog.open()
    blog.click_blog()
    blog.check_button_main()
    blog.check_click_main()