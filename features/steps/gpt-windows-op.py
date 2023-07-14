from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given('window operations')
def given_window_operations(context):
    context.browser.get("https://practice-automation.com/window-operations/")


@when('I choose {operation}')
def when_choosing_operation(context, operation):
    button_mapping = {
        'new_tab': "New Tab",
        'replace_window': "Replace Window",
        'new_window': "New Window"
    }

    button_text = button_mapping.get(operation)
    button_element = context.browser.find_element(By.XPATH, f"//button/b[text()='{button_text}']")
    button_element.click()

    # Allow time for operation to take effect
    time.sleep(2)


@then('I should manage {operation} accordingly')
def then_manage_operation(context, operation):
    if operation == 'new_tab':
        context.browser.close()
        assert len(context.browser.window_handles) == 1, "New tab not closed properly"

    elif operation == 'replace_window':
        assert context.browser.current_url == "https://automatenow.io/", "Window not replaced correctly"

    elif operation == 'new_window':
        # Switch back to the main window
        context.browser.switch_to.window(context.browser.window_handles[0])
        time.sleep(2)
