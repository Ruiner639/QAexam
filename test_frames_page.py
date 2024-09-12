from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_frames_page_elements():
    service = Service("C:\\Users\\dimaf\\Desktop\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/frames")
    
    iframe_link = driver.find_element(By.LINK_TEXT, "iFrame")
    assert iframe_link.is_displayed()
    assert iframe_link.text == "iFrame"
    driver.save_screenshot('screenshot_page.png')
    print("Everything is complete.")
    driver.quit()

if __name__ == "__main__":
    test_frames_page_elements()
