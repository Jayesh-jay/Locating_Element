from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Step 1: Open the Instagram profile page
driver.get("https://www.instagram.com/guviofficial/")

# Allow some time for the page to load
time.sleep(5)

# Step 2: Extract the total number of followers and following using XPath
followers_element = driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button')
following_element = driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button')

followers_count = followers_element.get_attribute('title') or followers_element.text
following_count = following_element.get_attribute('title') or following_element.text

print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the browser window
driver.quit()
