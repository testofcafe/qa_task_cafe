from behave import *
from core.appium_wrapper import AppiumWrapper
import time
use_step_matcher("re")


@when("I click on search icon")
def click_on_search_icon(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/search')


@step("I enter (?P<repository_name>.+) in to edit text")
def enter_repo_name(context, repository_name):
    AppiumWrapper().insert_data('id', 'com.fastaccess.github:id/searchEditText', repository_name)
    AppiumWrapper().click('id', 'com.fastaccess.github:id/search')


@then("I should see repo name (?P<repository_name>.+) in results of search")
def validation_search(context, repository_name):
    time.sleep(5)
    assert AppiumWrapper().get_element_text('id', 'com.fastaccess.github:id/title') == repository_name


@when("I click (?P<repository_name>.+) from search result")
def click_on_result(context, repository_name):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/title')


@then("I should see (?P<repository_name>.+) page")
def validation_repo_page(context, repository_name):
    time.sleep(5)
    assert AppiumWrapper().get_element_text('id', 'com.fastaccess.github:id/headerTitle') == repository_name
