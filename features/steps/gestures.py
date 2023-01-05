from behave import *

from features.environment import *


@given('gestures examples')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/gestures/")


@when('I choose {element} element')
def step_impl(context, element):
    actions = ActionChains(context.browser)
    context.browser.find_element(By.ID, "cookie_action_close_header").click()
    time.sleep(1)

    if element == 'move_me_around':
        context.box = context.browser.find_element(By.ID, "moveMeHeader")
        context.original_location = context.box.location
        actions.drag_and_drop_by_offset(context.box, 200, 30).perform()
    elif element == 'drag_and_drop':
        logo = context.browser.find_element(By.XPATH, "//*[@id='dragMe']")
        context.drop_target = context.browser.find_element(By.XPATH, "//*[@id='div2']")
        context.browser.execute_script("return arguments[0].scrollIntoView();", context.drop_target)
        actions.drag_and_drop(logo, context.drop_target).perform()

    elif element == 'drag_the_map':
        the_map = context.browser.find_element(By.CSS_SELECTOR, ".wp-block-jetpack-map-marker")
        context.browser.execute_script("return arguments[0].scrollIntoView();", the_map)

        context.original_position = the_map.get_attribute("style")
        actions.drag_and_drop_by_offset(the_map, 200, 400).perform()
        time.sleep(2)
        # context.new_position = style.split(" ")[1]
        context.new_position = the_map.get_attribute("style")


@then('I should manage {element} element accordingly')
def step_impl(context, element):
    if element == 'move_me_around':
        new_location = context.box.location

        assert (context.original_location["x"] != new_location["x"]) or (
                context.original_location["y"] != new_location["y"]), "Element has not moved"

    elif element == 'drag_and_drop':
        try:
            # try to look for 'dragMe' logo inside id="div2"
            context.drop_target.find_element(By.ID, ".//*[@id='dragMe']")
        except NoSuchElementException:
            print("The logo element is not contained inside the drop target element.")
    elif element == 'drag_the_map':
        assert context.original_position != context.new_position, "The map was not moved."
