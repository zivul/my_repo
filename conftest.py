import logging
from telnetlib import EC
from time import sleep
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from playwright.sync_api import Playwright
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

logging.basicConfig(
    level=logging.DEBUG,
    filename="my_log.log",
    format="%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]",
    datefmt="%d/%m/%Y %I:%M:%S",
    encoding="utf-8",
    filemode="w",
)

logger = logging.getLogger(__name__)
handler = logging.FileHandler("test.log", encoding="utf-8")
formatter = logging.Formatter(
    "%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Логи сайта Pizzeria")


@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(60)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def browser(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.set_viewport_size({"height": 1080, "width": 1920})
    yield page
    page.close()
    browser.close()
