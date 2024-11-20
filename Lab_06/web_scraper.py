from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd
import random

if __name__ == '__main__':

    url = "https://www.mimuw.edu.pl/pl/aktualnosci/"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error occurred while retrieving the page. Error code: {response.status_code}")
    else:
        soup = BeautifulSoup(response.content, "html.parser")

        elements = soup.find_all("div", class_="masonry-item news-archive-item")

        list_of_dicts = []

        print(f"liczba elementów: {len(elements)}")

        for element in elements:
            link = element.find('a')
            link_url = urljoin(url, link['href']) if link and link.has_attr('href') else None

            dict = {
                "date": element.find("div", class_="news-archive-item-date").text.strip(),
                "title": element.find("h2").text.strip(),
                "link": link_url
            }

            list_of_dicts.append(dict)

        df = pd.DataFrame(list_of_dicts)

        # Saving data to csv file
        df.to_csv("events.csv", index=False)

        # Printing random 5 events
        random_events = random.sample(list_of_dicts, 5)
        print("Random 5 events:")
        for event in random_events:
            print(f"Title: {event['title']}")
            print(f"URL: {event['link']}")
            print(f"Date: {event['date']}\n")
