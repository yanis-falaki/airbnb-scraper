import time
from bs4 import BeautifulSoup
from selenium import webdriver

# launch chrome and navigate to website
browser = webdriver.Chrome()
browser.get("https://airbnb.com/h/livmtl-plaza-2")

# images are added dynamicallly, so must wait for it to load
time.sleep(1)

# save the html in a variable to be parsed later
html = browser.page_source
print(html)