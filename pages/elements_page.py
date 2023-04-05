
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_are_visible(self.locators.FULL_NAME)[0].send_keys("Heisen")
        self.element_are_visible(self.locators.EMAIL)[0].send_keys("heisen@gmail.com")
        self.element_are_visible(self.locators.CURRENT_ADDRESS)[0].send_keys("Moscow")
        self.element_are_visible(self.locators.PERMANENT_ADDRESS)[0].send_keys("Moscow")
        self.element_are_visible(self.locators.SUBMIT)[0].click()

    def check_filled_form(self):

        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
