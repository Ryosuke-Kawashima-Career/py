def solution():
    poems = []
    with open("poem.txt", "r") as file:
        for word in file.read().split():
            poems.append(word.strip().lower())
    word_frequencies = {}
    for word in poems:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    max_frequency = max(word_frequencies.values())
    for word, freq in word_frequencies.items():
        if freq == max_frequency:
            print(word)

def solution2():
    stocks = {}
    cur_row = 0
    col_names = []
    with open("stocks.csv", "r") as file:
        if cur_row == 0:
            col_names = file.readline().strip().split(",")
            for col_name in col_names:
                stocks[col_name.strip()] = []
            cur_row += 1
        else:
            values = file.readline.strip().split()
            for i in range(len(col_names)):
                stocks[col_names[i].strip()].append(values[i])
    
    new_data = {}
    new_data["Company Name"] = []
    new_data["PE Ratio"] = []
    new_data["PB Ratio"] = []
    for i, company_name in enumerate(stocks["Company Name"]):
        new_data["Company Name"].append(company_name)
        pe_ratio = float(stocks["Price"][i]) / float(stocks["EPS"][i])
        pb_ratio = float(stocks["Price"][i]) / float(stocks["Book Value per Share"][i])
        new_data["PE Ratio"].append(pe_ratio)
        new_data["PB Ratio"].append(pb_ratio)
    
    cur_row_output = 0
    with open("output.csv", "w") as file:
        if cur_row_output == 0:
            file.write("Company Name,PE Ratio,PB Ratio\n")
            cur_row_output += 1
        else:
            for i in range(len(new_data["Company Name"])):
                file.write(f"{new_data['Company Name'][i]},{new_data['PE Ratio'][i]},{new_data['PB Ratio'][i]}\n")

if __name__ == "__main__":
    solution()
    solution2()
