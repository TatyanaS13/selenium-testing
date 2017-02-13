import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_login

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_task8(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    rows = driver.find_elements_by_css_selector("tr.row")
    i = 0
    while i < len(rows):
        row = rows[i]
        country_name = row.find_element_by_css_selector("a").get_attribute("textContent")
        prev_country_name = rows[i-1].find_element_by_css_selector("a").get_attribute("textContent")
        assert country_name > prev_country_name

