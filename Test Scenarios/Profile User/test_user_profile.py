import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('http://localhost:8080/')

try:
    email_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, 'btnSub')

    email_input.send_keys('manager@example.com')
    password_input.send_keys('managerpassword')
    login_button.click()

    time.sleep(2)

    driver.implicitly_wait(10)

    pagetitle_element = driver.find_element(By.ID, 'pagetitle')
    text = pagetitle_element.text

    assert "Welcome to Hotel Management Page" in text

    print("Teste de login como administrador bem-sucedido!")

except Exception as e:
    print("Teste de login como administrador falhou:", str(e))

try:
    driver.get('http://localhost:8080/')

    email_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, 'btnSub')

    email_input.send_keys('user1@example.com')
    password_input.send_keys('password1')
    login_button.click()

    time.sleep(2)
    
    driver.implicitly_wait(10)

    pagetitle_element = driver.find_element(By.ID, 'pagetitle')
    text = pagetitle_element.text

    assert "Welcome to Pet's Hotel," in text

    print("Teste de login como cliente bem-sucedido!")

except Exception as e:
    print("Teste de login como cliente falhou:", str(e))

finally:
    driver.quit()
