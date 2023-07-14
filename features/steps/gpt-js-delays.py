from behave import given, when, then
from selenium.webdriver.common.by import By
import time

url = "https://practice-automation.com/javascript-delays/"

@given('countdown timer with a start button')
def step_given_countdown_timer(context):
    context.browser.get(url)

@given('picture of a rocket ship')
def step_given_rocket_ship_picture(context):
    context.picture = context.browser.find_element(By.XPATH, "//*[@data-image-title='rocket']")  # Replace 'rocket' with the actual picture's ID
    assert context.picture is not None, "Picture of a rocket ship not found"

@when('START button is clicked')
def step_when_start_button_clicked(context):
    start_button = context.browser.find_element(By.ID, 'start')  # Replace 'start' with the actual start button's ID
    start_button.click()

@then('after 10 seconds "Liftoff!" appears in the text field')
def step_then_liftoff_appears(context):
    countdown_timer_field = context.browser.find_element(By.ID, "delay")
    # Pause the script to allow the countdown timer to finish
    time.sleep(11)
    # Retrieve the value from the JavaScript delay function using JavaScript Execution
    countdown_value = context.browser.execute_script("return arguments[0].value", countdown_timer_field)
    # Assert that the countdown value is as expected
    assert countdown_value == "Liftoff!", f"Expected 'Liftoff!', but got '{countdown_value}'"
