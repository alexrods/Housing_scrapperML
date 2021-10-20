"""
This file collect links of all pages of a search of houses rent, the links of each house and their characteristics
and return a table with all information
"""
import pandas as pd
import requests
import lxml.html as html


# scraping characteristics of houses
def scrap_characteristics(link):
    try:
        house = requests.get(link)
        house_page = house.content.decode('utf-8')
        home_parsed = html.fromstring(house_page)
        name_chars = home_parsed.xpath('//div[@class="ui-pdp-specs__table"]//tr[@class="andes-table__row"]/th[@class="andes-table__header andes-table__header--left ui-pdp-specs__table__column ui-pdp-specs__table__column-title"]/text()')
        num_chars = home_parsed.xpath('//div[@class="ui-pdp-specs__table"]//tr[@class="andes-table__row"]//span[@class="andes-table__column--value"]/text()')
        price = home_parsed.xpath('//span[@class="price-tag-amount"]/span[@class="price-tag-fraction"]/text()')
        link_location = home_parsed.xpath('//div[@id="ui-vip-location__map"]/div[@role="button"]/img[@decoding="async"]/@src')

        return make_table(link, name_chars, num_chars, price, link_location)

    except ValueError as ve:
        print("Value not found ", ve)


# Make a table with all characteristics
def make_table(link, cols, nums, price, location):
    data = nums + price
    col = cols + ["Precio"]
    table = pd.DataFrame(data, index=col)
    table = table.T
    table["URl"] = link
    table["ubicacion"] = location

    return table


# Collect links
def scrap_houses():
    try:
        HOME_URL = 'https://inmuebles.mercadolibre.com.mx/casas/renta/guanajuato/leon/'
        try:
            all_link_homes = []
            while HOME_URL:
                response = requests.get(HOME_URL)
                home = response.content.decode('utf-8')
                parsed = html.fromstring(home)
                links_to_homes = parsed.xpath('//li[@class="ui-search-layout__item"]//div[@class="ui-search-result__image"]/a/@href')
                all_link_homes = all_link_homes + links_to_homes
                next_page = parsed.xpath('//li[@class="andes-pagination__button andes-pagination__button--next"]/a/@href')
                HOME_URL = next_page[0]
        except Exception as e:
            print("Parsed pages")

        for i in range(len(all_link_homes)):
            if i == 0:
                df = scrap_characteristics(all_link_homes[i])
            else:
                df = pd.concat([df, scrap_characteristics(all_link_homes[i])])

        print(f'{len(df)} houses found')
        df.to_csv('data_houses.csv', encoding='utf-8')

    except ValueError as ve:
        print(ve)
        
# If you only want make scraping uncomment the next line
#scrap_houses()
