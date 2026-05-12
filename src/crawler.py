import requests

def request_website():
    try:
        req = requests.get('https://quotes.toscrape.com/')
        print("Accessing Website: Status " + str(req.status_code))
    except:
        print("Something went wrong, please try again later!")

    return req.text