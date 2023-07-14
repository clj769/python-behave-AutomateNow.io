# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# url = "https://automatenow.io/"
#
# @given('AutomateNow home page')
# def step_given_automatenow_home_page(context):
#     context.browser.get(url)
#
# @when('open AutomateNow home page')
# def step_when_open_automatenow_home_page(context):
#     assert "automateNow" in context.browser.title
#
# @then('verify that the logo is present on the page')
# def step_then_verify_logo(context):
#     logo = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='header']/div/a/img"))) # Replace 'logo' with the actual logo's ID or CSS selector
#     assert logo is not None, "Logo not found"
#
# @then('close browser')
# def step_then_close_browser(context):
#     context.browser.quit()
