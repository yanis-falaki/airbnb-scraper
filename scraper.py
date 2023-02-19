import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os

links = ['livmtl-plaza-2', 
        'livmtl-plaza-3',
        'livmtl-penthouse',
        'livmtl-avenue-1275',
        'livmtl-avenue-1277',
        'livmtl-soho-1',
        'livmtl-soho-2',
        'livmtl-soho-3',
        'livmtl-soho-4',
        'livmtl-soho-5',
        'livmtl-soho-6',
        'livmtl-soho-penthouse',]

# looping through all links necessary
for link in links:
  
  # launch chrome and navigate to website
  browser = webdriver.Chrome()
  browser.get(f"https://airbnb.com/h/{link}")

  # images are added dynamicallly, so must wait for it to load
  time.sleep(1.5)

  # save the initial web page
  html = browser.page_source

  # find the button for all images and press
  button = browser.find_element(By.CLASS_NAME, "l1j9v1wn.b1qnr4x4.c1p20n7u.dir.dir-ltr")
  button.click()

  # wait for images to load
  time.sleep(1.5)

  # set html to all images page to be parsed
  html = browser.page_source

  # parse html and store images in a list
  soup = BeautifulSoup(html, 'html.parser')
  images = soup.find_all('img', {'class': '_6tbg2q'})

  # loop through all images to save them
  for i in range(len((images))):

    # saving image data in a variable
    img_data = requests.get(images[i]['src']).content

    # writing the file name to make a directory
    filename = f'images/{link}/img{i}.jpg'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # saving the image to a file
    with open(filename, 'wb') as handler:
      handler.write(img_data)

  # closing the browser
  browser.close()