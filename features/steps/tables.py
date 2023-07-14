import time

from behave import *
from features.environment import *


@given('the simple table')
def step_impl(context):
    context.browser.get("https://practice-automation.com/tables/")


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
    context.browser.get("https://practice-automation.com/tables/")

    search_input = context.browser.find_element(By.CSS_SELECTOR, "input[type='search']")


@when('I type {search_term}')
def step_impl(context, search_term):
    context.search_input.send_keys(search_term)

    time.sleep(2)


@then('the table should show only the row of interest')
def step_impl(context, search_term):
    # Find the table rows
    rows = context.browser.find_element(By.XPATH, "//*[@id='tablepress-1']/tbody/tr")
    # Check that only one row is displayed
    # assert len(rows) == 1
    # Check that the row text matches the search term
    row_text = rows[0].text
    assert search_term in row_text
