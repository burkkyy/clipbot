from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path="/usr/bin/google-chrome-stable")

driver.get('https://google.com')

print(driver.page_source)

driver.quit()
