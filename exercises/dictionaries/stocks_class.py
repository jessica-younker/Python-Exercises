# Create a simple dictionary with ticker symbols and company names.

# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

# Create a second purchase summary which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

stockDict = {"SUN": "Sunoco", "MDT": "Medtronic", "COST": "Costco"}

purchases = [ ( 'SUN', 100, '4-apr-2017', 200 ), # 0 ticker symbol, 1 number of shares, 2 dates, 3 price
 ( 'MDT', 100, '2-nov-2012', 342 ),
 ( 'COST', 200, '5-oct-2001', 99 ), ( 'COST', 150, '17-oct-2009', 800 ) , ('MDT', 34, '6-nov-2010', 356 ) ]


portfolio = dict()

for purchase in purchases:
    ticker = purchase[0]
    full_company_name = stockDict[ticker]
    number_of_shares = purchase[1] #gets the index from purchase array to know which number is the number of shares
    purchase_price = purchase[3] #gets the index from purchase array to know which number is the price of each share
    full_purchase_price = number_of_shares * purchase_price

    try:
        portfolio[ticker].append(purchase)
    except KeyError:
        portfolio[ticker] = list()
        portfolio[ticker].append(purchase)

    print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))


for ticker, purchases in portfolio.items():
    print(ticker)
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print(purchase)
    print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))