import csv
from pathlib import Path

import requests

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

    path = file_path.joinpath(file_name)
    with open(path, 'w', newline='') as book_csv:
        writer = csv.DictWriter(book_csv, fieldnames=books[0])
        writer.writeheader()
        writer.writerows(books)


def save_image(books):
    file_path = Path("../images")

    if not Path(file_path).exists():
        Path.mkdir(file_path)

    for book in books:
        image_source = requests.get(book["product_page_url"])
        suffix = Path(book["product_page_url"]).suffix

        name = book["title"].translate({ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        if suffix not in ['.jpg', '.jpeg', '.png', '.gif']:
            output = name + ".png"
        else:
            output = name + suffix
        path = file_path.joinpath(output)
        with open(path, 'wb') as file:
            file.write(image_source.content)


def scrape_categories(url_category):
    """
    scrap books's url
    scrape 1st page then continue scraping next page
    :param url_category:
    :return:
    """
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
    save_image(books)
    return books


print(len(scrape_categories(url_1)))
