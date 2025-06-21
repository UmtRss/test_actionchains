from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

class InteractionPage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def hover_over_image(self):
        self.driver.get("https://the-internet.herokuapp.com/hovers")
        image = self.driver.find_element(By.XPATH, "(//div[@class='figure'])[1]")
        self.action.move_to_element(image).perform()
        caption = self.driver.find_element(By.XPATH, "(//div[@class='figcaption'])[1]/h5").text
        return caption

    def drag_and_drop(self):
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        source = self.driver.find_element(By.ID, "column-a")
        target = self.driver.find_element(By.ID, "column-b")
        self.action.drag_and_drop(source, target).perform()
        return self.driver.find_element(By.ID, "column-a").text

    def right_click_and_alert(self):
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        box = self.driver.find_element(By.ID, "hot-spot")
        self.action.context_click(box).perform()
        alert = Alert(self.driver)
        text = alert.text
        alert.accept()
        return text
