from lettuce import before, world, after
from appium import webdriver

@before.all
def open_shop():
    world.driver = setUp()

@after.all
def close_shop(total):
    print "Total %d of %d scenarios passed!" % (total.scenarios_passed, total.scenarios_ran)
    close_drivers()

def setUp():

    SAUCE_USERNAME = ''
    SAUCE_ACCESS_KEY = ''
    driver = webdriver.Remote(
        command_executor='http://'+SAUCE_USERNAME+':'+SAUCE_ACCESS_KEY+'@ondemand.saucelabs.com:80/wd/hub',
        desired_capabilities=
        # {
        #     # 'app': app,
        #     'deviceName': 'iPhone 6',
        #     'platformName': 'iOS',
        #     'platformVersion': '7.1',
        #     'browserName': 'Safari'
        # }
        {
            'platformName': 'Android',
            'platformVersion': '5.0',
            'deviceName': 'Android Emulator',
            'deviceType': 'tablet',
            'browserName': 'Browser'
        }
    )
    return driver

def close_drivers():
    if world.driver:
        world.driver.quit()
