import requests
from behave import given, when, then
from selenium.webdriver.common.by import By

@given('the images')
def step_given_the_images(context):
    context.url = "https://practice-automation.com/broken-images/"
    context.images = context.browser.find_elements(By.TAG_NAME, "img")


@when('the site is loaded')
def step_when_site_is_loaded(context):
    # Assuming the site url is stored in context.url
    context.browser.get(context.url)

@then('the images should be properly displayed')
def step_then_images_properly_displayed(context):
    broken_images = []
    for image in context.images:
        result = requests.head(image.get_attribute('src'))
        if result.status_code != 200:
            broken_images.append(image.get_attribute('src'))
    assert not broken_images, f"Broken images: {broken_images}"
