from webbrowser import Chrome
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# option = webdriver.ChromeOptions()
# option.binary_location=r"/etc/alternatives/brave-browser"

service = Service(executable_path="/home/kriot/Dev/chromedriver")
driver = webdriver.Chrome(service=service)

