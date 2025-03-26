import yfinance as yt
import plotly.express as px

def plot_price(ticker):
    """
    A function to plot the close 
    price given a ticker.
    """

    data = yf.download(
        ticker,
        multi_level_index = False
    )

    fig = px.line(
        data.reset_index(),
        x = 'Date', y = ['Close']
    )

    return fig

def get_stock_data(ticker, start_date, end_data):
    """obtém dados históricos de ações do Yahoo Fiance"""
    stock = yt.Ticker(ticker)
    data = stock.history(start=start_date, end=end_data)
    return data

ticker = "AAPL" 
start_date= "2024-01-01"
end_data= "2024-03-01"

data= get_stock_data(ticker, start_date, end_data)
print(data.head())