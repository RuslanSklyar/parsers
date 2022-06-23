from bs4 import BeautifulSoup
import requests


def main(input_vac):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    f = open("save.txt", "w")
    for count in range(1, 10):
        link = f"https://www.work.ua/jobs-{input_vac}/?page={count}"
        response = requests.get(link, headers=header)
        soup = BeautifulSoup(response.text, "lxml")

        table = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link")

        for i in table:
            vacancy = i.find("h2", class_="").text.replace("\n", "")
            company = i.find("div", class_="add-top-xs").find("span").text
            url = "https://www.work.ua" + i.find("a").get("href")
            money = i.find_all("b")

            if "грн" in money:
                info = vacancy + " " + company + " " + money + " " + url
            else:
                info = vacancy + " " + company + " " + url

            f.write(info + "\n")
    f.close()


if __name__ == "__main__":
    inpt_vac = input("Введите вакансию:").replace(" ", "+")
    main(inpt_vac)
