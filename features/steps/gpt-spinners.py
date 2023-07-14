# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# url = "https://practice-automation.com/spinners/"
#
# @given('the spinner element')
# def step_given_spinner_element(context):
#     context.browser.get(url)
#
# @when('I wait for the spinner to be present on the page')
# def step_when_wait_spinner(context):
#     WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.spinner")))  # Replace 'spinner' with the actual spinner's ID
#
# @then('the spinner should be displayed on the page')
# def step_then_spinner_displayed(context):
#     spinner = context.browser.find_element(By.CSS_SELECTOR, "div.spinner")  # Replace 'spinner' with the actual spinner's ID
#     assert spinner.is_displayed(), "Spinner is not displayed on the page"
