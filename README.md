
```
               ___              __              __                                             
              / _ ) ___  ___   / /__  ___      / /_ ___        ___ ____  ____ ___ _   ___  ___ 
             / _  |/ _ \/ _ \ /  '_/ (_-<     / __// _ \      (_-</ __/ / __// _ `/  / _ \/ -_)
            /____/ \___/\___//_/\_\ /___/     \__/ \___/     /___/\__/ /_/   \_,_/  / .__/\__/ 
                                                                                   /_/         

```


<p align="center">
    <a href="https://www.python.org">
        <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white" alt="python-badge">
    </a>
    <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">
        <img src="https://img.shields.io/badge/BeautifulSoup-4.11+-d71b60?style=flat" alt="Beautiful Soup">
    </a>
    <a href="https://github.com/psf/requests">
        <img src="https://img.shields.io/badge/Requests-2.28+-00838f?style=flat" alt="Requests">
    </a>
</p>


# Objectives

Scraping of [book to scrape](http://books.toscrape.com/) with **BeautifulSoup4** and **Requests**, export book datas to .csv files and download cover images to the *"images"* folder.

:+1: **ETL** process:

**Extract* relevent data from source web site.

**Transform* Filter, convert and clean data

**Load* data into files


# Setup


### Clone the repository

- `git clone https://github.com/Maiphuongthao/MaiPhuongThao_2_14022023`


### Create the virtual environment

- `cd MaiPhuongThao_2_14022023`
- `python -m venv env`
- Activate the environment `source env/bin/activate` (macOS and Linux) or `env\Scripts\activate` (Windows)


### Install required packages

- `pip install -r requirements.txt`



# Usage

To scrape the entirety of [books to scrape](https://books.toscrape.com) to .csv files, and to download the cover images
use the command `python main.py`.


To open the exported .csv files, follow the instruction [here](https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/)



