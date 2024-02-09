import requests

API_KEY = "fca_live_kHC29x5KWJmI4PjoHfJ2ZfLxfxpdgduS3OQPTgwl"
BASE_URL = f"https://api.freecurrencyapi.com/v1/"


def make_request(url):
    response = requests.get(url)
    return response.json()


def fetch_data(currencies):
    latest_url = f"{BASE_URL}latest?apikey={API_KEY}&currencies={currencies}"
    status_url = f"{BASE_URL}status?apikey={API_KEY}"
    data = make_request(latest_url)["data"]
    total__avail_req, remaining_req = (
        make_request(status_url)["quotas"]["month"]["total"],
        make_request(status_url)["quotas"]["month"]["remaining"],
    )
    print(f"Here is the data -> {data}")
    print(
        f"NB: You have {remaining_req} remaining requests out of, {total__avail_req} total free requests."
    )


while True:
    currencies_to_check = [
        word.upper()
        for word in input(
            "Enter the currencies you would want to see in their code or 'q' to quit: "
        ).split()
    ]
    if currencies_to_check[0] == "Q":
        print("Bye!")
        break
    fetch_data("%2C".join(currencies_to_check))

# https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_kHC29x5KWJmI4PjoHfJ2ZfLxfxpdgduS3OQPTgwl&currencies=EUR%2CUSD%2CCAD
# https://api.freecurrencyapi.com/v1/status?apikey=fca_live_kHC29x5KWJmI4PjoHfJ2ZfLxfxpdgduS3OQPTgwl
