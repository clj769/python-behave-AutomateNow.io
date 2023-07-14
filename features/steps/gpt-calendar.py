# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
#
# calendar_url = "https://practice-automation.com/calendars/"
# selected_date = "January 15, 2023"
#
# @given('the calendar')
# def step_given_the_calendar(context):
#     context.browser.get(calendar_url)
#
# @when('I select the date')
# def step_when_select_date(context):
#     date_field = context.browser.find_element(By.ID, "g1065-selectorenteradate")
#     date_field.send_keys(selected_date)
#     date_field.send_keys(Keys.RETURN)
#
#     submit_button = context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     submit_button.click()
#
# @then('I should be able to see selected date on the next page')
# def step_then_see_selected_date(context):
#     actual_date = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "field-value"))).get_attribute("innerHTML")
#
#     assert actual_date == selected_date, f"Expected '{selected_date}', got '{actual_date}' instead"
