from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd  # To store data in dataframe
from bs4 import BeautifulSoup

start_time = time()
URL = 'https://edgein.io'
# setting the webdriver for chrome
service = Service(executable_path="C:\Development\chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

# Login to web page
driver.get(URL)
driver.maximize_window()
login = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/nav/div[2]/button[1]')
login.click()
sleep(1)
linkedin_login = driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-panel-:r1:"]/div/button')
linkedin_login.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys("************")
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("*******")
sign_in = driver.find_element(By.XPATH, '//*[@id="app__container"]/main/div[2]/form/div[3]/button')
sign_in.click()
sleep(2)
companies = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/nav/div[2]/a[1]')
companies.click()

# Scroll down the page
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")

# First Page
# Store the page source
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Retrieve the url for each box
headers = soup.find_all('a', class_="cursor-pointer")
url_list = []
data = {}
for header in headers:
    name = header.find('div', class_="flex items-center justify-center pl-2 md:overflow-visible").get_text()
    url = "https://edgein.io" + header['href']
    data = {
        "name": name,
        "url": url,
    }
    url_list.append(data)

# Go to the next page
next_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div/nav/div[2]/button')
next_button.click()

# Second Page
# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")
# Scroll down the page
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
sleep(1)
# Store the page source
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Retrieve the url for each box
headers = soup.find_all('a', class_="cursor-pointer")
for header in headers:
    name = header.find('div', class_="flex items-center justify-center pl-2 md:overflow-visible").get_text()
    url = "https://edgein.io" + header['href']
    data = {
        "name": name,
        "url": url,
    }
    url_list.append(data)


# Scrape third page until 10th page

for i in range(8):
    # Go to the next page
    next_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[2]/div/nav/div[2]/button[2]')
    next_button.click()

    # Scroll to the top of the page
    driver.execute_script("window.scrollTo(0, 0);")
    # Scroll down the page
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
    sleep(1)
    # Store the page source
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Retrieve the url for each box
    headers = soup.find_all('a', class_="cursor-pointer")
    for header in headers:
        name = header.find('div', class_="flex items-center justify-center pl-2 md:overflow-visible").get_text()
        url = "https://edgein.io" + header['href']
        data = {
            "name": name,
            "url": url,
        }
        url_list.append(data)

print(url_list)

# create csv

df = pd.DataFrame(url_list)
df.to_csv('url_list.csv', index=False)
print("Data created success")
print("Total rows", len(url_list))
end_time = time()
total_time = end_time - start_time
print("\n" + str(total_time))




















