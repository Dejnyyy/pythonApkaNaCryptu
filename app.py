from flask import Flask, render_template
import os
from dotenv import load_dotenv
import requests

app = Flask(__name__)

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
            crypto_data = []
            for i in range(20):
                cryptocurrency = data['data'][i]
                name = cryptocurrency['name']
                symbol = cryptocurrency['symbol']
                price = cryptocurrency['quote']['USD']['price']
                crypto_data.append({'name': name, 'symbol': symbol, 'price': price})
            return crypto_data
        else:
            return "Error: Unable to fetch data from API"
    except Exception as e:
        return "An error occurred: " + str(e)

@app.route('/')
def index():
    crypto_data = get_crypto_data()
    return render_template('index.html', crypto_data=crypto_data)

if __name__ == "__main__":
    app.run(debug=True)
