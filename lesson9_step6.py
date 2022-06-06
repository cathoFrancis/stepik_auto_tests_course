from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    current_window = browser.window_handles[0]
    time.sleep(3) 
    btn = browser.find_element(By.TAG_NAME, "button").click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(browser.window_handles[1])

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    time.sleep(2)
    input.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    time.sleep(1)
    button.click()
    time.sleep(3)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[0])
    
finally:
    # задержка перед закрытием
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла