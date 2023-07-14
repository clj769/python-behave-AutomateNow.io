from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://practice-automation.com/click-events/"

@given('buttons of the animals')
def step_given_buttons_of_animals(context):
    context.browser.get(url)

@when('I click "{button}"')
def step_when_click_button(context, button):
    button_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//button[normalize-space()="{button}"]')))
    button_element.click()
    context.selected_button = button

@then('the "{sound}" of that animal should appear on the screen')
def step_then_sound_appears(context, sound):
    time.sleep(1)  # Pause to allow the button's action to take effect

    message_element = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'demo')))
    actual_sound = message_element.get_attribute('innerHTML')

    assert actual_sound == sound, f'For button "{context.selected_button}", expected sound "{sound}", got "{actual_sound}"'
