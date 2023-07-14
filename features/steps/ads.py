from behave import *

from features.environment import *


@given('the ad')
def step_impl(context):
    context.browser.get("https://practice-automation.com/ads/")


@when('I will wait until it pops up')
def step_impl(context):
    WebDriverWait(context.browser, 20).until(EC.presence_of_element_located((By.ID, "popmake-1272")))


@then('I should be able to close it')
def step_impl(context):
    try:
        close = WebDriverWait(context.browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']")))
        close.click()
    except ElementNotInteractableException:
        print("Ad don't pops up")
    finally:
        print("Run feature test again")
