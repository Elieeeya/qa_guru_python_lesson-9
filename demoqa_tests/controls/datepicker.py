from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_year(self, option: int):
        self.element.click()
        browser.element('#dateOfBirth').element(f'[value="{option}"]').click()

    def select_month(self, option: str):
        month_list = {'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4,
                      'June': 5, 'July': 6, 'August': 7, 'September': 8, 'October': 9,
                      'November': 10, 'December': 11}
        browser.element('#dateOfBirth').element(f'[value="{month_list.get(option)}"]').click()

    def select_day(self, option: int):
        browser.element('#dateOfBirth').element(f'.react-datepicker__day--0{option}').click()

    def enter_date(self, option: str):
        self.element.perform(command.js.set_value(option)).click()