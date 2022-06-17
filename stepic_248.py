import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100")
    )
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    # находим переменную "x" на странице сайта
    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_el.text
    # создаем функцию для нахождения значения "х"

    def calc(n):
        """ Вычисляет значение выражения переменной 'х' """
        return str(math.log(abs(12 * math.sin(int(n)))))


    # вычисляем значение функции
    y = calc(x)
    # находим поле для ответа, и вставляем полученное значение функции
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    # находим кнопку отправить submit
    button = browser.find_element(By.CSS_SELECTOR, "button[type]")
    button.click()
    time.sleep(15)
finally:
    time.sleep(2)
    browser.quit()