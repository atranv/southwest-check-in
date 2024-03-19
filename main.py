import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()
    driver.get('https://mobile.southwest.com/check-in')

    try:
        time.sleep(5)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'recordLocator'))
        )
        confirmation_num = driver.find_element(By.NAME, 'recordLocator')
        first_name = driver.find_element(By.NAME, 'firstName')
        last_name = driver.find_element(By.NAME, 'lastName')
    finally:
        driver.quit()

    confirmation_num.send_keys('TestNum')
    first_name.send_keys('Robert')
    last_name.send_keys('Robertson')

    retrieve = driver.find_element(By.NAME, 'button button--fluid large button--yellow')
    retrieve.click()

if __name__ == '__main__':
    main()

    #testing commits