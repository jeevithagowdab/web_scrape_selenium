"""
GitHub : https://github.com/jeevithagowdab/web_scrape_selenium

Scrape Smartprix Website for HTML Data

This script scrapes the HTML source of Smartprix webpages after clicking checkboxes and scrolling to the end of the page.
It is designed to be used for different categories of products on the Smartprix website.

"""


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


def scrape_smartprix_html(url, xpath):
    """
    Scrapes the HTML source of a webpage from Smartprix after clicking checkboxes and scrolling to the end of the page.

    Parameters:
        url (str): The URL of the Smartprix webpage to scrape.
        xpath (str): The XPath of the element to click for loading more items.

    Returns:
        str: The HTML source of the scraped webpage.
    """
    # Path to the chromedriver.exe file
    s = Service(
        "E:/1 DSMP/6.Data Analysis/wb scrapping selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe")

    # Initialize the Chrome WebDriver with the specified service
    driver = webdriver.Chrome(service=s)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the page to load
        time.sleep(1)

        # Click on the checkboxes for filtering the products (specific to mobiles page)
        if 'mobiles' in url:
            try:
                checkbox1 = driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
                checkbox1.click()
                time.sleep(1)
                checkbox2 = driver.find_element(By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
                checkbox2.click()
                time.sleep(2)
            except Exception as e:
                print("Error occurred while clicking checkboxes:", e)
                # If there's an error, print it and continue without raising an error or stopping the execution.

        # Get the initial height of the page
        old_height = driver.execute_script('return document.body.scrollHeight')

        # Loop to scroll until the end of the page
        while True:
            try:
                # Wait for the element to be clickable
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                # Click on the element
                element.click()
                time.sleep(1)
            except NoSuchElementException:
                # If no more elements are found, break out of the loop
                print("No more elements to load.")
                break
            except Exception as e:
                print("Error occurred while clicking element:", e)
                # If there's an error, print it and continue without raising an error or stopping the execution.

            # Get the new height of the page after scrolling
            new_height = driver.execute_script('return document.body.scrollHeight')
            # If the page height hasn't changed, it means we've reached the end
            if new_height == old_height:
                break
            # Update the old height to the new height
            old_height = new_height

        # Your scraping logic here

        # Get the HTML source of the page
        html = driver.page_source

        return html

    finally:
        # Close the browser
        driver.quit()
