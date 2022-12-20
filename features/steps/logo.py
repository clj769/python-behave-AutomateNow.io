import time

from behave import *
from features.environment import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# to run this program: behave features/logo.feature

@given('AutomateNow home page')
@when('open AutomateNow home page')
def open_homepage(context):
    context.browser.get("https://automatenow.io/")


@then('verify that the logo is present on the page')
def verify_logo(context):
    status = context.browser.find_element(By.XPATH, "//*[@id='header']/div/a/img").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    pass
