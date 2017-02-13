import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


# is_element_present(driver, By.name, "q")

def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


# задание 7 - сценарий, проходящий по всем разделам админки
def test_login(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    i = 0
    menu_items = driver.find_elements_by_css_selector("li#app-")
    while i < len(menu_items):

        element = menu_items[i]
        element.click()
        assert is_element_present(driver, By.TAG_NAME, "h1")

        if is_element_present(driver, By.CSS_SELECTOR, "li#app-[class='selected'] ul"):

            submenu_items = driver.find_elements_by_css_selector("li#app-[class='selected'] ul li")
            for j in range(0,len(submenu_items)):

                submenu_items[j].click()
                assert is_element_present(driver, By.TAG_NAME, "h1")
                submenu_items = driver.find_elements_by_css_selector("li#app-[class='selected'] ul li")


        i += 1
        menu_items = driver.find_elements_by_css_selector("li#app-")


