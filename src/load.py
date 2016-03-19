import csv

def readStocks(filePath):
    stocks = []
    stocksFile = open(filePath)
    reader = csv.reader(stocksFile)
    next(reader) # Skip the first headers row.
    for row in reader:
        firstArray = row[0].split("(")
        name = firstArray[0].strip()
        secondArray = firstArray[1].split(")")
        quote = secondArray[0].strip()
        stock = { "name": name, "quote": quote }
        stocks.append(stock)
    return stocks