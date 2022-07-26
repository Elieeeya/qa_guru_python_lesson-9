from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser


class Dropdown:
    def __init__(self, element: Element):
        self.element = element

    def select(self, /, *, option: str):
        self.element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()

    def autocomplete(self, /, *, option: str):
        self.element.element(
            '[id^=react-select-][id*=-input]'
        ).type(option).press_enter()
