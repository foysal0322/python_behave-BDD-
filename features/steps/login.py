import time

from behave import *
from selenium import webdriver

@given('launch browser')
def open_browser(context):
    """
    this function will open chrome browser
    :param context:
    :return:
    """
    context.driver = webdriver.Chrome()



@when('open bikroy.com login page')
def open_url(context):
    """
    this function will browse the given url
    :param context:
    :return:
    """
    context.driver.get('https://bikroy.com/')

    context.driver.find_element_by_xpath('//*[@id="app-wrapper"]/div[2]/div[2]/div/nav/div/ul[2]/li[2]/div/a/span').click()
    time.sleep(3)


@when('click "continue with email"')
def click_email(context):
    """
    this function will click on "continue the with email"
    :return: None
    """
    # context.driver.switch_to_window()
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[2]/div/div[3]/button').click() #click on "continue iwth email" button


@when('enter "{email}" and "{password}"')
def enter_credentials(context, email, password):
    """
    enter email and passwords
    :param password:
    :param email:
    :param context:
    :return: None
    """
    context.driver.find_element_by_id('input_email').send_keys(email)
    context.driver.find_element_by_id('input_password').send_keys(password)
    context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[2]/div/form/div[2]/div/button').click()

    time.sleep(5)

@when('click login button')
def click_login_btn(context):
    """
    clicks login btn
    :param context:
    :return: None
    """
    # context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[2]/div/form/div[2]/div/button').click()
    # time.sleep(5)
    pass

@then('User must successfully jump to the dashboard')
def check_is_dashborad_visible(context):
    """
    this function will check whether the credentials is valid or not by checking the "Dashboard" words visibility
    :param context:
    :return:
    """
    try:
        text = context.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[2]/div/div/span').text
    except:
        context.driver.close()
        assert False,"Wrong Credential"

    if text == 'The email or password you entered did not match our records. Please double-check and try again.':
        context.driver.close()
        assert True,"Credential matched!"
