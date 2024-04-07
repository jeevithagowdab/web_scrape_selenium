"""
GitHub : https://github.com/jeevithagowdab/web_scrape_selenium

"""

from main import scrape_smartprix_html

# Specify the XPath for tablets page
tablets_xpath = '//*[@id="app"]/main/div[1]/div[3]/div[3]'

# Call the function with the tablets URL and XPath
tablets_html = scrape_smartprix_html('https://www.smartprix.com/tablets', tablets_xpath)

# to handle tablets_html:
with open('smartprix_tablets.html', 'w', encoding='utf-8') as f:
    f.write(tablets_html)
