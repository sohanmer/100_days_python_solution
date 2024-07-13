import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = '<account_sid>'
auth_token = '<auth_token>'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "<api_key>"
}

news_parameters = {
    "qInTitle""": COMPANY_NAME,
    "apikey": "<api_key>"
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
percent_diff = (difference / float(yesterday_closing_price  )) * 100

if percent_diff > 5:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    articles = response.json()['articles'][:3]
    msg = [f"Headline:{article['title']}. \nBrief: {article['description']}" for article in articles]

    client = Client(account_sid, auth_token)

    message = client.messages.create(
      body=msg,
      from_='<twilio_number>',
      to='<your_number'
    )

    print(message.status)
