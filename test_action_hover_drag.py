import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert


@pytest.fixture

def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_hover_action(browser):
    browser.get("https://the-internet.herokuapp.com/hovers")
    image = browser.find_element(By.XPATH,"(//div[@class='figure'])[1]")
    hover = ActionChains(browser)
    hover.move_to_element(image).perform()
    caption = browser.find_element(By.XPATH,"(//div[@class='figcaption'])[1]/h5").text
    assert "name: user1" in caption.lower()

def test_drag_and_drop(browser):
    browser.get("https://the-internet.herokuapp.com/drag_and_drop")
    source = browser.find_element(By.ID, "column-a")
    target = browser.find_element(By.ID, "column-b")
    action = ActionChains(browser)
    action.drag_and_drop(source, target).perform()
    header = browser.find_element(By.ID,"column-a").text
    assert "B" in header

def test_right_click_alert(browser):
    browser.get("https://the-internet.herokuapp.com/context_menu")
    box = browser.find_element(By.ID,"hot-spot")
    action = ActionChains(browser)
    action.context_click(box).perform()
    alert = Alert(browser)
    assert "You selected a context menu" in alert.text
    alert.accept()
