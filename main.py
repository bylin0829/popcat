from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    myWeb = webdriver.Chrome()
    myWeb.set_window_position(0, 0)
    myWeb.get('https://popcat.click/')
    try:
        content = WebDriverWait(myWeb, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div'))
        )
        catimg = myWeb.find_element(By.XPATH, '/html/body/div/div')
        while True:
            catimg.click()
    finally:
        myWeb.quit()
