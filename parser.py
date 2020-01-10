from bs4 import BeautifulSoup
import requests

URL = 'https://vilki-palki.od.ua/pizza'
DATA = []

response = requests.get(URL)
contents = response.text
soup = BeautifulSoup (contents, 'lxml')
div = soup.find_all("div",{"class": "item"})

for row in div:
    price_all = row.find_all("span", {"class": "day"})
    name_all = row.find_all("div", {"class": "name fl2"})
    description_all = row.find_all("div", {"class": "cont-text fl1"})
    image_url_all = row.find_all("div", {"class": "img"})

    price = price_all[0].span.contents[0]
    name = name_all[0].a.contents[0].strip()
    description = description_all[0].contents[0].rstrip()
    image_url = "https://vilki-palki.od.ua/" + image_url_all[0].img.attrs["src"]

    DATA.append({
        name: {
            "name": name,
            "price": price,
            "description": description,
            "image_url": image_url,
        }
    })

for item in DATA:
    print(item)
