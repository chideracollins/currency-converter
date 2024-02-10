import os
from requests import get
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.freecurrencyapi.com/v1/"


def make_request(url):
    try:
        response = get(url)
        return response.json()
    except:
        print(
            "You need an internet connection to access the website!\nRetry after you establish one."
        )
        quit()


def fetch_data(currencies):
    latest_url = f"{BASE_URL}latest?apikey={API_KEY}&currencies"
    status_url = f"{BASE_URL}status?apikey={API_KEY}"
    try:
        data = make_request(f"{latest_url}={currencies}")["data"]
    except:
        valid_curr_abbr = list(make_request(latest_url)["data"].keys())
        print("Invalid currency abbreviation!")
        print(
            f"Here is a list of valid currencies abbreviation that can be checked -> {valid_curr_abbr}"
        )
        return
    status = make_request(status_url)
    total__avail_req, remaining_req = (
        status["quotas"]["month"]["total"],
        status["quotas"]["month"]["remaining"],
    )
    print(f"Here is the data -> {data}")
    print(
        f"NB: You have {remaining_req} remaining requests out of, {total__avail_req} total free requests for the month."
    )


while True:
    currencies_to_check = [
        word.upper()
        for word in input(
            "Enter the currencies abbreviation you would want to see, leaving a space after each or 'q' to quit: "
        ).split()
    ]
    if currencies_to_check[0] == "Q":
        print("Bye!")
        break
    fetch_data("%2C".join(currencies_to_check))
