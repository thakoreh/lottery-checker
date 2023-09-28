import requests
import re
from bs4 import BeautifulSoup
import csv
import datetime
# Define your header
header = ["Lottery Date", "Lottery Numbers"]

import os

# Check if the file exists
if not os.path.isfile("scrape_data.csv"):
    # To create a new CSV file and write data:
    with open("scrape_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(header)


for year in range(2023, 2024):  # Loop through the years 1994 to 2024
    url = f"https://www.national-lottery.com/lotto/results/{year}-archive"  # Construct the URL for each year's lottery results
    response = requests.get(url)  # Send a GET request to the URL
    soup = BeautifulSoup(response.content, "html.parser")  # Parse the HTML content of the response

    # Use BeautifulSoup to extract specific data from the HTML.
    # Find all the winning numbers:
    winning_numbers = soup.find_all("ul", class_="balls")

    # Find all the dates for the draws:
    dates_for_draw = soup.find_all("td", class_="noBefore colour")

    # Open the existing CSV file in read mode to load existing data:
    with open("scrape_data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        existing_data = list(reader)

    # Open the existing CSV file in write mode:
    with open("scrape_data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer

        # Loop through each pair of winning numbers and draw dates:
        for number, date in zip(winning_numbers, dates_for_draw):
            # Prepare the row with the draw date and winning numbers
            # Convert the date format from 'Saturday9th September 2023' to '09-09-2023'
            # date_formatted = datetime.datetime.strptime(date.text, '\n%A%dth %B %Y\n').strftime('%d-%m-%Y')
            row = [re.sub(r"\n", " ", date.text), re.sub(r"\n", " ", number.text)]

            # Check if the row already exists in the CSV file
            if row not in existing_data:
                # If not, write the row to the CSV file
                writer.writerow(row)
                # Print the winning numbers (with newline characters replaced by spaces)
                print(re.sub(r"\n", " ", number.text))


from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import csv

class Numbers(BaseModel):
    numbers: List[int]

app = FastAPI()
@app.get('/')
async def home():
    return {'message':"Hello"}


@app.get('/check_probability/{numbers}')
async def check_probability(numbers: str):
    user_numbers = list(map(int, numbers.split(',')))
    print(user_numbers)
    total_draws = 0
    winning_draws = 0
    max_percent = 0

    with open("scrape_data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header



        for row in reader:
            print(row[1])
            print(user_numbers)

            lotter_numbers_pick = []
            for num in row[1].split(' '):
                try:
                    lotter_numbers_pick.append(int(num))
                except ValueError:
                    continue
            

            def match_percentage(l1, l2):
                matches = set(l1) & set(l2)
                positional_matches = sum([1 for i, j in zip(l1, l2) if i == j])
                percentage = ((len(matches) + positional_matches) / (2 * len(set(l1)))) * 100
                return percentage

            match_percent = match_percentage(user_numbers, lotter_numbers_pick)
            # print("Match Percentage : ", match_percent)
            if max_percent < match_percent:
                max_percent = match_percent
            print("Match Percentage : ", max_percent)


    return {'probability': max_percent}
