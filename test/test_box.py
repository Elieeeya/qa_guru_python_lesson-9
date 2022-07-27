import pytest
from selene import have
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from demoqa_tests.utils import *
from demoqa_tests.controls.entering_tags import EnteringTags
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.datepicker import DatePicker
from demoqa_tests.controls.nameplate import Nameplate
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def test_student_registration_form():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    with allure.step('test_open_student_registration_form'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step('test_fill_student_form'):
        # First name, last name, mail
        browser.element('#firstName').type('TestName')
        browser.element('#lastName').type('TestSurname')
        browser.element('#userEmail').type('test_email@ya.ru')

        # Gender
        browser.element('[for="gender-radio-1"]').click()
        # Phone number
        browser.element('#userNumber').type('9208887755')

        # Form with date
        date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
        date_of_birth.select_year(1993)
        date_of_birth.select_month('September')
        date_of_birth.select_day(18)

        # Subjects
        subjects = EnteringTags(browser.element('#subjectsInput'))

        subjects.add('Economics')
        subjects.add('English')
        subjects.add('Arts')

        # Hobbies
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

        # Loading a picture
        browser.element('#uploadPicture').send_keys(get_abspath('l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg'))

        # Address
        browser.element('#currentAddress').type('Bolshaya Nikitskaya st., 22k2, Moscow, 121099')

        # State selection
        state = Dropdown(browser.element('#state'))
        state.select(option='Haryana')

        # City selection
        city = Dropdown(browser.element('#city'))
        city.autocomplete(option='Panipat')

        # Submit form button
        browser.element('#submit').press_enter()

    with allure.step('test_check_form_result'):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        res_nameplate = Nameplate()
        res_nameplate.way_to(tr=1, td=2).should(have.text('TestName TestSurname'))
        res_nameplate.way_to(tr=2, td=2).should(have.text('test_email@ya.ru'))
        res_nameplate.way_to(tr=3, td=2).should(have.text('Male'))
        res_nameplate.way_to(tr=4, td=2).should(have.text('9208887755'))
        res_nameplate.way_to(tr=5, td=2).should(have.text('18 September,1993'))
        res_nameplate.way_to(tr=6, td=2).should(have.text('Economics, English, Arts'))
        res_nameplate.way_to(tr=7, td=2).should(have.text('Sports, Music'))
        res_nameplate.way_to(tr=8, td=2).should(have.text('l8xMcQXMrRqEv1GdFVdPCD6a9zP.jpg'))
        res_nameplate.way_to(tr=9, td=2).should(have.text('Bolshaya Nikitskaya st., 22k2, Moscow, 121099'))
        res_nameplate.way_to(tr=10, td=2).should(have.text('Haryana Panipat'))

    demoqa_tests.utils.add_html(browser)
    demoqa_tests.utils.add_screenshot(browser)
    demoqa_tests.utils.add_logs(browser)
    demoqa_tests.utils.add_video(browser)
