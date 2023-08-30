from datetime import timedelta, date
import requests
from bs4 import BeautifulSoup
import re

# lotto max // lotto 69 // canada


def encodeDate(dateob):
    answer = dateob.strftime("%m") + "%2F"
    answer = answer + dateob.strftime("%d") + "%2F"
    answer = answer + dateob.strftime("%Y") + "&submitForm=Submit"
    return answer


fl5 = open("fl_fant_5.csv", "w")
fl5.write(
    ",".join(
        [
            "drawdate",
            "n1",
            "n2",
            "n3",
            "n4",
            "n5",
            "winners5",
            "winners4",
            "winners3",
            "prize5",
            "prize4",
            "prize3",
        ]
    )
    + "\n"
)
url_stem = "http://www.flalottery.com/site/winningNumberSearch?searchTypeIn=date&gameNameIn=FANTASY5&singleDateIn="
start_date = date(2023, 8, 10)
end_date = date(2023, 8, 16)
current = start_date
while current < end_date:
    url = url_stem + encodeDate(current)
    page = requests.get(url).text
    bsPage = BeautifulSoup(page)
    numbers = bsPage.find_all("div", class_="winningNumbers")
    balls = bsPage.find_all("span", class_="balls")
    rem_balls = []
    rem_balls = balls
    draws = []
    while len(rem_balls):
        draw_1 = ""
        for _ in range(5):
            draw_1 += " " + balls[0].get_text()
            rem_balls.pop(0)
        print(draw_1)
        draws.append(draw_1)
        for _ in range(5):
            try:
                rem_balls.pop(0)
            except:
                continue
    temp = numbers[0].get_text()
    winners = bsPage.find_all("td", class_="column2")
    winners = [tag.get_text().replace(",", "") for tag in winners[:-1]]
    prizes = bsPage.find_all("td", class_="column3 columnLast")
    prizes = [tag.get_text().replace("$", "").replace(",", "") for tag in prizes[:-1]]
    fl5.write(
        ",".join(
            [current.strftime("%Y-%m-%d")] + draws[: len(winners)] + winners + prizes
        )
        + "\n"
    )
    print(current.strftime("%Y-%m-%d"))
    current = current + timedelta(1)

fl5.close()
print("done")

# # fl_lucky_money

# fllm = open("fl_lucky_money.csv", "w")
# fllm.write(
#     ",".join(
#         [
#             "drawdate",
#             "n1",
#             "n2",
#             "n3",
#             "n4",
#             "luckyball",
#             "win41",
#             "win40",
#             "win31",
#             "win30",
#             "win21",
#             "win11",
#             "win20",
#             "prize41",
#             "prize40",
#             "prize31",
#             "prize30",
#             "prize21",
#             "prize11",
#             "prize20",
#         ]
#     )
#     + "\n"
# )
# url_stem = "http://www.flalottery.com/site/winningNumberSearch?searchTypeIn=date&gameNameIn=LUCKYMONEY&singleDateIn="
# start_date = date(2014, 7, 4)
# end_date = date(2015, 10, 24)
# current = start_date
# while current < end_date:
#     while current.strftime("%w") not in ["2", "5"]:
#         current = current + timedelta(1)
#     url = url_stem + encodeDate(current)
#     page = requests.get(url).text
#     bsPage = BeautifulSoup(page)
#     numbers = bsPage.find_all("div", class_="winningNumbers")
#     balls = bsPage.find_all("span", class_="balls")
#     temp = numbers[0].get_text()
#     draws = re.split("[-\n]", temp)
#     draws = draws[1:6]
#     winners = bsPage.find_all("td", class_="column2")
#     winners = [tag.get_text().replace(",", "") for tag in winners[:-1]]
#     prizes = bsPage.find_all("td", class_="column3 columnLast")
#     prizes = [tag.get_text().replace("$", "").replace(",", "") for tag in prizes[:-1]]
#     fllm.write(
#         ",".join([current.strftime("%Y-%m-%d")] + draws + winners + prizes) + "\n"
#     )
#     print(current.strftime("%Y-%m-%d"))
#     current = current + timedelta(1)

# fllm.close()

# # nc_cash

