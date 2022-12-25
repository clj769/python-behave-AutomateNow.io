import time

from behave import *
from features.environment import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# to run this program: behave features/Logo.feature

@given('AutomateNow home page')
@when('open AutomateNow home page')
def step_impl(context):
    context.browser.get("https://automatenow.io/")


@then('verify that the logo is present on the page')
def step_impl(context):
    status = context.browser.find_element(By.XPATH, "//*[@id='header']/div/a/img").is_displayed()
    assert status is True


@then('close browser')
def step_impl(context):
    pass
