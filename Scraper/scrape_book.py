import re

import requests
from bs4 import BeautifulSoup

main_url = 'http://books.toscrape.com/'


def book_info(soup):
    # get infos of product information table
    info = soup.find('table', class_='table')
    product_info = {}
    for td in info:
        product_info["universal_product_code"] = info.select('tr>td')[0].text
        product_info["price_excluding_tax"] =info.select('tr>td')[2].text.strip('£')
        product_info["price_including_tax"] = info.select('tr>td')[3].text.strip('£')
        available = info.select('tr>td')[5].text
        # use regex to get only number
        product_info["number_available"] = re.findall("[0-9]+",available)[0]
    return product_info


def rating_number(soup):
    # get rating class of star then turn letters to numbers(string) of stars, return None if there is nothing
    review = soup.find('p', class_='star-rating')['class'][1]
    number = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    number_rating = number.get(review, "None")

    return number_rating


def scrape_url(url):
    # scrap url using requests and beautifulSoup
    res = requests.get(url)
    if (res.ok):
        soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def scrape_one_book(url):
    # get infos of one book together and put in book's library
    soup = scrape_url(url)

    title = soup.h1.text
    description = soup.select("article > p")[0].text
    category = soup.select("ul.breadcrumb > li")[2].text.strip()
    image = soup.find("img")['src'].strip('../../')
    image_url = main_url + image

    review_rating = rating_number(soup)

    info = book_info(soup)

    book = {'title': title, 'product_description': description, 'category': category, 'image_url': image_url,
            'review_rating': review_rating, 'universal_product_code': info["universal_product_code"],
            'price_excluding_tax': info["price_excluding_tax"], 'price_including_tax': info["price_including_tax"],
            "number_available": info["number_available"],'product_page_url':url}

    return book
