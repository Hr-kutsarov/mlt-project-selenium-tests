from selenium import webdriver
from selenium.webdriver.common.by import By


class WebDriver(webdriver.Chrome):
    HOST = "http://localhost:3000"

    def __init__(self):
        super(WebDriver, self).__init__()

    def header_nav_to_devlogs(self):
        self.get(self.HOST)
        # ^navigate to webpage

        btn = self.find_element(by=By.ID, value="homepage-nav-link-devlogs")
        # ^selects the element on the page that matches the id

        btn.click()
        # ^runs click function on the selected dom element, navigates to hostname/devlogs

        if self.find_element(by=By.ID, value="collection-devlog-wrapper"):
            return 'Devlogs component exists'
        # ^if the wrapper that contains the component exists returns a value that can be compared

    def header_nav_to_home(self):
        self.get(self.HOST)
        btn = self.find_element(by=By.ID, value="homepage-nav-link-home")
        btn.click()
        if self.find_element(by=By.CSS_SELECTOR, value="main") and self.find_element(by=By.CSS_SELECTOR, value="footer"):
            return True

    def header_nav_to_calendar_view(self):
        self.get(self.HOST)
        btn = self.find_element(by=By.ID, value="homepage-nav-link-calendar")
        btn.click()
        if self.find_element(by=By.ID, value="calendar-view-wrapper"):
            return True

    def header_nav_to_login(self):
        self.get(self.HOST)
        btn = self.find_element(by=By.ID, value="homepage-nav-link-login")
        btn.click()
        if self.find_element(by=By.ID, value="login-form-wrapper"):
            return True

    def header_nav_to_register(self):
        self.get(self.HOST)
        btn = self.find_element(by=By.ID, value="homepage-nav-link-register")
        btn.click()
        if self.find_element(by=By.ID, value="register-form-wrapper"):
            return True

    def header_nav_to_add_event(self):
        self.get(self.HOST)
        btn = self.find_element(by=By.ID, value="homepage-nav-link-add-event")
        btn.click()
        if self.find_element(by=By.ID, value="add-event-form-wrapper"):
            return True
