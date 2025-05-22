import yfinance as yf
from tabulate import tabulate

class Stock:
    def __init__(self, symbol, quantity, buy_price):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.buy_price = buy_price

    def fetch_current_price(self):
        try:
            stock_info = yf.Ticker(self.symbol)
            return stock_info.history(period="1d")['Close'][-1]
        except Exception as e:
            print(f"Error fetching price for {self.symbol}: {e}")
            return None

    def market_value(self):
        current_price = self.fetch_current_price()
        if current_price is None:
            return 0
        return self.quantity * current_price

    def gain_loss(self):
        current_price = self.fetch_current_price()
        if current_price is None:
            return 0
        return (current_price - self.buy_price) * self.quantity


class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity, buy_price):
        self.stocks[symbol.upper()] = Stock(symbol, quantity, buy_price)

    def remove_stock(self, symbol):
        self.stocks.pop(symbol.upper(), None)

    def show_portfolio(self):
        table = []
        total_value = 0
        total_gain = 0

        for stock in self.stocks.values():
            current_price = stock.fetch_current_price()
            if current_price is None:
                continue

            value = stock.market_value()
            gain = stock.gain_loss()
            total_value += value
            total_gain += gain

            table.append([
                stock.symbol,
                stock.quantity,
                f"${stock.buy_price:.2f}",
                f"${current_price:.2f}",
                f"${value:.2f}",
                f"${gain:.2f}"
            ])

        headers = ["Symbol", "Qty", "Buy Price", "Current Price", "Market Value", "Gain/Loss"]
        print(tabulate(table, headers=headers))
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
        print(f"Total Gain/Loss: ${total_gain:.2f}")


# Sample usage
if __name__ == "__main__":
    portfolio = Portfolio()
    portfolio.add_stock("AAPL", 10, 150)   #Apple
    portfolio.add_stock("GOOGL", 5, 2700)  #Google
    portfolio.add_stock("MSFT", 8, 300)     #Microsoft
    portfolio.add_stock("AMZN", 3, 150)      # Amazon
    portfolio.add_stock("TSLA", 8, 100)      # Tesla
    portfolio.add_stock("META", 4, 250)      # Meta (Facebook)

    portfolio.show_portfolio()
