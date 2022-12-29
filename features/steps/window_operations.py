import time

from behave import *

from features.environment import *


@given('window operations')
def step_impl(context):
    context.browser.get("https://automatenow.io/sandbox-automation-testing-practice-website/window-operations/")


@when('I choose {operation}')
def step_impl(context, operation):
    if operation == 'new_tab':
        new_tab = context.browser.find_element(By.XPATH, "//button/b[text()='New Tab']")
        new_tab.click()
    elif operation == 'replace_window':
        replace_window = context.browser.find_element(By.XPATH, "//button/b[text()='Replace Window']")
        replace_window.click()
    elif operation == 'new_window':
        new_window = context.browser.find_element(By.XPATH, "//button/b[text()='New Window']")
        new_window.click()

    time.sleep(2)


@then('I should manage {operation} accordingly')
def step_impl(context, operation):
    # original_window = context.browser.current_window_handle
    # assert len(context.browser.window_handles) == 1
    # title = context.browser.title
    # assert title == "Google"

    if operation == 'new_tab':
        # Get the number of open windows before closing the current window
        num_windows_before = len(context.browser.window_handles)
        # Close the current window
        context.browser.close()
        # Get the number of open windows after closing the current window
        num_windows_after = len(context.browser.window_handles)

        # Assert that the number of open windows has decreased by 1
        assert num_windows_after == num_windows_before - 1

    elif operation == 'replace_window':
        current_url = context.browser.current_url
        assert current_url == "https://www.google.com/", "Wrong URL address"


    elif operation == 'new_window':

        # Get the handles of all open windows
        handles = context.browser.window_handles

        # Remove the handle of the latest opened window from the list
        handles.remove(handles[-1])

        # Switch to the main window
        context.browser.switch_to.window(handles[0])

        time.sleep(2)
