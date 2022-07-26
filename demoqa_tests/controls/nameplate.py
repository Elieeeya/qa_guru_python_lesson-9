from selene.support.shared import browser


class Nameplate:
    @staticmethod
    def way_to(tr: int, td: int):
        return browser.element(f'//*[@class="table-responsive"]//tr[{tr}]//td[{td}]')