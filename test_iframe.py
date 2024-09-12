from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_page_elements():
    service = Service("C:\\Users\\dimaf\\Desktop\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/iframe")
    
    header = driver.find_element(By.TAG_NAME, "h3")
    assert header.is_displayed(), "Header is not displayed"
    assert header.text == "iFrame containing the TinyMCE Editor", "Header text is incorrect"
    
    driver.save_screenshot('screenshot_iframe.png')
    driver.quit()

if __name__ == "__main__":
    test_page_elements()
