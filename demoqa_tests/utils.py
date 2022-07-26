import allure
import demoqa_tests
import os

from allure_commons.types import AttachmentType
from pathlib import Path


# Abs Путь к файлу
def get_abspath(path):
    file_path = str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'resources/{path}'))
    return os.path.abspath(file_path)


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_videos(browser):
    video_url = 'https://selenoid.autotests.cloud/#/videos' + browser.driver.session_id + '.mp4'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video' + browser.driver.session_id, AttachmentType.HTML, '.html')
