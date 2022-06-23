import csv
from bs4 import BeautifulSoup
import requests
from time import sleep


def main():
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    for count in range(1, 2):
        sleep(0.5)
        link = f"https://coinmarketcap.com/nft/upcoming/?page={count}"
        response = requests.get(link, headers=header)
        soup = BeautifulSoup(response.text, "lxml")

        table = soup.find_all("tr")

        for card in table:
            sleep(0.1)
            try:
                name = card.find("div", class_="sc-15yqupo-0 cqAZPF").find("p").find("span").text
                b_ch = card.find("div", class_="sc-15yqupo-0 cqAZPF").find("span", class_="lsid7u-0 kciUBo").text
                info = card.find("div", class_="sc-15yqupo-0 cqAZPF").find_all("p")[1].text
                discord = card.find("div", class_="sc-15yqupo-1 gEtvIk").find_all("p")[0].find("a").get("href")
                twitter = card.find("div", class_="sc-15yqupo-1 gEtvIk").find_all("p")[1].find("a").get("href")
                site = card.find("div", class_="sc-15yqupo-1 gEtvIk").find_all("p")[2].find("a").get("href")
                time = card.find("div", class_="sc-15yqupo-2 dhMNvT").find_all("p")[0].text + " " + card.find("div", class_="sc-15yqupo-2 dhMNvT").find_all("p")[1].text
                sale = card.find("div", class_="sc-1ay2tc4-0 dRIGnz").text

                with open("save.csv", "a", encoding="utf-8") as file:
                    write = csv.writer(file, delimiter=";")

                    write.writerow(
                        (
                            "Название",
                            "Блокчейн технология",
                            "Описание",
                            "Discord",
                            "Twitter",
                            "Сайт",
                            "Время",
                            "Цена"
                        )
                    )

                    write.writerow(
                        (
                            name,
                            b_ch,
                            info,
                            discord,
                            twitter,
                            site,
                            time,
                            sale
                        )
                    )

            except AttributeError:
                continue


if __name__ == "__main__":
    main()
