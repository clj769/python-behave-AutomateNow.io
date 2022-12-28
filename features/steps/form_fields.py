from behave import *

from features.environment import *


@given('the form')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/form-fields/")


@when('I fill the form and click submit')
def step_impl(context):
    context.browser.find_element(By.ID, "cookie_action_close_header").click()
    context.browser.find_element(By.ID, "g1103-name").send_keys("Adam")
    context.browser.find_element(By.CSS_SELECTOR, "input[value='Coffee']").click()
    context.browser.find_element(By.XPATH, "//input[@value='Yellow']").click()

    dropdown = context.browser.find_element(By.ID, "g1103-doyouhaveanysiblings")
    select = Select(dropdown)
    select.select_by_value("No")
    # or select.select_by_visible_text("No")

    context.browser.find_element(By.ID, "email").send_keys('google@google.com')
    context.browser.find_element(By.ID, "contact-form-comment-message").send_keys('My test message')

    context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


@then('I should see message sent confirmation')
def step_impl(context):
    success = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "contact-form-success-header"))).get_attribute("innerHTML")

    assert success == "Your message has been sent", f"Expected: 'Your message has been sent' got '{success}' instead"
