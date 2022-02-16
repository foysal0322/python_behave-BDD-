from behave import *
from selenium import webdriver
import time


@given('launch chrome browser')
def open_browser(context):
    """
    this function will open chrome browser
    :param context:
    :return:
    """
    context.driver = webdriver.Chrome()



@when('open bikroy.com home page')
def open_url(context):
    """
    this function will browse the given url
    :param context:
    :return:
    """
    context.driver.get('https://bikroy.com/')


@then('veryfy that all category name are visible')
def category_is_visible(context):
    """
    this function will check the given category(element's) visibility
    :param context:
    :return:
    """
    status = context.driver.find_element_by_xpath('//*[@id="app-wrapper"]/div[2]/div[3]/div[3]/ul/li[1]/a/div[2]/p').is_displayed()  #catgegory name: Mobile
    assert status is True



@then('close the browser')
def tear_down(context):
    """
    this function will close the browser.

    """
    context.driver.close()
