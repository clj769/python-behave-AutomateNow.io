import time

from behave import *
from features.environment import *


@given('buttons of the animals')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/click-events/")


@when('I click "{button}"')
def step_impl(context, button):
    context.find_button = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//button[normalize-space()="{button}"]')))

    context.find_button.click()


@then('the "{sound}" of that animal should appear on the screen')
def step_impl(context, sound):
    time.sleep(1)  # so we could see buttons being clicked

    message_element = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'demo')))
    context.message = message_element.get_attribute('innerHTML')

    if context.find_button == 'Cat':
        assert context.message == sound, f'Expected "Meow!", got {context.message}'
    elif context.find_button == 'Pig':
        assert context.message == sound, f'Expected "Oink!", got {context.message}'
    elif context.find_button == 'Dog':
        assert context.message == sound, f'Expected "Woof!", got {context.message}'
    elif context.find_button == 'Cow':
        assert context.message == sound, f'Expected "Moo!", got {context.message}'
