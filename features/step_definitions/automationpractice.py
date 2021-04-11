from pytest_bdd import scenarios, given, then, parsers, when
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

scenarios('')

@given(parsers.parse('I am opening page "{URL}"'))
def open_page_url(driver_init, URL):
        with allure.step(f'I am opening page {URL}'):
            driver_init.get(f'{URL}')


@when(parsers.parse('I am clicking on "{LOCATOR}"'))
def click(driver_init, LOCATOR):
    with allure.step(f'I am clicking on {LOCATOR}'):
        driver_init.click(LOCATOR)


@then(parsers.parse('I am verifying title with "{PATTERN}"'))
def click(driver_init, PATTERN):
    with allure.step(f'I am verifying title with {PATTERN}'):
        driver_init.verify_title(PATTERN)

