import time

from behave import *
from features.environment import *


@given('the simple table')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/tables/")


@when('I extract data from the table')
def step_impl(context):
    simple_table = context.browser.find_element(By.TAG_NAME, "table")

    for row in simple_table.find_elements(By.TAG_NAME, 'tr'):
        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            print(cell.text)

@then('the values will be available for analysis')
def step_impl(context):
    pass