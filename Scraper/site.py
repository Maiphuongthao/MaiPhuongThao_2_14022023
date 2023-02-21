from Scraper import category
from Scraper import scrape_book
import emoji
def scrape_all_categories(main_page):
    """
    to main_page get all categories url to scrape
    :return:
    """
    soup = scrape_book.scrape_url(main_page)

    all_categories = soup.select('.side_categories ul li ul li a')
    number_categories = len(all_categories)
    for category_url in all_categories:
        url = main_page + '/' + category_url.get('href')
        category.scrape_one_category(url)


    print(emoji.emojize(':books: :books:'))
    print(f'{number_categories} categories in {main_page}')
    print(emoji.emojize(':books: :books:'))