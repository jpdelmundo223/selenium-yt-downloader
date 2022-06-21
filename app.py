import time

from pytube import Playlist
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import constant

p = Playlist('https://www.youtube.com/playlist?list=PLUAg255I-02Z8gXty0IrtV1RggK-CUZG3')

urls = ['https://www.youtube.com/watch?v=Qfm6nfz1QNQ&list=PLDIoUOhQQPlXzhp-83rECoLaV6BwFtNC4&index=1', 'https://www.youtube.com/watch?v=HhQJrLbH6-4&list=PLDIoUOhQQPlXzhp-83rECoLaV6BwFtNC4&index=2']

for url in p.video_urls:
    browser = webdriver.Chrome(executable_path=constant.DRIVER_PATH)

    browser.implicitly_wait(30)
    browser.get('https://getn.topsandtees.space/s/eLW82xOGkW')
    searchElem = browser.find_element(By.NAME, "q")
    searchElem.send_keys(url, Keys.ENTER)

    time.sleep(3)
    downloadElem1 = browser.find_element(By.CSS_SELECTOR, "a[class='search-item__download item__download']")
    downloadElem1.click()

    try:
        downloadElem = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='search-item__download dl_progress_finished btn_clck_spec'"))
        ) 
        if downloadElem:
            downloadElem.click()
            time.sleep(10)
    finally:
        browser.close()