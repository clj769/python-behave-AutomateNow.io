# from behave import *
#
# from features.environment import *
#
#
# @given('the images')
# def step_impl(context):
#     context.browser.get("https://practice-automation.com/broken-images/")
#
#
# @when('the site is loaded')
# def step_impl(context):
#     pass
#
#
# @then('the images should be properly displayed')
# def step_impl(context):
#     # Find all img elements on the page
#     images = context.browser.find_elements(By.XPATH, "//img")
#
#     # Print the number of img elements
#     print("Number of img elements:", len(images))
#
#     # Iterate through the img elements
#     for image in images:
#         # Locate the img elements again
#         updated_images = context.browser.find_elements(By.XPATH, "//img")
#
#         # Check if the element is still present in the updated list
#         if image in updated_images:
#             # Retrieve the src attribute of the img element
#             src = image.get_attribute("src")
#             try:
#                 # Check if the image is loading correctly
#                 response = requests.get(src)
#                 assert response.status_code == 200, f"Broken image: {response.url}"
#             except:
#                 # If the image is not loading correctly, print the exception message
#                 print("Broken image:", src)
#         else:
#             # If the element is not present in the updated list, skip it
#             continue
