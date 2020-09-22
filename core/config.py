from core.utils import Utils
from appium import webdriver
import time
import os
from core.session_handler import Session
from appium.webdriver.appium_service import AppiumService



class ConfigSetup:
    current_config = {}

    @staticmethod
    def start_appium_server():
        if not Utils.check_appium_is_already_running():
            appium_service = AppiumService()
            appium_service.start()
            time.sleep(4)
            print("Appium is started")
        else:
            print("Appium is already running")


    @staticmethod
    def stop_appium_server():
        if Utils.check_appium_is_already_running():
            appium_service = AppiumService()
            appium_service.stop()
            os.system('pkill adb')
            print("Appium is stop")
        else:
            print("Appium is already stop")

    def __init__(self):
        self.driver = None

    def launch_app(self):

        app_name = ConfigSetup.current_config['appName']
        platform_name = ConfigSetup.current_config['platformName']
        device_name = ConfigSetup.current_config['deviceName']
        launch_activity = ConfigSetup.current_config['launchActivity']

        print("Launching app with below config, for scenario : {}".format(ConfigSetup.current_config['scenario_name']))

        desired_capabilities = {
            "app": "{}/app/{}".format(os.getcwd(), app_name),
            "platformName": platform_name,
            "appWaitActivity": launch_activity,
            "deviceName": device_name,
            "automationName": "appium",
            "newCommandTimeout": 60,

        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
        Session.session_config_instance[self.driver] = ConfigSetup.current_config

    def get_driver(self):
        return self.driver
