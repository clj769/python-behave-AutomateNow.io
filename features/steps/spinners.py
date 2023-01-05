from behave import *

from features.environment import *


@given('the spinner element')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/spinners/")


@when('I wait for the spinner to be present on the page')
def step_impl(context):
    # Wait for the spinner element to be present on the page
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.spinner")))


@then('the spinner should be displayed on the page')
def step_impl(context):
    # Find the spinner element
    spinner = context.browser.find_element(By.CSS_SELECTOR, "div.spinner")

    # Check if the spinner element is visible on the page
    assert spinner.is_displayed()
