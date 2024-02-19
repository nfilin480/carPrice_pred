import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from fake_useragent import FakeUserAgentError
from math import ceil
from random import randint
from time import sleep
from base64 import b64decode
from io import BytesIO
from PIL import Image
import pandas as pd
from tqdm import tqdm

#URL = "https://www.avito.ru/all/avtomobili?f=ASgBAgICAUTyCrCKAQ" #не битые авто
URL = "https://www.avito.ru/all/avtomobili?f=ASgBAgECAUTyCrCKAQFF~owUF3siZnJvbSI6bnVsbCwidG8iOjIwMjB9" #последние объявления до 2020 года авто

NAME_TAG = 'h3[itemprop="name"]'
PRICE_TAG = 'meta[itemprop="price"]'
PARAMS_TAG = 'p[data-marker="item-specific-params"]'
DESC_TAG = 'div[class="iva-item-descriptionStep-C0ty1"]'
REGION_TAG = 'div[class="geo-root-zPwRk"]'

class AvitoParser:

    def __init__(self):

        try:
            ua = UserAgent().chrome
        except FakeUserAgentError:
            ua = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={ua}")
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def __get_popular_models__(self, url = URL):
        self.driver.get(url)

        popular_models = self.driver.find_element(
            by=By.CSS_SELECTOR, value='div[data-marker="popular-rubricator/links"]'
        ).find_elements(
            by=By.CSS_SELECTOR, value='a[data-marker="popular-rubricator/link"]'
        )

        return popular_models
    
    def parser(self, url = URL, model = None):
        models = self.__get_popular_models__(url)

        for i, model in enumerate(models):
            url_model = model.get_attribute("href")
            df = self.__parse_model__(url_model=url_model)
            df.to_csv(f'./datasets2/data{i}.csv')
            self.driver.quit()

    
    def __find_elements__(self, offer, tag, attribute = None):

        try:
            if attribute == None:
                return offer.find_element(
                        by=By.CSS_SELECTOR, value=tag
                    ).text
            else:
                return offer.find_element(
                        by=By.CSS_SELECTOR, value=tag
                    ).get_attribute(attribute)
            
        except Exception as ex:
            print(ex)

        
    def __parse_model__(self, page_num = 50, url_model = None):
        
        if url_model == None:
            return None

        df = pd.DataFrame(columns=['name', 'price', 'params', 'desc', 'region'])

        self.driver.get(url_model)

        for _ in range(page_num):

            offers = self.driver.find_elements(
                by=By.CSS_SELECTOR, value='div[data-marker="item"]'
            )

            for offer in offers:

                avito_id = int(offer.get_attribute("id")[1:])
                name = self.__find_elements__(offer, tag = NAME_TAG)
                price = self.__find_elements__(offer, tag = PRICE_TAG, attribute="content")
                params = self.__find_elements__(offer, tag = PARAMS_TAG)
                desc = self.__find_elements__(offer, tag = DESC_TAG)
                region = self.__find_elements__(offer, tag = REGION_TAG)

                df.loc[avito_id, 'name':'region'] = [name, price, params, desc, region]

            try:    
                self.driver.find_element(
                    by=By.CSS_SELECTOR, value='a[data-marker="pagination-button/nextPage"]'
                ).click()

                rand_sleep = randint(25, 49)
                sleep(rand_sleep / 10)

            except Exception as ex:
                    print(ex)

        return df

a = AvitoParser(URL)
a.parser()