from ascii_scrape import ascii_scrape_book
from Scraper.site import scrape_all_categories
from Scraper.scrape_book import main_url

import time

url = main_url

print(ascii_scrape_book)
print('Scrapping....')
def main(main_url):

    start_time = time.time()

    scrape_all_categories(main_url)
    time_difference = time.time() - start_time
    print(f'Scraping time: %2d seconds.'%time_difference)

main(url)

print('End')