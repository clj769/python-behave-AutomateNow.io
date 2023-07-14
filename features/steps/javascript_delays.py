# from behave import *
# from features.environment import *
#
#
# @given('countdown timer with a start button')
# def step_impl(context):
#     context.browser.get("https://practice-automation.com/javascript-delays/")
#
# @given('picture of a rocket ship')
# def step_impl(context):
#     img = context.browser.find_element(By.XPATH, "//*[@data-image-title='rocket']")
#     assert img.is_displayed(), "There is no image or attribute name is no longer valid"
#
#
# @when('START button is clicked')
# def step_impl(context):
#     context.browser.find_element(By.ID, "start").click()
#
#
# @then('after 10 seconds "Liftoff!" appears in the text field')
# def step_impl(context):
#     context.browser.find_element(By.ID, "delay")
#     # waits for the timer
#     time.sleep(11)
#     # gets value from JavaScript delay function with querySelector for id (#) 'delay'
#     msg = context.browser.execute_script("return document.querySelector('#delay').value")
#
#     print(msg)
#     assert msg == "Liftoff!", "Text inside the input field is not 'Liftoff!'"
