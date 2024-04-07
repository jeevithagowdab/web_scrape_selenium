"""
GitHub : https://github.com/jeevithagowdab/web_scrape_selenium

"""

from main import scrape_smartprix_html

# Specify the XPath for mobiles page
mobiles_xpath = '//*[@id="app"]/main/div[1]/div[2]/div[3]'

# Call the function with the mobiles URL and XPath
mobiles_html = scrape_smartprix_html('https://www.smartprix.com/mobiles', mobiles_xpath)

# mobiles_html write
with open('smartprix_mobiles.html', 'w', encoding='utf-8') as f:
    f.write(mobiles_html)
