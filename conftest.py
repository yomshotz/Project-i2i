from selenium.webdriver import Chrome
from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup(request):

    url = 'https://chain.unionbankph.com'
    path = 'D:\\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=800,600")

    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1,
    })

    driver = Chrome(executable_path=path, options=options)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    # time.sleep(10)
    driver.close()