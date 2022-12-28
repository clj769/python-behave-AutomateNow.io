import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def before_all(context):
    print("Executing before all")



def before_feature(context, feature):
    print("Before feature\n")
    # Create logger
    context.logger = logging.getLogger('automation_test')
    context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    print("User data:", context.config.userdata)
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def after_scenario(context, scenario):
    print("scenario status" + str(scenario.status))
    context.browser.quit()


def after_feature(context, feature):
    print("\nAfter Feature")


def after_all(context):
    print("Executing after all")
