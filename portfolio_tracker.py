##STOCK PORTFOLIO TRACKER

import yfinance as yf  # Import the yfinance library for accessing stock data
import requests  # Import the requests library for making HTTP requests

# Print the file location of the requests module
print(requests.__file__)
# Print the Session class from the requests module
print(requests.Session)

class StockPortfolio:
    def __init__(self):
        # Initialize an empty dictionary to store the portfolio
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        # Add shares of a stock to the portfolio
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares

    def remove_stock(self, ticker, shares):
        # Remove shares of a stock from the portfolio
        if ticker in self.portfolio:
            self.portfolio[ticker] -= shares
            # If the number of shares becomes zero or less, remove the stock from the portfolio
            if self.portfolio[ticker] <= 0:
                del self.portfolio[ticker]
        else:
            # Print a message if the stock is not found in the portfolio
            print(f"No stock with ticker {ticker} found in portfolio.")

    def get_portfolio_value(self):
        # Calculate the total value of the portfolio
        total_value = 0
        for ticker, shares in self.portfolio.items():
            stock = yf.Ticker(ticker)  # Get the stock data
            price = stock.history(period='1d')['Close'].iloc[0]  # Get the latest closing price
            total_value += shares * price  # Calculate the total value for this stock
        return total_value

    def display_portfolio(self):
        # Display the current stocks in the portfolio
        for ticker, shares in self.portfolio.items():
            stock = yf.Ticker(ticker)  # Get the stock data
            price = stock.history(period='1d')['Close'].iloc[0]  # Get the latest closing price
            # Print the stock ticker, number of shares, and price per share
            print(f"{ticker}: {shares} shares at ${price:.2f} each")

def main():
    portfolio = StockPortfolio()  # Create an instance of the StockPortfolio class

    while True:
        # Print the menu options
        print("\n1. Add Stock\n2. Remove Stock\n3. Display Portfolio\n4. Get Portfolio Value\n5. Exit")
        choice = input("Choose an option: ")  # Get user input for the menu choice

        if choice == '1':
            # Add stock to the portfolio
            ticker = input("Enter the stock ticker symbol: ").upper()  # Get the stock ticker symbol from the user
            shares = int(input("Enter the number of shares: "))  # Get the number of shares from the user
            portfolio.add_stock(ticker, shares)
        elif choice == '2':
            # Remove stock from the portfolio
            ticker = input("Enter the stock ticker symbol: ").upper()  # Get the stock ticker symbol from the user
            shares = int(input("Enter the number of shares to remove: "))  # Get the number of shares to remove
            portfolio.remove_stock(ticker, shares)
        elif choice == '3':
            # Display the portfolio
            portfolio.display_portfolio()
        elif choice == '4':
            # Get and display the total portfolio value
            value = portfolio.get_portfolio_value()
            print(f"Total portfolio value: ${value:.2f}")
        elif choice == '5':
            # Exit the program
            break
        else:
            # Print a message for invalid options
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()  # Run the main function
