from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas

browser = webdriver.Chrome("./chromedriver-win64/chromedriver.exe")
browser.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
time.sleep(5)

planets_data = []
soup = BeautifulSoup(browser.page_source, "html.parser")
bright_star_table = soup.find('table', attrs=["class", "wikitable"])

table_body = bright_star_table.find("tbody")

table_rows = table_body.find_all('tr')

scraped_data = []

def scrape():
    for rows in table_rows:
        table_cols = rows.find_all('td')
        print(table_cols)
        temp_list = []

        for col_data in table_cols:
            data=col_data.text.strip()

            temp_list.append(data)
        scraped_data.append(temp_list)

    star_data = []
    for i in range(0, len(scraped_data)):
        star_names = scraped_data[i][1]
        distance = scraped_data[i][3]
        mass = scraped_data[i][5]
        radius = scraped_data[i][6]
        lum = scraped_data[i][7]
        required_data = [star_names, distance, mass, radius, lum]
        star_data.append(required_data)

        headers = ["star_names", "distance", "mass", "radius", "lum"]

        star_df_1 = pandas.DataFrame(star_data, columns=headers)
        star_df_1.to_csv('scraped-data.csv', index=True, index_label="id")


scrape()