from behave import *
from core.appium_wrapper import AppiumWrapper

use_step_matcher("re")


@given("I lunch application")
def close_change_log(context):
    """lunch application in environment - step before scenario run"""
    if AppiumWrapper().is_exist_element('id', 'com.fastaccess.github:id/title', time_out=2):
        AppiumWrapper().back_button()


@then("I should see login activity")
def validate_login_activity(context):
    assert AppiumWrapper().get_current_activity() == "com.fastaccess.ui.modules.login.chooser.LoginChooserActivity"


@when('I choose my login type "Basic Authentication"')
def choose_login_method(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/basicAuth')


@when("I enter username as (?P<Username>.+) and password as (?P<Password>.+)")
def fill_user_account_info(context, Username, Password):
    AppiumWrapper().insert_data('id', 'com.fastaccess.github:id/usernameEditText', Username)
    AppiumWrapper().insert_data('id', 'com.fastaccess.github:id/passwordEditText', Password)
    AppiumWrapper().hide_keyboard()


@step("I click on login button")
def click_on_login_btn(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/login')


@then('I should see main menu activity "FastHub"')
def validate_main_activity(context):
    assert AppiumWrapper().get_current_activity(sleep_time=5) == 'com.fastaccess.ui.modules.main.MainActivity'


@when("I click on side menu button")
def click_on_navigation_drawer(context):
    AppiumWrapper().click('xpath',
                          '//android.widget.ImageButton[@content-desc="‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‎‏‏‎‏‏‎‎‎‎‏‏‏‏‏‏‏‎‏‏‏‏‏‎‏‎‎‏‏‎‏‎‎‎‎‎‏‏‏‎‏‎‎‎‎‎‏‏‎‏‏‎‎‏‎‏‎‏‏‏‏‏‎‎Navigate up‎‏‎‎‏‎"]')


@step('I click on "Profile" tab')
def click_on_profile_tab(context):
    AppiumWrapper().click('xpath', '//androidx.appcompat.app.ActionBar.Tab[@content-desc="Profile"]')


@step('I click on "Logout" option')
def click_on_logout_option(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/logout')


@step('I click on "Yes" to confirm logout')
def confirm_logout(context):
    AppiumWrapper().click('id', 'com.fastaccess.github:id/ok')
    assert AppiumWrapper().get_current_activity(
        sleep_time=1) == "com.fastaccess.ui.modules.login.chooser.LoginChooserActivity"

#
# @when('I click on "OPEN IN BROWSER"')
# def step_impl(context):
#     AppiumWrapper().click('id', 'com.fastaccess.github:id/browserLogin')
#     AppiumWrapper().context_switch_to_web()
#
#
# @then('I should see browser title is "Sign in to Github"')
# def step_impl(context):
#     AppiumWrapper().get_element_text('id', 'com.android.chrome:id/title_bar')
#
#
# @step('I click on "Sign in" button')
# def step_impl(context):
#     AppiumWrapper().click('xpath',
#                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[1]/android.widget.Button')
#
#
# @then('I should back to native app and see main menu activity "FastHub"')
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     pass
#
#
# @when("I enter (?P<username>.+) and (?P<password>.+)")
# def step_impl(context, username, password):
#     AppiumWrapper().insert_data('xpath',
#                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
#                                 '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
#                                 '.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout['
#                                 '1]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View['
#                                 '1]/android.widget.EditText[1]', username)
#     AppiumWrapper().insert_data('xpath',
#                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
#                                 '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
#                                 '.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout['
#                                 '1]/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View['
#                                 '1]/android.widget.EditText[2]', password)
#     AppiumWrapper().hide_keyboard()
#     AppiumWrapper().context_switch_to_native()
