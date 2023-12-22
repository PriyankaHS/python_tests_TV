from appium import webdriver
from appium.options.ios import XCUITestOptions

options = XCUITestOptions()
options.app = "absolute-path"
options.platform_name = "iOS"
options.platform_version = "version"
options.automation_name = "XCUITest"
options.udid = "uuid"
options.no_reset = True
options.device_name = "device-name"

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

try:
    driver.implicitly_wait(20)
finally:
    driver.quit()
