from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://careers.google.com/jobs/results/'

driver = webdriver.Chrome()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)


job = driver.find_element(
    By.XPATH, '//*[@id="46"]').send_keys("Software Engineering")

driver.find_element(
    By.XPATH, '//*[@id="46"]').send_keys(Keys.RETURN)

# dropDown = driver.find_element(
#     By.XPATH, '//*[@id="accordion-location"]').click()
# location = driver.find_element(
#     By.XPATH, '//*[@id="location"]').send_keys('India')

# India = driver.find_element(
#     By.XPATH, '//*[@id="autocomplete-result-1666-0"]').click()

card = driver.find_element(By.CLASS_NAME, 'gc-card__title').text

header = driver.find_element(By.CLASS_NAME, 'gc-card__header')
location = header.find_elements(By.TAG_NAME, 'span')

address = ""
for addr in location:
    address += addr.text

para = driver.find_element(By.CLASS_NAME, 'gc-card__preview')

eligiblity = para.find_elements(By.TAG_NAME, 'li')

prev = ""

if card + address != prev:
    print(card, address)
    for qual in eligiblity:
        print(qual.text)

prev = card + address

# make a sheet jismai 1 row for google, 2nd for microsoft etc etc.
# now take the prev data from that sheet, if prev == curr data toh don't update the data in the sheet jaha se bot msgs render karta h.
# if there's a change toh update in the sheet jaha se bot render karta h

# now make a string out of heading and location and check if equal to prev?
# if equal then dont update the sheet
# if not then update the sheet with this info and also set prev as this string

# XPATH can be used for elements that dont change positions. Xpath gives the exact same element. Kind of an identifier to a particalar element on the page
# class name, tag name, are more general.
# click() , send_keys()  - some selenium functions to automate commands on browser
