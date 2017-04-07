stockDict = { 'GM': 'General Motors',
    'CAT':'Caterpillar', 'EK':'Eastman Kodak', 'DOG':'Dogerpillar', 
    'SM': 'Specific Motors', 'WP': 'Westwoman Polaroid' }


purchases = [ ( 'SM', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), 
 	( 'GM', 200, '1-jul-1998', 56 ), ('DOG',  101, '1-mar-1999', 24), ('WP', 99, '1-may-1998', 15), 
 	( 'SM', 105, '10-sep-2001', 48 ), ( 'CAT', 102, '1-apr-1999', 24 ), 
 	( 'GM', 204, '1-jul-1998', 56 ), ('DOG',  103, '1-mar-1999', 24), ('WP', 98, '1-may-1998', 15)]

for block in purchases:
	ticker_name = stockDict[block[0]]
	stock_cost = (block[1]*block[3])
	print(ticker_name)
	print(stock_cost)
	print("------")

combined_purchase_history = dict()

for ticker in stockDict:
	combined_purchase_history[ticker] = (block[1]*block[3])
	print(combined_purchase_history)





#try/except



# combined_purchase_history = {GM: $$$, EK: $$$}


#create dict where key = ticker and value = list of blocks purchased
#one pass through data to create the dict


#  Create a purchase history report that computes the full purchase price 
#  (shares times dollars) for each block of stock and uses the stockDict to 
#  look up the full company name. This is the basic relational database join 
#  algorithm between two tables.

# Create a second purchase summary that accumulates total investment by 
# ticker symbol. In the above sample data, there are two blocks of GE. These can easily 
# be combined by creating a dict where the key is the ticker and the value is the list of 
# blocks purchased. The program makes one pass through the data to create the dict. A pass 
# through the dict can then create a report showing each ticker symbol and all blocks of stock. ]