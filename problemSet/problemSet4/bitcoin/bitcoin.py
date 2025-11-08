import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin_amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument must be a number")

try:
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=cf92993f912f101b3552e21411d5a32f08f40ccf4140f2e03015179184967bc0"
    response = requests.get(url)

    data = response.json()
    price_usd = data["data"]["priceUsd"]
    price_usd = float(price_usd)

    price = price_usd * bitcoin_amount

    print(f"${price:,.4f}")
except requests.RequestException:
    pass
