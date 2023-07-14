# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# url = "https://practice-automation.com/gestures/"
#
# @given('gestures examples')
# def step_given_gestures_examples(context):
#     context.browser.get(url)
#
# @when('I choose "{element}" element')
# def step_when_choose_element(context, element):
#     context.selected_element = context.browser.find_element(By.ID, element)
#     context.action_chain = ActionChains(context.browser)
#
# @then('I should manage "{element}" element accordingly')
# def step_then_manage_element(context, element):
#     if element == 'move_me_around':
#         # For instance, move the element by an offset
#         context.action_chain.drag_and_drop_by_offset(context.selected_element, 100, 100).perform()
#     elif element == 'drag_and_drop':
#         # For instance, simulate dragging and dropping the element to another location
#         target = context.browser.find_element(By.ID, ".//*[@id='dragMe']")  # Replace 'target' with the actual target's ID
#         context.action_chain.drag_and_drop(context.selected_element, target).perform()
