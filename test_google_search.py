import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_search_request_has_result(driver):
    driver.get("https://www.google.com/?hl=en")
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search.send_keys("wildberries" + Keys.ENTER)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    links = driver.find_elements(By.CSS_SELECTOR, '#search a[href*="wildberries.ru"]')
    assert links


def test_search_gibberish_shows_no_result(driver):
    driver.get("https://www.google.com/?hl=en")
    gibberish = str(uuid.uuid4())
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search.send_keys(gibberish + Keys.ENTER)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "did not match any documents" in body_text

