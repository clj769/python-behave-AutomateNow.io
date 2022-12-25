import time

from behave import *
from features.environment import *


@given('the simple table')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/tables/")


@when('I extract data from the table')
def step_impl(context):
    simple_table = context.browser.find_element(By.TAG_NAME, "tbody")
    print(simple_table.text)


@then('the values will be available for analysis')
def step_impl(context):
    print("Values from the table are printed to terminal.")
    pass


@given('the search input field')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/tables/")


@when('I type rank, country or population')
def step_impl(context):
    search = context.browser.find_element(By.CSS_SELECTOR, "input[type='search']")
    search.send_keys('Italy')


@then('the table should show only the row of interest')
def step_impl(context):
    table = context.browser.find_element(By.CLASS_NAME, "row-hover")
    rows = table.find_element(By.TAG_NAME, "tr")
    value = rows.find_elements(By.TAG_NAME, "td")

    time.sleep(3)
    print(value.text)
    assert value.text == "Italy", "No match found"

    time.sleep(3)
