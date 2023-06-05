import unittest
from main import WebDriver

driver = WebDriver()

class Tester(unittest.TestCase):
    def test_homepage_nav_link_Devlogs_navigates_to_devlogs(self):
        result = driver.header_nav_to_devlogs()
        self.assertEqual(result, "Devlogs component exists")

    def test_homepage_nav_link_Calendar_navigates_to_calendar_view(self):
        result = driver.header_nav_to_calendar_view()
        self.assertEqual(result, True)

    def test_homepage_nav_link_Register_navigates_to_register(self):
        result = driver.header_nav_to_register()
        self.assertEqual(result, True)

    def test_homepage_nav_link_Login_navigates_to_login(self):
        result = driver.header_nav_to_login()
        self.assertEqual(result, True)

    def test_homepage_nav_link_AddEvent_navigates_to_add_event(self):
        result = driver.header_nav_to_add_event()
        self.assertEqual(result, True)

    def test_homepage_nav_home_link_Home_navigates_to_homepage(self):
        result = driver.header_nav_to_home()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
