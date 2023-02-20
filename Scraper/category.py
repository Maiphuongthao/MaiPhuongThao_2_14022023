import csv
from pathlib import Path

import scrape_book

url_1 = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"

"""def page(soup):
    pager = soup.find('li', class_='current').text
    if pager is None:
        return 1
    else:
        page_text = pager.strip()[-1]
        number_page = int(page_text)
        return number_page"""


def get_books_infos(soup):
    """
    scrape page and get dictionary of all books on page
    return dictionary of books
    :param soup:
    :return:
    """
    books_url = soup.find_all("h3")
    books_infos = []

    for book in books_url:
        url = scrape_book.main_url + 'catalogue/' + book.a['href'].strip('../../../')
        book_info = scrape_book.scrape_one_book(url)
        books_infos.append(book_info)
    return books_infos


def write_to_csv(books, category_name):
    file_name = f'books_in_{category_name}_category.csv'
    file_path = Path("../csv")

    if not Path(file_path).exists():
        Path.mkdir(file_path)

    with open(str(file_path) +"/"+ file_name, 'w', newline='') as book_csv:
        writer = csv.DictWriter(book_csv, fieldnames=books[0])
        writer.writeheader()
        writer.writerows(books)


def scrape_categories(url_category):
    soup = scrape_book.scrape_url(url_1)
    # pager = page(soup)
    books = []
    category_name = soup.h1.text.replace(" ", "_")
    books.extend(get_books_infos(soup))
    pager = soup.find('li', class_='next')

    # if pager > 1:
    # for p in range(1, pager + 1):
    while pager:
        page_url = pager.find('a')['href']
        next_link = url_category.replace("index.html", page_url)
        soup = scrape_book.scrape_url(next_link)
        books.extend(get_books_infos(soup))
        pager = soup.find('li', class_='next')
    # else:
    write_to_csv(books, category_name)
    return books


print(len(scrape_categories(url_1)))
