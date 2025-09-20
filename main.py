from datetime import datetime
import selectorlib
import requests

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


# function to store scraped temperatures into a file
def store(extracted):
    with open("data.txt", "a") as file:
        current_datetime = datetime.now()
        # timestamp = current_datetime.timestamp()    # timestamp[ step is not required
        # local_time = datetime.fromtimestamp(timestamp)
        formatted_time = current_datetime.strftime('%Y-%m-%d-%H-%M-%S')
        # print(formatted_time)
        file.write(f'{formatted_time}, {extracted} \n')


# def read(extracted):
#     with open("data.txt", "r") as file:
#         return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