# ncc5 = open("nc_cash_5.csv", "w")
# ncc5.write(
#     ",".join(
#         [
#             "drawdate",
#             "n1",
#             "n2",
#             "n3",
#             "n4",
#             "n5",
#             "winners5",
#             "winners4",
#             "winners3",
#             "prize5",
#             "prize4",
#             "prize3",
#         ]
#     )
#     + "\n"
# )
# url_stem = "http://www.nc-educationlottery.org/cash5_payout.aspx?drawDate="
# start_date = date(2006, 10, 27)
# end_date = date(2015, 10, 27)
# current = start_date
# p = re.compile("[,$]")
# while current < end_date:
#     print(current.strftime("%Y-%m-%d"))
#     url = url_stem + current.strftime("%m/%d/%Y")
#     page = requests.get(url).text
#     bsPage = BeautifulSoup(page)

#     draws = []
#     draws.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Num1")[0].get_text(),
#         )
#     )
#     draws.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Num2")[0].get_text(),
#         )
#     )
#     draws.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Num3")[0].get_text(),
#         )
#     )
#     draws.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Num4")[0].get_text(),
#         )
#     )
#     draws.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Num5")[0].get_text(),
#         )
#     )

#     winners = []
#     winners.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Match5")[
#                 0
#             ].get_text(),
#         )
#     )
#     winners.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Match4")[
#                 0
#             ].get_text(),
#         )
#     )
#     winners.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Match3")[
#                 0
#             ].get_text(),
#         )
#     )

#     prizes = []
#     prizes.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Match5Prize")[
#                 0
#             ].get_text(),
#         )
#     )
#     prizes.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Match4Prize")[
#                 0
#             ].get_text(),
#         )
#     )
#     prizes.append(
#         p.sub(
#             "",
#             bsPage.find_all("span", id="ctl00_MainContent_lblCash5Match3Prize")[
#                 0
#             ].get_text(),
#         )
#     )
#     if prizes[0] == "Rollover":
#         prizes[0] = "0"
#     ncc5.write(
#         ",".join([current.strftime("%Y-%m-%d")] + draws + winners + prizes) + "\n"
#     )
#     current = current + timedelta(1)

# ncc5.close()
# print("finished")

# from selenium import webdriver
# from time import sleep


# def GetTnCashData(url):
#     page = requests.get(url).text
#     bsPage = BeautifulSoup(page)
#     temp = bsPage.find_all("td", class_="SmallBlackText")
#     winners = []
#     prizes = []
#     for i in range(1, 8):
#         winners.append(temp[3 * i + 1].get_text())
#         prizes.append(temp[3 * i + 2].get_text().replace("$", "").replace(",", ""))
#     return winners + prizes


# def cleanDate(strdate):
#     temp = strdate.split("/")
#     return date(int(temp[2]), int(temp[0]), int(temp[1])).strftime("%Y-%m-%d")


# tnc = open("tn_cash.csv", "w")
# tnc.write(
#     ",".join(
#         [
#             "drawdate",
#             "n1",
#             "n2",
#             "n3",
#             "n4",
#             "n5",
#             "cashball",
#             "win51",
#             "win50",
#             "win41",
#             "win40",
#             "win31",
#             "win30",
#             "win21",
#             "prize51",
#             "prize50",
#             "prize41",
#             "prize40",
#             "prize31",
#             "prize30",
#             "prize21",
#         ]
#     )
#     + "\n"
# )
# driver = webdriver.Firefox()
# driver.get(
#     "https://www.tnlottery.com/winningnumbers/TennesseeCashlist.aspx?TCShowall=y#TennesseeCashball"
# )
# html = driver.page_source
# nextLink = "navTennesseeCashNextPage"
# soup = BeautifulSoup(html)
# for pg in range(0, 20):
#     temp = soup.find_all("td", align="center")
#     top = (len(temp) - 4) / 3 + 1
#     print(pg, len(temp))
#     for i in range(1, top):
#         drawDate = [cleanDate(temp[3 * i].get_text())]
#         NumsDrawn = temp[3 * i + 1].get_text().replace("-", " ").split(" ")
#         drawID = temp[3 * i + 2].a.get("href")
#         drawID = drawID[drawID.index("=") + 1 :]
#         drawID = drawID[: drawID.index("'")]
#         drawData = GetTnCashData(
#             "https://www.tnlottery.com/winningnumbers/TennesseeCashdetails_popup.aspx?id="
#             + drawID
#         )
#         tnc.write(",".join(drawDate + NumsDrawn + drawData) + "\n")
#     driver.find_element_by_id(nextLink).click()
#     sleep(30)
#     soup = BeautifulSoup(driver.page_source)

# tnc.close()
# print("Done")
