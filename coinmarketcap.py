import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get the API_KEY from the environment variables
API_KEY = os.getenv('API_KEY')

# Endpoint URL for the CoinMarketCap API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Define headers required for the API request
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

def get_crypto_data():
    try:
        # Sending a GET request to the API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extracting data for the first 20 cryptocurrencies
            for i in range(20):
                cryptocurrency = data['data'][i]
                name = cryptocurrency['name']
                symbol = cryptocurrency['symbol']
                price = cryptocurrency['quote']['USD']['price']
                print(f"{name} ({symbol}): ${price}")
        else:
            print("Error:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    get_crypto_data()
