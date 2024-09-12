from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_frames():
    service = Service("C:\\Users\\dimaf\\Desktop\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    wait = WebDriverWait(driver, 10)

    driver.switch_to.frame("frame-top")
    driver.switch_to.frame("frame-left")
    left_frame_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text
    assert left_frame_text == "LEFT", f"Expected 'LEFT' but '{left_frame_text}'"
    
    driver.switch_to.parent_frame()
    
    driver.switch_to.frame("frame-middle")
    middle_frame_text = wait.until(EC.presence_of_element_located((By.ID, "content"))).text
    assert middle_frame_text == "MIDDLE", f"Expected 'MIDDLE' but '{middle_frame_text}'"
    
    driver.switch_to.parent_frame()
    
    driver.switch_to.frame("frame-right")
    right_frame_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text
    assert right_frame_text == "RIGHT", f"Expected 'RIGHT' but '{right_frame_text}'"

    driver.switch_to.default_content()
    
    driver.switch_to.frame("frame-bottom")
    bottom_frame_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text
    assert bottom_frame_text == "BOTTOM", f"Expected 'BOTTOM' but '{bottom_frame_text}'"

    driver.save_screenshot('screenshot_frame.png')
    driver.quit()

if __name__ == "__main__":
    test_frames()
