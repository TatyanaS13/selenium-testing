import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_login as t

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


# задание 8 - сценарий, проверяющий наличие стикеров у товаров
def test_task8(driver):
    driver.get("http://localhost/litecart")

    items = driver.find_elements_by_css_selector("li.product")

    for item in items:
        stickers = item.find_elements_by_css_selector("div.sticker");
        assert len(stickers) == 1