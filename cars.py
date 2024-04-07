"""
GitHub : https://github.com/jeevithagowdab/web_scrape_selenium

"""

from main import scrape_smartprix_html

# Specify the XPath for cars page
cars_xpath = '//*[@id="app"]/main/div[1]/div[3]/div[3]'

# Call the function with the cars URL and XPath
cars_html = scrape_smartprix_html('https://www.smartprix.com/cars', cars_xpath)

#  handle cars_html:
with open('smartprix_cars.html', 'w', encoding='utf-8') as f:
    f.write(cars_html)
