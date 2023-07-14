import time

from behave import *
from features.environment import *


@given('the slider')
def step_impl(context):
    context.browser.get("https://practice-automation.com/slider/")


@when('I adjust it by {using} drag-and-drop or clicking a given-area operation')
def step_impl(context, using):
    slider = context.browser.find_element(By.ID, "slideMe")

    if using == 'drag_and_drop':
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(slider, -10, 0).perform()

    elif using == 'given_area':
        actions = ActionChains(context.browser)
        actions.move_to_element(slider).move_by_offset(35, 0).click().perform()

    # remember that final value depends on the size of the window your Selenium instance stars off
    # in my case, offset by 10 results in current value of 51


@then('the current value will be updated')
def step_impl(context):
    current_value = context.browser.find_element(By.ID, "value").get_attribute('innerHTML')

    assert current_value != "25"  # if it is 25 then the slider did not move
