from datetime import datetime
import selectorlib
import requests
import sqlite3

# define URL of the webpage to be scraped
URL = "https://programmer100.pythonanywhere.com/"


# define a scrape function to scrape text from web page
def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


# define function to extract the temperature data source selector
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperatures"]
    return value


def init_db():
    # Function to create database table if not existing already
    with sqlite3.connect("data.db", timeout=10) as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS temperatures (datetime TEXT,temperature REAL)")


# function to store scraped temperatures into SQL database table
def store(extracted):
    current_datetime = datetime.now()
    formatted_time = current_datetime.strftime('%Y-%m-%d-%H-%M-%S')
    row = [formatted_time, extracted]
    with sqlite3.connect("data.db", timeout=10) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO temperatures VALUES(?,?)", row)
        connection.commit()


# code to store datae into a file instead
# with open("data.txt", "a") as file:
#     current_datetime = datetime.now()
#     # timestamp = current_datetime.timestamp()    # timestamp[ step is not required
#     # local_time = datetime.fromtimestamp(timestamp)
#     formatted_time = current_datetime.strftime('%Y-%m-%d-%H-%M-%S')
#     # print(formatted_time)
#     file.write(f'{formatted_time}, {extracted} \n')

# function to read data if reading from a file. This function should called from webapp.py
# def read(extracted):
#     with open("data.txt", "r") as file:
#         return file.read()

# code to execute the program steps
if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    init_db()
    store(extracted)
