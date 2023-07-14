# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# url = "https://practice-automation.com/slider/"
#
# @given('the slider')
# def step_given_slider(context):
#     context.browser.get(url)
#
# @when('I adjust it by {using} drag-and-drop or clicking a given-area operation')
# def step_when_adjust_slider(context, using):
#     slider_element = context.browser.find_element(By.ID, 'slideMe')  # Replace 'slider' with the actual slider's ID
#     action_chain = ActionChains(context.browser)
#
#     if using == 'drag_and_drop':
#         # For instance, simulate dragging the slider to a new position
#         action_chain.click_and_hold(slider_element).move_by_offset(50, 0).release().perform()
#     elif using == 'given_area':
#         # For instance, simulate clicking a new position on the slider
#         action_chain.move_to_element(slider_element).move_by_offset(50, 0).click().perform()
#
# @then('the current value will be updated')
# def step_then_value_updated(context):
#     slider_value = context.browser.find_element(By.ID, 'value')  # Replace 'slider_value' with the actual value element's ID
#     assert slider_value.text != '', "Slider value did not update"
