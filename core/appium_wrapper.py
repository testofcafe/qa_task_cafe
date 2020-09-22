from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from core.config import ConfigSetup as Config
import time
import logging


class AppiumWrapper:
    instance = None
    driver = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AppiumWrapper.instance is None:
            AppiumWrapper()

        return AppiumWrapper.instance

    def __init__(self):
        """ Virtually private constructor. """
        if AppiumWrapper.instance is not None:
            pass
        else:
            AppiumWrapper.instance = self
            config = Config()
            config.launch_app()
            AppiumWrapper.driver = config.get_driver()

    def get_current_activity(self, sleep_time=0):
        time.sleep(sleep_time)
        current__activity = AppiumWrapper.driver.current_activity
        logging.info(f"{__name__} : {current__activity}")
        return current__activity

    def start_activity(self, package_name, activity_name):
        logging.info(f'{__name__} : package name: {package_name} activity name: {activity_name}')
        AppiumWrapper.driver.start_activity(package_name, activity_name)

    def insert_data(self, by, located, value, time_out=10):
        element = self.click(by, located, time_out)
        element.send_keys(value)
        logging.info(f'{__name__} : inserted data By: {by} located: {located} value: {value}')
        return element

    def is_exist_element(self, by, element, time_out=10):
        try:
            self.__wait_for_located(by, element, time_out)
            return True
        except Exception as e:
            print(e)
            return False

    def click(self, by, element, time_out=10):
        self.__wait_for_element_clickable(by, element, time_out)
        element = self.__wait_for_located(by, element, time_out)
        element.click()
        logging.info(f'{__name__} : clicked data By: {by} located: {element} ')
        return element

    def get_element_text(self, by, located, time_out=10):
        element = self.__wait_for_located(by, located, time_out)
        return element.text

    def context_switch_to_web(self):
        time.sleep(10)
        webview = AppiumWrapper.driver.contexts[1]
        AppiumWrapper.driver.switch_to.context(webview)

    def context_switch_to_native(self):
        time.sleep(10)
        webview = AppiumWrapper.driver.contexts[0]
        AppiumWrapper.driver.switch_to.context(webview)

    def __wait_for_located(self, by, element, time_out=10):
        logging.debug(f'{__name__} : wait By: {by} located: {element} ')
        return WebDriverWait(AppiumWrapper.driver, time_out).until(
            ec.presence_of_element_located((by, element)))

    def __wait_for_element_clickable(self, by, element, time_out=10):
        logging.debug(f'{__name__} : wait By: {by} located: {element} ')
        WebDriverWait(AppiumWrapper.driver, time_out).until(
            ec.element_to_be_clickable((by, element)))

    def hide_keyboard(self):
        return AppiumWrapper.driver.hide_keyboard()

    def back_button(self):
        return AppiumWrapper.driver.back()

    def clear_text_box(self, by, element, time_out=10):
        self.__wait_for_element_clickable(by, element, time_out)
        element = self.__wait_for_located(by, element, time_out)
        element.clear()

    def wait_for_activity(self, activity, time_out, interval=1):
        try:
            WebDriverWait(self, time_out, interval).until(
                lambda d: self.driver.current_activity == activity)
            return True
        except Exception as e:
            print("can't find activity", e)
            return False

    def find_element(self, by, element, time_out=10):
        self.__wait_for_element_clickable(by, element, time_out)
        return self.__wait_for_located(by, element, time_out)

    def is_visible_element(self, by, element, time_out=10):
        try:
            self.__wait_for_element_clickable(by, element, time_out)
            if self.__wait_for_located(by, element, time_out):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
