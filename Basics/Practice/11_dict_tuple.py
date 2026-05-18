def solution():
    coutry_to_population = {
        "China": 143, 
        "India": 136, 
        "USA": 32, 
        "Pakistan": 21
    }
    query = input("Enter your query: ")
    if query == "print":
        for coutry, population in coutry_to_population.items():
            print(f"{coutry} ==> {population}")
    elif query == "add":
        coutry = input("Enter country name: ")
        population = int(input("Enter population: "))
        coutry_to_population[coutry] = population
    elif query == "remove":
        coutry = input("Enter country name: ")
        if coutry in coutry_to_population:
            del coutry_to_population[coutry]
        else:
            print("Country doesn't exist")
    elif query == "query":
        coutry = input("Enter country name: ")
        print(coutry_to_population[coutry])
    else:
        print("Invalid query")

def solution2():
    stocks = {
        "info": [600, 630, 620],
        "ril": [1430, 1490, 1567],
        "mtl": [234, 180, 160]
    }
    query = input("Enter your query: ")
    if query == "print":
        for stock, prices in stocks.items():
            print(f"{stock} ==> {prices} ==> avg: {sum(prices)/len(prices)}")
    elif query == "add":
        stock = input("Enter stock name: ")
        price = int(input("Enter price: "))
        stocks.get(stock, []).append(price)
    elif query == "remove":
        stock = input("Enter stock name: ")
        if stock in stocks:
            del stocks[stock]
        else:
            print("Stock doesn't exist")
    elif query == "query":
        stock = input("Enter stock name: ")
        print(stocks[stock])
    else:
        print("Invalid query")



if __name__ == "__main__":
    solution()