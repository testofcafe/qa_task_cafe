from behave import *
from core.appium_wrapper import AppiumWrapper
import time
use_step_matcher("re")


@when("I click on issue icon")
def click_on_issue_icon(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/issues')


@step("I click on float button")
def click_on_fab_btn(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/fab')


@step('I click on "Add" Option')
def click_on_add_option(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/add')


@step("I click on submit button")
def click_on_submit_btn(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/submit')


@step("I click edit icon")
def click_on_edit_btn(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/editMenu')
    AppiumWrapper().click('xpath', "//*[@text='Edit']")


@when("I update (?P<issue_title>.+) and (?P<issue_description>.+) in boxes")
def update_issue_title_and_description(context, issue_title, issue_description):
    AppiumWrapper().clear_text_box('class name', "android.widget.EditText")
    AppiumWrapper().insert_data('class name', "android.widget.EditText", issue_title)
    AppiumWrapper().click('id', "com.fastaccess.github:id/description")
    AppiumWrapper().insert_data('id', "com.fastaccess.github:id/editText", issue_description)
    AppiumWrapper().click('id', "com.fastaccess.github:id/submit")


@when("I enter issue title as (?P<issue_title>.+) and description as (?P<issue_description>.+) in boxes")
def add_new_issue(context, issue_title, issue_description):
    AppiumWrapper().insert_data('xpath', "//*[@text='Title']", issue_title)
    AppiumWrapper().click('xpath', "//*[@text='Description']")
    AppiumWrapper().insert_data('id', "com.fastaccess.github:id/editText", issue_description)
    AppiumWrapper().click('id', "com.fastaccess.github:id/submit")


@then("I should see new issue title (?P<issue_title>.+) in issue list")
def validation_issue_title(context, issue_title):
    time.sleep(5)
    assert AppiumWrapper().get_element_text('xpath', "//*[@text='" + issue_title + "']") == issue_title


@step("I click on issue title (?P<recent_issue_title>.+)")
def click_on_issue_title(context, recent_issue_title):
    AppiumWrapper().click('xpath', "//*[@text='" + recent_issue_title + "']")