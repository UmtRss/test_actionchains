from pages.interaction_page import InteractionPage

def test_hover_action(browser):
    page = InteractionPage(browser)
    caption = page.hover_over_image()
    assert "name: user1" in caption.lower()

def test_drag_and_drop(browser):
    page = InteractionPage(browser)
    result = page.drag_and_drop()
    assert "b" in result.lower()

def test_right_click_alert(browser):
    page = InteractionPage(browser)
    alert_text = page.right_click_and_alert()
    assert "you selected a context menu" in alert_text.lower()
