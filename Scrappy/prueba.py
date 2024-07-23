from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium_stealth import stealth

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import json
import random
import time
from fake_useragent import UserAgent

url = "https://www.betano.pe/casino/games/aviator/3337/"
chrome_bin="/home/dhackos/chrome/chrome-linux64/chrome"
chrome_bin="/usr/bin/google-chrome-stable"

ua = UserAgent()
user_agent = ua.random

proxy = '187.102.219.137:999'

# Login
user = "user_sebas123@proton.me"
password = "1VX8wAWeFqQ21PwZcXxY#"

########### BYPASS DETECTION BOTS ##############

options = ChromeOptions()

options.add_argument("--log-level=3")
options.add_argument( '--no-sandbox' )
options.add_argument( '--disable-dev-shm-usage' )

# Disable loading images for faster crawling
options.add_argument('--blink-settings=imagesEnabled=false')

options.add_argument("start-maximized")
#options.add_argument("--headless=False")

options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--use_subprocess")

options.add_argument("--disable-extensions")
options.add_argument("-–disable-gpu")
#options.add_argument("-–incognito")
#options.add_argument("-–disable-infobars")

options.add_argument("--use_subprocess")

#options.add_argument(f'--user-agent={user_agent}')
options.binary_location = chrome_bin
#options.add_argument('--proxy-server=socks5://' + proxy)



def authentication(driver):
    try:
        url_login = "https://www.betano.pe/casino/myaccount/login"
        driver.get(url_login)
        
        time.sleep(3)
        
        wait = WebDriverWait(driver, 5)

        username_field = wait.until(EC.presence_of_element_located((By.NAME, "Username")))
        
        if username_field:
            print("Campo de usuario encontrado correctamente")
            username_field.send_keys(user)
        else:
            raise Exception("Campo de usuario no encontrado")

        #wait.until(EC.((By.NAME, "Username"))).send_keys(user)
        wait.until(EC.element_to_be_clickable((By.Name, "Password"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/main[1]/div[1]/section[1]/div[1]/form[1]/button[1]"))).click()
        print("Logged in")
    except TimeoutException as timeout_ex:
        print(f"Tiempo de espera excedido durante el login: {str(timeout_ex)}")
    except NoSuchElementException as no_element_ex:
        print(f"Elemento no encontrado durante el login: {str(no_element_ex)}")
    except Exception as e:
        print(f"Error durante el login: {str(e)}")
    finally:
        time.sleep(3)
        driver.quit()    

def human_delay(min_delay=0.5, max_delay=2.0):
    print(random.uniform(min_delay, max_delay))
    time.sleep(random.uniform(min_delay, max_delay))

def bypassCaptcha():
    pass

driver = Chrome(executable_path=chrome_bin,options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url_login = "https://www.betano.pe/casino/myaccount/login"
url = "https://www.betano.pe/casino/games/aviator/3337"
driver.get(url)
human_delay()

#data = driver.find_element(By.XPATH,py).text

#print(f"{data}")

while True:
    pass

driver.quit()
